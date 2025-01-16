# Contributing to GitScan

[English](#english) | [中文](#中文)

<a name="english"></a>
## Contributing Guidelines

We're excited that you're interested in contributing to GitScan! This document will guide you through the contribution process.

### Development Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Testing related changes
- `chore`: Build process or auxiliary tool changes

Examples:
```
feat: add time range filtering for statistics
fix: resolve modal scrolling issue
docs: update installation guide
```

### Code Style

- Follow PEP 8 for Python code
- Use 4 spaces for indentation
- Keep code simple and clear
- Add necessary comments
- Use meaningful variable and function names

### Testing

- Add unit tests for new features
- Ensure all tests pass
- Keep test code maintainable

### Documentation

- Update README.md to reflect changes
- Add necessary code comments
- Update API documentation if changed

### Issue Reporting

When creating an issue, include:

1. Issue description
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment information
   - Python version
   - Operating system
   - Dependency versions

### Feature Suggestions

When suggesting new features:

1. Clearly describe the feature
2. Explain why it's needed
3. Provide possible implementation approaches
4. Consider backward compatibility

---

<a name="中文"></a>
## 贡献指南

我们很高兴你有兴趣为 GitScan 做出贡献！这个文档将指导你如何参与项目开发。

### 开发流程

1. Fork 项目仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的改动 (`git commit -m 'feat: add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个 Pull Request

### 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat`: 新功能
- `fix`: 修复问题
- `docs`: 文档修改
- `style`: 代码格式修改
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat: 添加时间范围筛选功能
fix: 修复模态框滚动问题
docs: 更新安装指南
```

### 代码风格

- Python 代码遵循 PEP 8 规范
- 使用 4 个空格进行缩进
- 保持代码简洁明了
- 添加必要的注释
- 使用有意义的变量和函数名

### 测试

- 为新功能添加单元测试
- 确保所有测试通过
- 保持测试代码的可维护性

### 文档

- 更新 README.md 反映新的变化
- 添加必要的代码注释
- 更新 API 文档（如果有变动）

### 问题报告

创建 issue 时请包含：

1. 问题描述
2. 复现步骤
3. 预期行为
4. 实际行为
5. 环境信息
   - Python 版本
   - 操作系统
   - 相关依赖版本

### 功能建议

提出新功能建议时请：

1. 清晰描述新功能
2. 解释为什么需要这个功能
3. 提供可能的实现方案
4. 考虑向后兼容性

## 开发环境设置

1. 克隆项目：
   ```bash
   git clone <your-fork-url>
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

## 分支策略

- `main`: 主分支，保持稳定
- `develop`: 开发分支
- `feature/*`: 新功能分支
- `fix/*`: 问题修复分支
- `docs/*`: 文档更新分支

## 发布流程

1. 更新版本号
2. 更新 CHANGELOG.md
3. 创建发布标签
4. 推送到 GitHub
5. 创建 Release 说明

## 联系方式

如有任何问题，请通过 Issues 或 Discussions 联系我们。

感谢你的贡献！
