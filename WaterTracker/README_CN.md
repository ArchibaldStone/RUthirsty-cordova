# 喝水打卡 - Water Tracker App

一个炫酷的喝水打卡应用，采用红黑科技风格设计，帮助您养成健康的饮水习惯。

## 功能特点

- ✅ **一键打卡**: 简单快捷的喝水记录功能
- 📊 **实时统计**: 显示今日饮水量和目标完成度
- 📝 **记录列表**: 详细展示每次喝水的时间
- 🎯 **健康提醒**: 智能提示还需补充多少水量
- 🎨 **炫酷界面**: 红黑科技风格，视觉效果出众
- 💾 **数据持久化**: 使用 localStorage 保存数据
- 📅 **日期显示**: 实时显示当前日期和星期

## 技术栈

- **框架**: Apache Cordova
- **前端**: HTML5 + CSS3 + JavaScript
- **平台**: Android (可扩展至 iOS)
- **存储**: localStorage

## 项目结构

```
WaterTracker/
├── www/
│   ├── index.html          # 主页面
│   ├── css/
│   │   └── index.css       # 样式文件（红黑科技风格）
│   ├── js/
│   │   └── index.js        # 主要逻辑
│   └── img/                # 图片资源
├── platforms/
│   └── android/            # Android 平台文件
├── config.xml              # Cordova 配置文件
└── package.json            # 项目依赖
```

## 安装和构建

### 前置要求

1. **Node.js** (v14 或更高版本)
2. **Cordova CLI**
   ```bash
   npm install -g cordova
   ```

3. **Android 开发环境**:
   - Java JDK 8 或更高版本
   - Android SDK
   - Gradle

### 环境配置

1. 安装 Android SDK:
   ```bash
   # 下载 Android Studio 或 Android SDK Command-line Tools
   # 设置环境变量
   export ANDROID_HOME=$HOME/Android/Sdk
   export PATH=$PATH:$ANDROID_HOME/tools
   export PATH=$PATH:$ANDROID_HOME/platform-tools
   ```

2. 验证环境:
   ```bash
   cordova requirements
   ```

### 构建步骤

1. **克隆或进入项目目录**:
   ```bash
   cd WaterTracker
   ```

2. **安装依赖**:
   ```bash
   npm install
   ```

3. **添加 Android 平台** (如果还没有):
   ```bash
   cordova platform add android
   ```

4. **构建 APK**:
   ```bash
   # 调试版本
   cordova build android

   # 发布版本
   cordova build android --release
   ```

5. **在设备上运行**:
   ```bash
   # 连接 Android 设备并启用 USB 调试
   cordova run android
   ```

6. **在模拟器上运行**:
   ```bash
   cordova emulate android
   ```

### 浏览器预览

在开发过程中，可以在浏览器中预览应用:

```bash
cd www
python3 -m http.server 8080
# 然后在浏览器中访问 http://localhost:8080
```

## 使用说明

1. **打开应用**: 启动后会显示当前日期和饮水统计
2. **喝水打卡**: 点击中间的红色"喝水打卡"按钮记录一次饮水
3. **查看记录**: 下方列表显示今日所有饮水记录的时间
4. **查看进度**: 顶部显示今日饮水量和目标完成度
5. **清空记录**: 点击"清空"按钮可以清除今日所有记录

## 健康标准

- **每日目标**: 8 杯水
- **进度条**: 实时显示完成百分比
- **完成提示**: 达到目标后会显示祝贺信息

## 界面设计

### 配色方案
- **主色调**: 黑色 (#000000, #0a0a0a, #1a0000)
- **强调色**: 红色 (#ff0000, #ff3333, #ff6666)
- **文字色**: 白色 (#ffffff) 和灰色 (#999999, #666666)

### 设计特点
- 渐变背景营造科技感
- 发光效果和阴影增强视觉冲击
- 流畅的动画过渡
- 响应式按钮反馈
- 自定义滚动条样式

## 数据存储

应用使用 `localStorage` 存储数据:
- **存储键**: `waterTrackerData`
- **数据结构**:
  ```json
  {
    "date": "2026-01-31",
    "records": [
      {
        "time": "09:30:15",
        "timestamp": 1738315815000
      }
    ]
  }
  ```
- **自动重置**: 每天零点后首次打开会自动清空前一天的记录

## 兼容性

- **Android**: 5.0 (API 21) 及以上
- **浏览器**: Chrome, Firefox, Safari, Edge (现代浏览器)

## 自定义配置

### 修改每日目标

编辑 `www/js/index.js` 文件:
```javascript
const DAILY_GOAL = 8; // 修改为您想要的目标杯数
```

### 修改配色

编辑 `www/css/index.css` 文件，搜索颜色代码并替换:
- 红色: `#ff0000`, `#ff3333`, `#ff6666`
- 黑色: `#000000`, `#0a0a0a`, `#1a0000`

## 故障排除

### 构建失败
- 确保已安装所有前置要求
- 运行 `cordova requirements` 检查环境
- 清理并重新构建: `cordova clean && cordova build android`

### 应用无法启动
- 检查 Android 设备是否启用了 USB 调试
- 确认设备已正确连接: `adb devices`
- 查看日志: `adb logcat`

### 数据丢失
- 检查浏览器/应用是否清除了缓存
- localStorage 数据存储在应用私有目录中

## 开发计划

- [ ] 添加自定义每日目标设置
- [ ] 支持不同容量的杯子（小杯、中杯、大杯）
- [ ] 添加饮水提醒通知功能
- [ ] 历史数据统计和图表展示
- [ ] 多语言支持
- [ ] iOS 平台支持

## 许可证

本项目基于 Apache License 2.0 开源。

## 联系方式

如有问题或建议，欢迎提交 Issue 或 Pull Request。

---

**享受健康的饮水生活！💧**
