from flask import Flask, request, jsonify, send_from_directory
from sqlalchemy.orm import sessionmaker
from git import Repo
import os
from datetime import datetime, timedelta
import models
from sqlalchemy import create_engine
from typing import Dict, Any
import tempfile
import shutil

app = Flask(__name__, static_url_path='/static')

# 创建数据库引擎和会话
engine = create_engine('sqlite:///gitscan.db')
SessionLocal = sessionmaker(bind=engine)

# 确保数据库表存在
models.Base.metadata.create_all(engine)

# 挂载静态文件
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# 创建仓库存储目录
REPOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'repos')
if not os.path.exists(REPOS_DIR):
    os.makedirs(REPOS_DIR)

@app.route('/')
def read_root():
    return send_from_directory('static', 'index.html')

@app.route('/api/repositories', methods=['POST'])
def add_repository() -> Dict[str, Any]:
    db = SessionLocal()
    try:
        # 从查询参数或表单数据中获取路径
        path = request.args.get('path') or request.form.get('path')
        if not path:
            # 尝试从 JSON 数据中获取
            data = request.get_json(silent=True)
            if data:
                path = data.get('path')
        
        if not path:
            return jsonify({"error": "Path parameter is required"}), 400

        # 判断是本地路径还是远程 URL
        is_remote = path.startswith(('http://', 'https://', 'git://'))
        
        if is_remote:
            # 对于远程仓库，先克隆到本地临时目录
            repo_name = os.path.splitext(os.path.basename(path))[0]
            local_path = os.path.join(REPOS_DIR, repo_name)
            
            # 如果目录已存在，先删除
            if os.path.exists(local_path):
                shutil.rmtree(local_path)
            
            # 克隆仓库
            repo = Repo.clone_from(path, local_path)
            path = local_path
        else:
            # 本地仓库，直接使用路径
            repo = Repo(path)
            repo_name = os.path.basename(path)

        # 创建仓库记录
        db_repo = models.Repository(
            name=repo_name,
            path=path,
            url=path if is_remote else None
        )
        db.add(db_repo)
        db.commit()
        
        return jsonify({"status": "success", "repository_id": db_repo.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

@app.route('/api/repositories', methods=['GET'])
def list_repositories():
    db = SessionLocal()
    try:
        repositories = db.query(models.Repository).all()
        return jsonify([{
            'id': repo.id,
            'name': repo.name,
            'path': repo.path,
            'last_updated': repo.last_updated.isoformat() if repo.last_updated else None,
            'last_analyzed': repo.last_analyzed.isoformat() if repo.last_analyzed else None
        } for repo in repositories])
    finally:
        db.close()

@app.route('/api/stats/<int:repo_id>', methods=['GET'])
def get_repository_stats(repo_id: int) -> Dict[str, Any]:
    db = SessionLocal()
    try:
        time_range = request.args.get('time_range', 'all')  # all, year, quarter, month, week, day
        repo = db.query(models.Repository).filter(models.Repository.id == repo_id).first()
        if not repo:
            return jsonify({"error": "Repository not found"}), 404
        
        # 构建时间过滤条件
        now = datetime.utcnow()
        if time_range == 'year':
            start_date = now - timedelta(days=365)
        elif time_range == 'quarter':
            start_date = now - timedelta(days=90)
        elif time_range == 'month':
            start_date = now - timedelta(days=30)
        elif time_range == 'week':
            start_date = now - timedelta(days=7)
        elif time_range == 'day':
            start_date = now - timedelta(days=1)
        else:  # all
            start_date = None
        
        # 查询提交记录
        commits_query = db.query(models.Commit).filter(
            models.Commit.repository_id == repo_id
        )
        if start_date:
            commits_query = commits_query.filter(models.Commit.date >= start_date)
        
        commits = commits_query.all()
        
        # 统计数据
        total_commits = len(commits)
        total_insertions = sum(c.insertions or 0 for c in commits)
        total_deletions = sum(c.deletions or 0 for c in commits)
        
        # 按作者分组的提交数和代码行数
        author_stats = {}
        for commit in commits:
            if commit.author not in author_stats:
                author_stats[commit.author] = {
                    'commits': 0,
                    'insertions': 0,
                    'deletions': 0,
                    'net_changes': 0
                }
            author_stats[commit.author]['commits'] += 1
            author_stats[commit.author]['insertions'] += commit.insertions or 0
            author_stats[commit.author]['deletions'] += commit.deletions or 0
            author_stats[commit.author]['net_changes'] += (commit.insertions or 0) - (commit.deletions or 0)
        
        # 按时间统计代码行数变化
        time_series = {}
        for commit in commits:
            date_key = commit.date.strftime('%Y-%m-%d')
            if date_key not in time_series:
                time_series[date_key] = {
                    'insertions': 0,
                    'deletions': 0,
                    'net_changes': 0
                }
            time_series[date_key]['insertions'] += commit.insertions or 0
            time_series[date_key]['deletions'] += commit.deletions or 0
            time_series[date_key]['net_changes'] += (commit.insertions or 0) - (commit.deletions or 0)
        
        return jsonify({
            "time_range": time_range,
            "total_commits": total_commits,
            "total_insertions": total_insertions,
            "total_deletions": total_deletions,
            "net_changes": total_insertions - total_deletions,
            "author_stats": author_stats,
            "time_series": time_series
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@app.route('/api/analyze/<int:repo_id>', methods=['POST'])
def analyze_repository(repo_id: int):
    db = SessionLocal()
    try:
        repo = db.query(models.Repository).filter(models.Repository.id == repo_id).first()
        if not repo:
            return jsonify({"error": "Repository not found"}), 404

        repo_path = repo.path
        if not os.path.exists(repo_path):
            return jsonify({"error": "Repository path does not exist"}), 404

        git_repo = Repo(repo_path)
        commits = []
        for commit in git_repo.iter_commits():
            try:
                stats = commit.stats.total
                commits.append(models.Commit(
                    repository_id=repo.id,
                    hash=commit.hexsha,
                    author=commit.author.name,
                    date=datetime.fromtimestamp(commit.committed_date),
                    message=commit.message,
                    insertions=stats.get('insertions', 0),
                    deletions=stats.get('deletions', 0)
                ))
            except Exception as e:
                print(f"Error processing commit {commit.hexsha}: {str(e)}")
                continue

        # 清除旧的提交记录
        db.query(models.Commit).filter(models.Commit.repository_id == repo.id).delete()
        
        # 添加新的提交记录
        db.add_all(commits)
        
        # 更新仓库的分析时间
        repo.last_analyzed = datetime.utcnow()
        
        db.commit()
        return jsonify({"message": "Analysis completed successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8006, debug=True)
