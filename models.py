from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

Base = declarative_base()

class Repository(Base):
    __tablename__ = "repositories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String)
    url = Column(String, nullable=True)  
    last_updated = Column(DateTime, default=datetime.utcnow)
    last_analyzed = Column(DateTime)  
    commits = relationship("Commit", back_populates="repository", cascade="all, delete-orphan")

class Commit(Base):
    __tablename__ = "commits"
    
    id = Column(Integer, primary_key=True, index=True)
    repository_id = Column(Integer, ForeignKey("repositories.id", ondelete="CASCADE"))
    hash = Column(String, index=True)
    author = Column(String)
    date = Column(DateTime)
    message = Column(Text)
    files_changed = Column(Integer)
    insertions = Column(Integer)
    deletions = Column(Integer)
    repository = relationship("Repository", back_populates="commits")

# 全局数据库引擎和会话工厂
engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal
    
    # 如果已经初始化，直接返回
    if engine is not None:
        return engine, SessionLocal
    
    # 根据环境选择数据库 URL
    if os.environ.get('VERCEL_ENV') == 'production':
        db_url = 'sqlite:///:memory:'
    else:
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gitscan.db')
        db_url = f'sqlite:///{db_path}'
    
    # 创建数据库引擎
    engine = create_engine(
        db_url,
        connect_args={'check_same_thread': False}
    )
    
    # 创建会话工厂
    session_factory = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
    
    # 使用 scoped_session 来确保线程安全
    SessionLocal = scoped_session(session_factory)
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    return engine, SessionLocal

# 初始化数据库
engine, SessionLocal = init_db()
