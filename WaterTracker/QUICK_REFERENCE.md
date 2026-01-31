# 🚀 快速参考 - Quick Reference

## 访问应用 / Access App
```
http://localhost:8080
```

## 服务器管理 / Server Management

```bash
cd /workspaces/RUthirsty-cordova/WaterTracker

# 查看状态
./dev-server.sh status

# 启动
./dev-server.sh start

# 停止
./dev-server.sh stop

# 重启
./dev-server.sh restart

# 查看日志
./dev-server.sh logs

# 实时日志
./dev-server.sh follow
```

## 项目结构 / Project Structure

```
WaterTracker/
├── www/
│   ├── index.html          # 主页面
│   ├── css/index.css       # 样式
│   └── js/index.js         # 功能
├── dev-server.sh           # 服务器管理脚本
└── build.sh                # 构建脚本
```

## 开发工作流 / Development Workflow

1. 访问 http://localhost:8080
2. 编辑 www/ 目录中的文件
3. 保存文件 (Ctrl+S)
4. 浏览器自动刷新 ✨

## 常用命令 / Common Commands

```bash
# 查看进程
ps aux | grep live-server | grep -v grep

# 查看日志
tail -f /tmp/live-server.log

# 停止服务器
pkill -f "live-server"

# 构建 APK
./build.sh
```

## 文件位置 / File Locations

- **HTML**: `www/index.html`
- **CSS**: `www/css/index.css`
- **JS**: `www/js/index.js`
- **日志**: `/tmp/live-server.log`

## 快速修改 / Quick Edits

### 修改颜色
```bash
vim www/css/index.css
# 搜索 #ff0000 (红色)
```

### 修改目标
```bash
vim www/js/index.js
# 修改 DAILY_GOAL = 8
```

### 修改文字
```bash
vim www/index.html
# 修改标题和按钮文字
```

## 调试工具 / Debug Tools

- **F12**: 打开开发者工具
- **Ctrl+Shift+M**: 移动端模拟器
- **Ctrl+Shift+C**: 元素选择器
- **Ctrl+Shift+I**: 检查元素

## 文档索引 / Documentation

- `README_CN.md` - 完整文档
- `QUICKSTART.md` - 快速开始
- `HOT_RELOAD.md` - 热重载说明
- `热重载启动成功.md` - 启动指南

## 状态检查 / Status Check

```bash
# 一键检查所有状态
./dev-server.sh status
```

---

**当前状态**: ✅ 运行中
**访问地址**: http://localhost:8080
**热重载**: ✅ 启用
