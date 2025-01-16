# GitScan

[English](#english) | [中文](#中文)

<a name="english"></a>
## Git Repository Analysis Tool

GitScan is a powerful tool designed to analyze Git repositories and provide insights into commit history, contributor statistics, and code change trends.

### Features

- Repository Management
  - Add local and remote Git repositories
  - View repository list
  - Analyze repository statistics
- Code Statistics
  - Time range filtering (year, quarter, month, week, day)
  - Code line count statistics
  - Contributor analysis
  - Time series trend charts
- Modern Web Interface
  - Responsive design
  - Real-time data visualization
  - Interactive statistical charts

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GitScan.git
   cd GitScan
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the server:
   ```bash
   python main.py
   ```

2. Open your browser and visit:
   ```
   http://localhost:8006
   ```

3. Add a repository and analyze it:
   - Click "Add Repository"
   - Enter repository path
   - Click "Analyze" to generate statistics
   - View detailed statistics by clicking "View Statistics"

### API Endpoints

- `GET /api/repositories`: List all repositories
- `POST /api/repositories`: Add a new repository
- `GET /api/analyze/{repo_id}`: Analyze a repository
- `GET /api/statistics/{repo_id}`: Get repository statistics

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<a name="中文"></a>
## Git 仓库分析工具

GitScan 是一个强大的工具，用于分析 Git 仓库并提供提交历史、贡献者统计和代码变更趋势的洞察。

### 功能特点

- 仓库管理
  - 添加本地和远程 Git 仓库
  - 查看仓库列表
  - 分析仓库统计信息
- 代码统计
  - 时间范围筛选（年、季度、月、周、日）
  - 代码行数统计
  - 贡献者分析
  - 时间序列趋势图
- 现代化 Web 界面
  - 响应式设计
  - 实时数据可视化
  - 交互式统计图表

### 安装说明

1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/GitScan.git
   cd GitScan
   ```

2. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

### 使用方法

1. 启动服务器：
   ```bash
   python main.py
   ```

2. 打开浏览器访问：
   ```
   http://localhost:8006
   ```

3. 添加仓库并分析：
   - 点击"添加仓库"
   - 输入仓库路径
   - 点击"分析"生成统计信息
   - 点击"查看统计"查看详细统计

### API 接口

- `GET /api/repositories`: 列出所有仓库
- `POST /api/repositories`: 添加新仓库
- `GET /api/analyze/{repo_id}`: 分析仓库
- `GET /api/statistics/{repo_id}`: 获取仓库统计信息

### 贡献指南

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解行为准则以及提交拉取请求的流程。

### 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。
