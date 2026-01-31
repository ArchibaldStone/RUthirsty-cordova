# 📱 Android 构建完整指南

## 🎯 前提条件

### 必需软件

1. **Node.js** (v14+)
   - 下载: https://nodejs.org/

2. **Java JDK** (JDK 8 或 JDK 11)
   ```bash
   # 检查 Java 版本
   java -version
   javac -version
   ```

3. **Android Studio**
   - 下载: https://developer.android.com/studio
   - 或 Android SDK Command-line Tools

4. **Gradle** (通常随 Android Studio 安装)

5. **Cordova CLI**
   ```bash
   npm install -g cordova
   ```

---

## 🔧 环境配置

### 1. 安装 Android SDK

#### 方法 A: 使用 Android Studio (推荐)

1. 下载并安装 Android Studio
2. 打开 Android Studio
3. 进入 **Tools** → **SDK Manager**
4. 安装以下组件:
   - ✅ Android SDK Platform 34
   - ✅ Android SDK Build-Tools 34.0.0
   - ✅ Android SDK Platform-Tools
   - ✅ Android SDK Tools
   - ✅ Android Emulator (可选)

#### 方法 B: 使用命令行工具

```bash
# 下载 Android SDK Command-line Tools
# https://developer.android.com/studio#command-tools

# 解压到指定目录
mkdir -p ~/Android/Sdk
cd ~/Android/Sdk
unzip commandlinetools-*.zip

# 安装必需组件
./cmdline-tools/bin/sdkmanager --sdk_root=$HOME/Android/Sdk \
  "platform-tools" "platforms;android-34" "build-tools;34.0.0"
```

### 2. 配置环境变量

#### Linux / macOS

编辑 `~/.bashrc` 或 `~/.zshrc`:

```bash
# Android SDK
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/emulator

# Java (如果需要)
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
```

应用配置:
```bash
source ~/.bashrc  # 或 source ~/.zshrc
```

#### Windows

1. 右键 **此电脑** → **属性** → **高级系统设置** → **环境变量**
2. 添加系统变量:
   - `ANDROID_HOME` = `C:\Users\YourName\AppData\Local\Android\Sdk`
   - `JAVA_HOME` = `C:\Program Files\Java\jdk-11`
3. 编辑 `Path` 变量，添加:
   - `%ANDROID_HOME%\tools`
   - `%ANDROID_HOME%\platform-tools`
   - `%JAVA_HOME%\bin`

### 3. 验证环境

```bash
# 检查 Cordova
cordova --version

# 检查 Java
java -version

# 检查 Android SDK
adb version

# 检查 Cordova 环境
cd /workspaces/RUthirsty-cordova/WaterTracker
cordova requirements
```

预期输出:
```
Requirements check results for android:
Java JDK: installed ✅
Android SDK: installed ✅
Android target: installed ✅
Gradle: installed ✅
```

---

## 🏗️ 构建 APK

### 方法 1: 使用构建脚本 (推荐)

```bash
cd /workspaces/RUthirsty-cordova/WaterTracker

# 运行构建脚本
./build.sh

# 选择选项:
# 1 - 构建调试版本
# 2 - 构建发布版本
```

### 方法 2: 手动构建

#### 构建调试版本 (Debug APK)

```bash
cd /workspaces/RUthirsty-cordova/WaterTracker

# 构建
cordova build android

# 或指定平台
cordova build android --debug
```

**APK 位置**:
```
platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

#### 构建发布版本 (Release APK)

```bash
cd /workspaces/RUthirsty-cordova/WaterTracker

# 构建未签名的发布版本
cordova build android --release

# APK 位置
# platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

---

## 🔐 签名 APK (发布版本)

### 1. 生成密钥库

```bash
keytool -genkey -v -keystore water-tracker.keystore \
  -alias water-tracker \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000

# 按提示输入信息:
# - 密钥库密码
# - 姓名、组织等信息
# - 密钥密码
```

### 2. 签名 APK

```bash
# 使用 jarsigner
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore water-tracker.keystore \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk \
  water-tracker

# 或使用 apksigner (推荐)
apksigner sign --ks water-tracker.keystore \
  --out app-release-signed.apk \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

### 3. 验证签名

```bash
jarsigner -verify -verbose -certs \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

---

## 📲 安装到设备

### 方法 1: 使用 Cordova (推荐)

```bash
cd /workspaces/RUthirsty-cordova/WaterTracker

# 连接 Android 设备 (USB 调试模式)
# 运行应用
cordova run android

# 或指定设备
cordova run android --device
```

