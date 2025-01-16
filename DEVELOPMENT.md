# GitScan 开发记录

本文档记录了 GitScan 项目的完整开发过程，包括需求变更、功能迭代和问题修复。

[English](#english) | [中文](#中文)

<a name="english"></a>
## Development Documentation

This document records the complete development process of the GitScan project, including requirement changes, feature iterations, and issue fixes.

### Complete Dialogue Record

#### Initial Development Phase

**User**: Help me implement a Git repository analysis tool that can analyze code commit trends and data

*[System started implementing basic functionality]*

#### Feature Enhancement Phase

**User**: Now I want to add code commit line count statistics, which can be filtered by time range, such as past year, past quarter, past month, past week, past day, etc.

*[System implemented time range filtering and statistics]*

#### UI Optimization Phase

**User**: Please fix the issue where the detail modal cannot be scrolled. Also, when clicking operations like Add Repository, Analyze, etc., provide users with a waiting status display to prevent confusion about task status.

*[System fixed scrolling issues and added loading states]*

**User**: Very good, but when selecting filters for past quarter and past month, it shows "Unexpected token '<', "<!doctype "... is not valid JSON"

*[System fixed date calculation issues]*

**User**: Now it shows "Failed to load repository list"

*[System fixed database structure issues]*

**User**: Now repositories that have been analyzed once still have their View Statistics button disabled, normally it should be clickable after a repository has been analyzed.

*[System fixed button state logic]*

### Development Phases

#### Phase 1: Basic Functionality Implementation
- Created basic project structure
- Implemented repository management
- Established database models
- Developed simple web interface

#### Phase 2: Code Statistics Enhancement
- Implemented multiple time range filtering options
- Added code line count statistics
- Integrated data visualization

#### Phase 3: UI Optimization and Bug Fixes

1. Modal Scrolling
   - Fixed detail modal scrolling issue
   - Optimized modal layout

2. User Experience
   - Added loading state indicators
   - Optimized button state logic
   - Improved error handling

3. Data Processing
   - Fixed date calculation issues
   - Improved database structure
   - Added last_analyzed field

#### Phase 4: Environment Configuration and Deployment

**Issue**: Encountered deployment issues on Vercel and database configuration challenges.

1. Database Configuration Optimization
   - Simplified database configuration for both local and Vercel environments
   - Improved session management and connection handling
   - Added proper error handling and connection cleanup

2. Environment-Specific Settings
   - Local Development:
     ```python
     # Uses file-based SQLite database
     db_path = os.path.join(BASE_DIR, 'gitscan.db')
     # Persistent repository storage
     REPOS_DIR = os.path.join(BASE_DIR, 'repos')
     ```
   
   - Vercel Environment:
     ```python
     # Uses in-memory SQLite database
     db_url = 'sqlite:///:memory:'
     # Temporary repository storage
     REPOS_DIR = tempfile.mkdtemp()
     ```

3. Code Improvements
   - Enhanced database session management
   - Added cascade delete support for repositories and commits
   - Improved error handling and transaction management
   - Optimized database connection configuration

4. Dependencies Update
   ```
   flask==3.0.0
   gitpython==3.1.31
   sqlalchemy==1.4.41
   aiofiles==23.1.0
   werkzeug==3.0.1
   ```

#### Current Status
- Local development environment is functioning correctly with persistent storage
- Database operations are properly handled with transaction support
- Environment-specific configurations are in place
- Pending verification of Vercel deployment

#### Next Steps
1. Test and verify local development functionality
2. Address Vercel deployment issues
3. Implement proper error logging for production environment
4. Consider adding database migration support

### Technical Improvements

#### Database Optimization
- Added last_analyzed field
- Optimized database structure
- Improved error handling mechanism

#### UI Improvements
- Implemented responsive layout
- Added loading state indicators
- Optimized modal interactions

#### Code Quality
- Standardized code structure
- Added error handling
- Improved documentation

### Environment Configuration

#### Local Development Environment

1. Create `.env.local` file in project root:
   ```env
   VERCEL_ENV=
   DEBUG=True
   ```

2. Local environment characteristics:
   - Uses file-based SQLite database (`gitscan.db`)
   - Persistent repository storage in `repos/` directory
   - Database and repositories persist between restarts

3. Database location:
   - Database file: `gitscan.db` in project root
   - Repository storage: `repos/` directory in project root

#### Vercel Deployment Environment

1. Set environment variables in Vercel project settings:
   - Navigate to Project Settings > Environment Variables
   - Add variable:
     ```
     VERCEL_ENV=production
     ```

2. Vercel environment characteristics:
   - Uses in-memory SQLite database
   - Temporary repository storage
   - Data resets between deployments

3. Important considerations:
   - Data is not persistent in Vercel environment
   - Suitable for demonstration and testing
   - For production use, consider using persistent storage solutions

#### Environment Detection

The application automatically detects the environment and configures itself:
```python
# Database configuration
if os.environ.get('VERCEL_ENV'):
    # Vercel: Use in-memory database
    DATABASE_URL = 'sqlite:///:memory:'
else:
    # Local: Use file database
    DATABASE_URL = 'sqlite:///gitscan.db'

# Repository storage configuration
if os.environ.get('VERCEL_ENV'):
    # Vercel: Use temporary directory
    REPOS_DIR = tempfile.mkdtemp()
else:
    # Local: Use persistent directory
    REPOS_DIR = os.path.join(BASE_DIR, 'repos')
```

### Todo List

#### Performance Optimization
- [ ] Optimize large repository analysis
- [ ] Add data caching mechanism
- [ ] Improve data loading speed

#### Feature Enhancement
- [ ] Add more statistical dimensions
- [ ] Support more time range options
- [ ] Add data export functionality

#### User Experience
- [ ] Add more interactive feedback
- [ ] Optimize mobile adaptation
- [ ] Add theme switching

### Technical Debt

#### Code Quality
- [ ] Add unit tests
- [ ] Improve error handling
- [ ] Optimize code structure

#### Documentation
- [ ] Add API documentation
- [ ] Complete development documentation
- [ ] Add deployment documentation

#### Security
- [ ] Add access control
- [ ] Improve error handling
- [ ] Enhance input validation

---

<a name="中文"></a>
## 开发文档

本文档记录了 GitScan 项目的完整开发过程，包括需求变更、功能迭代和问题修复。

### 完整对话记录

#### 初始开发阶段

**用户**: 帮我实现一个 Git 代码仓库分析工具，可以分析代码提交趋势与数据

*[系统开始实现基础功能]*

#### 功能增强阶段

**用户**: 现在我想增加代码提交行数统计，可以按照时间范围进行筛选，比如过去一年、过去一季度、过去一个月、过去一周、过去一天等等

*[系统实现了时间范围筛选和统计功能]*

#### UI 优化阶段

**用户**: 请修复 详情弹窗无法滚动浏览的问题。并在点击 添加仓库、分析 等等候操作时，给予用户等候中的状态展示，以防止用户对任务状态的模糊认知导致误解。

*[系统修复了滚动问题并添加了加载状态]*

**用户**: 很不错，但是在选择筛选 过去一个季度 和 过去一个月 的时候，会显示 Unexpected token '<', "<!doctype "... is not valid JSON

*[系统修复了日期计算问题]*

**用户**: 现在显示 加载仓库列表失败

*[系统修复了数据库结构问题]*

**用户**: 现在已经分析过一次的仓库，其查看统计也仍然不可点击，正常的话是仓库经过一次分析之后，就可以查看统计了。

*[系统修复了按钮状态逻辑]*

### 开发阶段

#### 阶段一：基础功能实现
- 创建了基础项目结构
- 实现了仓库管理功能
- 建立了数据库模型
- 开发了简单的 Web 界面

#### 阶段二：代码统计功能增强
- 实现了多个时间范围的筛选选项
- 添加了代码行数统计功能
- 集成了数据可视化功能

#### 阶段三：UI 优化和问题修复

1. 弹窗滚动问题
   - 修复了详情弹窗无法滚动的问题
   - 优化了弹窗布局

2. 用户体验改进
   - 添加了加载状态指示
   - 优化了按钮状态逻辑
   - 改进了错误处理

3. 数据处理优化
   - 修复了日期计算问题
   - 改进了数据库结构
   - 添加了 last_analyzed 字段

#### 阶段四：环境配置和部署

**问题**: 遇到了 Vercel 部署问题和数据库配置挑战。

1. 数据库配置优化
   - 简化了数据库配置，适用于本地和 Vercel 环境
   - 改进了会话管理和连接处理
   - 添加了错误处理和连接清理

2. 环境特定设置
   - 本地开发：
     ```python
     # 使用基于文件的 SQLite 数据库
     db_path = os.path.join(BASE_DIR, 'gitscan.db')
     # 持久化存储仓库
     REPOS_DIR = os.path.join(BASE_DIR, 'repos')
     ```
   
   - Vercel 环境：
     ```python
     # 使用内存中的 SQLite 数据库
     db_url = 'sqlite:///:memory:'
     # 临时存储仓库
     REPOS_DIR = tempfile.mkdtemp()
     ```

3. 代码改进
   - 改进了数据库会话管理
   - 添加了级联删除支持
   - 改进了错误处理和事务管理
   - 优化了数据库连接配置

4. 依赖更新
   ```
   flask==3.0.0
   gitpython==3.1.31
   sqlalchemy==1.4.41
   aiofiles==23.1.0
   werkzeug==3.0.1
   ```

#### 当前状态
- 本地开发环境正常工作，具有持久化存储
- 数据库操作正确处理，具有事务支持
- 环境特定配置已就绪
- 等待 Vercel 部署验证

#### 下一步
1. 测试和验证本地开发功能
2. 解决 Vercel 部署问题
3. 实现生产环境错误日志记录
4. 考虑添加数据库迁移支持

### 技术改进

#### 数据库优化
- 添加了 last_analyzed 字段
- 优化了数据库结构
- 改进了错误处理机制

#### UI 改进
- 实现了响应式布局
- 添加了加载状态指示
- 优化了弹窗交互

#### 代码质量
- 规范了代码结构
- 添加了错误处理
- 完善了文档注释

### 环境配置

#### 本地开发环境

1. 在项目根目录创建 `.env.local` 文件：
   ```env
   VERCEL_ENV=
   DEBUG=True
   ```

2. 本地环境特点：
   - 使用基于文件的 SQLite 数据库（`gitscan.db`）
   - 在 `repos/` 目录中持久化存储仓库
   - 数据库和仓库在重启之间保持持久化

3. 数据库位置：
   - 数据库文件：项目根目录下的 `gitscan.db`
   - 仓库存储：项目根目录下的 `repos/` 目录

#### Vercel 部署环境

1. 在 Vercel 项目设置中设置环境变量：
   - 导航到 Project Settings > Environment Variables
   - 添加变量：
     ```
     VERCEL_ENV=production
     ```

2. Vercel 环境特点：
   - 使用内存中的 SQLite 数据库
   - 使用临时目录存储仓库
   - 数据在部署之间重置

3. 重要注意事项：
   - Vercel 环境中的数据不是持久化的
   - 适用于演示和测试
   - 如需生产环境使用，请考虑使用持久化存储解决方案

#### 环境检测

应用程序自动检测环境并配置自身：
```python
# 数据库配置
if os.environ.get('VERCEL_ENV'):
    # Vercel：使用内存数据库
    DATABASE_URL = 'sqlite:///:memory:'
else:
    # 本地：使用文件数据库
    DATABASE_URL = 'sqlite:///gitscan.db'

# 仓库存储配置
if os.environ.get('VERCEL_ENV'):
    # Vercel：使用临时目录
    REPOS_DIR = tempfile.mkdtemp()
else:
    # 本地：使用持久化目录
    REPOS_DIR = os.path.join(BASE_DIR, 'repos')
```

### 待办事项

#### 性能优化
- [ ] 优化大型仓库分析性能
- [ ] 添加数据缓存机制
- [ ] 改进数据加载速度

#### 功能增强
- [ ] 添加更多统计维度
- [ ] 支持更多时间范围选项
- [ ] 添加数据导出功能

#### 用户体验
- [ ] 添加更多交互反馈
- [ ] 优化移动端适配
- [ ] 添加主题切换功能

### 技术债务

#### 代码质量
- [ ] 添加单元测试
- [ ] 改进错误处理
- [ ] 优化代码结构

#### 文档完善
- [ ] 添加 API 文档
- [ ] 完善开发文档
- [ ] 添加部署文档

#### 安全性
- [ ] 添加访问控制
- [ ] 改进错误处理
- [ ] 加强输入验证
