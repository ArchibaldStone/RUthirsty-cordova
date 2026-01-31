# 快速开始指南 - Quick Start Guide

## 中文版

### 立即开始

1. **浏览器预览** (最快方式):
   ```bash
   cd WaterTracker/www
   python3 -m http.server 8080
   ```
   然后在浏览器中访问: http://localhost:8080

2. **使用构建脚本**:
   ```bash
   cd WaterTracker
   ./build.sh
   ```
   选择选项 5 进行浏览器预览

### 在 Android 设备上安装

#### 方法 1: 使用已有的 Android 开发环境

如果您已经安装了 Android Studio 和 SDK:

```bash
cd WaterTracker

# 检查环境
cordova requirements

# 构建 APK
cordova build android

# 安装到连接的设备
cordova run android
```

APK 文件位置: `platforms/android/app/build/outputs/apk/debug/app-debug.apk`

#### 方法 2: 在其他电脑上构建

1. 将整个 `WaterTracker` 文件夹复制到有 Android 开发环境的电脑
2. 运行上述命令

#### 方法 3: 直接安装 APK (如果已构建)

1. 将 APK 文件传输到 Android 设备
2. 在设备上启用"未知来源"安装
3. 点击 APK 文件进行安装

### 应用功能

- **打卡按钮**: 点击记录一次喝水
- **今日饮水量**: 显示今天喝了几杯水
- **目标完成度**: 显示完成百分比 (目标: 8杯/天)
- **进度条**: 可视化显示进度
- **记录列表**: 显示每次喝水的具体时间
- **清空按钮**: 清除今日所有记录

### 数据说明

- 数据保存在本地 (localStorage)
- 每天自动重置
- 不需要网络连接
- 不会上传任何数据

---

## English Version

### Get Started Immediately

1. **Browser Preview** (Fastest way):
   ```bash
   cd WaterTracker/www
   python3 -m http.server 8080
   ```
   Then visit in browser: http://localhost:8080

2. **Use Build Script**:
   ```bash
   cd WaterTracker
   ./build.sh
   ```
   Select option 5 for browser preview

### Install on Android Device

#### Method 1: Using Existing Android Development Environment

If you have Android Studio and SDK installed:

```bash
cd WaterTracker

# Check environment
cordova requirements

# Build APK
cordova build android

# Install to connected device
cordova run android
```

APK location: `platforms/android/app/build/outputs/apk/debug/app-debug.apk`

#### Method 2: Build on Another Computer

1. Copy entire `WaterTracker` folder to a computer with Android development environment
2. Run the commands above

#### Method 3: Direct APK Installation (if already built)

1. Transfer APK file to Android device
2. Enable "Unknown sources" installation on device
3. Tap APK file to install

### App Features

- **Check-in Button**: Tap to record water intake
- **Today's Water Intake**: Shows how many glasses today
- **Goal Completion**: Shows completion percentage (Goal: 8 glasses/day)
- **Progress Bar**: Visual progress display
- **Record List**: Shows specific time of each drink
- **Clear Button**: Remove all today's records

### Data Information

- Data saved locally (localStorage)
- Auto resets daily
- No network connection required
- No data uploaded

---

## 系统要求 / System Requirements

### 开发环境 / Development Environment
- Node.js 14+
- Cordova CLI
- Android SDK (for building APK)

### 运行环境 / Runtime Environment
- Android 5.0+ (API 21+)
- Modern web browser (for preview)

---

## 故障排除 / Troubleshooting

### 问题: Cordova 命令未找到
**解决**:
```bash
npm install -g cordova
```

### 问题: Android SDK 未安装
**解决**:
1. 下载 Android Studio: https://developer.android.com/studio
2. 安装 Android SDK
3. 设置环境变量 ANDROID_HOME

### 问题: 浏览器预览时功能不正常
**说明**: 某些 Cordova 特定功能在浏览器中可能受限，但核心功能（打卡、记录、统计）完全可用

### Problem: Cordova command not found
**Solution**:
```bash
npm install -g cordova
```

### Problem: Android SDK not installed
**Solution**:
1. Download Android Studio: https://developer.android.com/studio
2. Install Android SDK
3. Set ANDROID_HOME environment variable

### Problem: Browser preview not working properly
**Note**: Some Cordova-specific features may be limited in browser, but core features (check-in, records, statistics) work fully

---

## 联系支持 / Support

如有问题，请查看:
- README.md (English documentation)
- README_CN.md (中文文档)

For issues, please check:
- README.md (English documentation)
- README_CN.md (Chinese documentation)