### 方法 2: 使用 ADB

```bash
# 检查连接的设备
adb devices

# 安装 APK
adb install platforms/android/app/build/outputs/apk/debug/app-debug.apk

# 或强制重新安装
adb install -r platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

### 方法 3: 手动安装

1. 将 APK 文件传输到 Android 设备
2. 在设备上:
   - 进入 **设置** → **安全** → 启用 **未知来源**
   - 使用文件管理器找到 APK
   - 点击安装

---

## 🧪 测试

### 在真实设备上测试

1. **启用 USB 调试**:
   - 设置 → 关于手机 → 连续点击 "版本号" 7 次
   - 返回 → 开发者选项 → 启用 USB 调试

2. **连接设备**:
   ```bash
   adb devices
   # 应该显示你的设备
   ```

3. **运行应用**:
   ```bash
   cordova run android
   ```

### 在模拟器上测试

1. **创建模拟器** (Android Studio):
   - Tools → AVD Manager → Create Virtual Device
   - 选择设备型号和系统镜像
   - 启动模拟器

2. **运行应用**:
   ```bash
   cordova emulate android
   ```

---

## 🐛 故障排除

### 问题 1: Gradle 构建失败

**错误**: `Could not find gradle wrapper`

**解决**:
```bash
cd platforms/android
./gradlew wrapper
cd ../..
cordova build android
```

### 问题 2: SDK 未找到

**错误**: `Failed to find 'ANDROID_HOME'`

**解决**:
```bash
# 设置环境变量
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# 或在 ~/.bashrc 中永久设置
```

### 问题 3: Java 版本不兼容

**错误**: `Unsupported Java version`

**解决**:
```bash
# 安装 JDK 11
sudo apt install openjdk-11-jdk

# 设置 JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### 问题 4: 设备未授权

**错误**: `device unauthorized`

**解决**:
1. 在设备上允许 USB 调试授权
2. 重新连接设备
3. 运行 `adb devices` 确认

### 问题 5: 构建缓存问题

**解决**:
```bash
# 清理构建
cordova clean android

# 删除平台并重新添加
cordova platform remove android
cordova platform add android

# 重新构建
cordova build android
```

---

## 📊 构建优化

### 减小 APK 大小

1. **启用代码压缩**:
   编辑 `platforms/android/app/build.gradle`:
   ```gradle
   android {
       buildTypes {
           release {
               minifyEnabled true
               shrinkResources true
           }
       }
   }
   ```

2. **移除未使用的资源**:
   ```bash
   cordova build android --release -- --minifyEnabled=true
   ```

### 提高构建速度

1. **启用 Gradle 守护进程**:
   创建 `~/.gradle/gradle.properties`:
   ```properties
   org.gradle.daemon=true
   org.gradle.parallel=true
   org.gradle.configureondemand=true
   ```

2. **增加 Gradle 内存**:
   ```properties
   org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m
   ```

---

## 📦 发布到 Google Play

### 1. 准备发布

- ✅ 测试所有功能
- ✅ 签名 APK
- ✅ 准备应用图标 (512x512)
- ✅ 准备截图 (多种尺寸)
- ✅ 编写应用描述
- ✅ 设置隐私政策

### 2. 创建 Google Play 开发者账号

- 访问: https://play.google.com/console
- 支付一次性注册费 ($25)

### 3. 上传 APK

1. 创建新应用
2. 填写应用信息
3. 上传签名的 APK
4. 设置定价和分发
5. 提交审核

---

## ✅ 构建检查清单

构建前检查:
- [ ] 环境变量已配置
- [ ] Cordova 已安装
- [ ] Android SDK 已安装
- [ ] Java JDK 已安装
- [ ] config.xml 配置正确
- [ ] 代码已测试

构建后检查:
- [ ] APK 文件生成成功
- [ ] APK 大小合理 (~2MB)
- [ ] 在设备上安装成功
- [ ] 应用启动正常
- [ ] 所有功能工作正常
- [ ] 无崩溃或错误

---

## 🎉 快速构建命令

```bash
# 完整构建流程
cd /workspaces/RUthirsty-cordova/WaterTracker

# 1. 检查环境
cordova requirements

# 2. 清理旧构建
cordova clean android

# 3. 构建 APK
cordova build android

# 4. 安装到设备
cordova run android

# 5. 查看日志
adb logcat | grep "WaterTracker"
```

---

**构建状态**: ✅ 就绪
**兼容性**: ✅ Android 7.0+
**文档**: ✅ 完整

**准备好构建您的 Android 应用了！** 🚀
