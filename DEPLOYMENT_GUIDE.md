# 部署指南 - Deployment Guide

## 🚀 快速部署 / Quick Deployment

### 选项 1: 浏览器预览 (立即可用)
```bash
cd WaterTracker/www
python3 -m http.server 8080
```
访问: http://localhost:8080

### 选项 2: Android APK 构建

#### 步骤 1: 安装依赖
```bash
# 安装 Node.js (如果未安装)
# 下载: https://nodejs.org/

# 安装 Cordova
npm install -g cordova

# 安装 Android Studio
# 下载: https://developer.android.com/studio
```

#### 步骤 2: 配置环境变量
```bash
# Linux/Mac
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Windows (PowerShell)
$env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk"
$env:PATH += ";$env:ANDROID_HOME\tools;$env:ANDROID_HOME\platform-tools"
```

#### 步骤 3: 构建 APK
```bash
cd WaterTracker

# 检查环境
cordova requirements

# 构建调试版本
cordova build android

# 或使用构建脚本
./build.sh
```

#### 步骤 4: 安装到设备
```bash
# 方法 1: 直接运行
cordova run android

# 方法 2: 手动安装
# APK 位置: platforms/android/app/build/outputs/apk/debug/app-debug.apk
# 将 APK 传输到设备并安装
```

## 📦 文件说明 / File Description

### 核心文件 / Core Files
- `www/index.html` - 主页面
- `www/css/index.css` - 样式文件
- `www/js/index.js` - 功能逻辑
- `config.xml` - Cordova 配置

### 文档文件 / Documentation
- `README.md` - 英文文档
- `README_CN.md` - 中文文档
- `QUICKSTART.md` - 快速开始
- `PROJECT_SUMMARY.md` - 项目总结
- `PREVIEW.md` - 界面预览

### 工具文件 / Tool Files
- `build.sh` - 构建脚本
- `package.json` - 项目依赖

## 🔧 常见问题 / FAQ

### Q: 如何修改应用名称？
A: 编辑 `config.xml` 中的 `<name>` 标签

### Q: 如何修改应用图标？
A: 替换 `www/img/` 目录中的图标文件

### Q: 如何修改每日目标？
A: 编辑 `www/js/index.js` 中的 `DAILY_GOAL` 常量

### Q: 如何更改配色？
A: 编辑 `www/css/index.css` 中的颜色值

### Q: 数据存储在哪里？
A: 使用 localStorage，存储在应用私有目录

### Q: 如何清除所有数据？
A: 在应用中点击"清空"按钮，或清除应用数据

## 📱 测试清单 / Testing Checklist

- [ ] 打卡按钮功能正常
- [ ] 记录列表显示正确
- [ ] 统计数据更新准确
- [ ] 进度条显示正确
- [ ] 日期显示正确
- [ ] 清空功能正常
- [ ] 数据持久化正常
- [ ] 跨天自动重置
- [ ] 界面显示美观
- [ ] 动画效果流畅

## 🎯 性能优化 / Performance

- ✅ 使用 CSS3 动画 (GPU 加速)
- ✅ 最小化 DOM 操作
- ✅ 使用事件委托
- ✅ localStorage 缓存
- ✅ 响应式设计

## 🔒 安全性 / Security

- ✅ 无网络请求
- ✅ 本地数据存储
- ✅ 无敏感信息
- ✅ CSP 策略配置

## 📊 应用信息 / App Info

- **名称**: WaterTracker (喝水打卡)
- **包名**: com.ruthirsty.watertracker
- **版本**: 1.0.0
- **平台**: Android 5.0+
- **大小**: ~2MB (APK)

## 🌟 特色功能 / Features

1. ✅ 一键打卡
2. ✅ 实时统计
3. ✅ 记录列表
4. ✅ 进度可视化
5. ✅ 健康提醒
6. ✅ 数据持久化
7. ✅ 炫酷界面
8. ✅ 离线可用

---

**部署状态**: ✅ 就绪
**预览地址**: http://localhost:8080
**文档完整**: ✅ 是
