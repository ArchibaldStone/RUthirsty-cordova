# Cordova APK Build Troubleshooting Guide

## Common Build Errors

### 1. Gradle Build Failures

#### Error: "Could not find gradle wrapper"

**Cause**: Gradle wrapper not initialized in Android platform

**Solution**:
```bash
cd platforms/android
./gradlew wrapper
cd ../..
cordova build android
```

#### Error: "Gradle sync failed"

**Cause**: Corrupted Gradle cache or incompatible versions

**Solution**:
```bash
# Clean Gradle cache
rm -rf ~/.gradle/caches/

# Clean and rebuild
cordova clean android
cordova build android
```

#### Error: "Execution failed for task ':app:processDebugResources'"

**Cause**: Resource conflicts or invalid XML in resources

**Solution**:
1. Check config.xml for invalid characters
2. Verify all image resources are valid
3. Clean and rebuild:
```bash
cordova clean android
cordova platform remove android
cordova platform add android
cordova build android
```

### 2. SDK and Environment Issues

#### Error: "Failed to find 'ANDROID_HOME'"

**Cause**: ANDROID_HOME environment variable not set

**Solution**:
```bash
# Linux/macOS
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export ANDROID_HOME=$HOME/Android/Sdk' >> ~/.bashrc
echo 'export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools' >> ~/.bashrc
source ~/.bashrc
```

#### Error: "Android SDK not found"

**Cause**: Android SDK not installed or path incorrect

**Solution**:
1. Install Android Studio or SDK Command-line Tools
2. Set ANDROID_HOME to SDK location
3. Verify with: `echo $ANDROID_HOME`

#### Error: "Failed to find target with hash string 'android-34'"

**Cause**: Required Android SDK platform not installed

**Solution**:
```bash
# Using sdkmanager
sdkmanager "platforms;android-34"
sdkmanager "build-tools;34.0.0"

# Or install via Android Studio SDK Manager
```

### 3. Java Version Issues

#### Error: "Unsupported Java version" or "Java version mismatch"

**Cause**: Incompatible Java version (need JDK 11 or 17)

**Solution**:
```bash
# Check current Java version
java -version

# Install JDK 11 (Ubuntu/Debian)
sudo apt install openjdk-11-jdk

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

# Verify
java -version
```

#### Error: "JAVA_HOME is not set"

**Solution**:
```bash
# Find Java installation
which java
# or
/usr/libexec/java_home -V  # macOS

# Set JAVA_HOME
export JAVA_HOME=/path/to/jdk
```

### 4. Platform Issues

#### Error: "Current working directory is not a Cordova-based project"

**Cause**: Running command outside Cordova project directory

**Solution**:
```bash
# Navigate to project directory
cd /path/to/your/cordova/project

# Verify config.xml exists
ls config.xml
```

#### Error: "Platform android not found"

**Cause**: Android platform not added to project

**Solution**:
```bash
# Add Android platform
cordova platform add android

# Verify platforms
cordova platform ls
```

#### Error: "Platform android already added"

**Cause**: Trying to add platform that already exists

**Solution**:
```bash
# Remove and re-add platform
cordova platform remove android
cordova platform add android
```

### 5. Build Output Issues

#### Error: "APK not found at expected location"

**Cause**: Build failed silently or output path changed

**Solution**:
```bash
# Check build output
cordova build android --verbose

# Look for APK in alternative locations
find platforms/android -name "*.apk"

# Common locations:
# platforms/android/app/build/outputs/apk/debug/app-debug.apk
# platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

### 6. Signing Issues

#### Error: "jarsigner: unable to sign jar"

**Cause**: Invalid keystore or incorrect password

**Solution**:
1. Verify keystore exists and path is correct
2. Check keystore password
3. Verify key alias exists:
```bash
keytool -list -v -keystore my-release-key.keystore
```

#### Error: "apksigner not found"

**Cause**: Android SDK build-tools not in PATH

**Solution**:
```bash
# Add build-tools to PATH
export PATH=$PATH:$ANDROID_HOME/build-tools/34.0.0

# Or use jarsigner instead (fallback)
```

### 7. Device/Emulator Issues

#### Error: "device unauthorized"

**Cause**: USB debugging not authorized on device

**Solution**:
1. On device: Allow USB debugging authorization popup
2. Reconnect device
3. Verify: `adb devices`

#### Error: "No devices found"

**Cause**: No Android device/emulator connected

**Solution**:
```bash
# Check connected devices
adb devices

# For physical device:
# - Enable USB debugging in Developer Options
# - Connect via USB
# - Authorize computer on device

# For emulator:
# - Start emulator from Android Studio
# - Or: emulator -avd <avd_name>
```

### 8. Memory Issues

#### Error: "OutOfMemoryError" during build

**Cause**: Insufficient memory allocated to Gradle

**Solution**:
Create/edit `~/.gradle/gradle.properties`:
```properties
org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m
org.gradle.daemon=true
org.gradle.parallel=true
```

### 9. Network Issues

#### Error: "Could not download" or "Connection timeout"

**Cause**: Network issues downloading dependencies

**Solution**:
```bash
# Use a mirror or proxy
# Edit gradle.properties to add proxy settings

# Or download dependencies manually
# Clear Gradle cache and retry
rm -rf ~/.gradle/caches/
cordova build android
```

### 10. Plugin Issues

#### Error: "Plugin not found" or "Plugin version conflict"

**Cause**: Incompatible or missing Cordova plugins

**Solution**:
```bash
# List installed plugins
cordova plugin ls

# Remove problematic plugin
cordova plugin remove <plugin-id>

# Re-add plugin
cordova plugin add <plugin-id>

# Or update all plugins
cordova plugin update
```

## General Troubleshooting Steps

### Clean Build Process

When encountering persistent issues, try a complete clean build:

```bash
# 1. Clean build artifacts
cordova clean android

# 2. Remove and re-add platform
cordova platform remove android
cordova platform add android

# 3. Clear Gradle cache
rm -rf ~/.gradle/caches/

# 4. Rebuild
cordova build android --verbose
```

### Verbose Output

Always use `--verbose` flag to see detailed error messages:

```bash
cordova build android --verbose
```

### Check Logs

View detailed Android logs:

```bash
# View all logs
adb logcat

# Filter by app
adb logcat | grep "YourAppName"

# Clear logs first
adb logcat -c
```

### Verify Environment

Run environment check before building:

```bash
# Check Cordova requirements
cordova requirements

# Or use the check_environment.py script
python3 scripts/check_environment.py
```

## Platform-Specific Issues

### Linux

- Ensure proper permissions for Android SDK directory
- May need to add user to `plugdev` group for USB debugging

### macOS

- May need to install Xcode Command Line Tools
- Use `brew` to install Java and other dependencies

### Windows

- Use forward slashes in paths or escape backslashes
- May need to run Command Prompt as Administrator
- Ensure environment variables are set in System Properties

## Getting Help

If issues persist:

1. Check Cordova documentation: https://cordova.apache.org/docs/
2. Search Cordova issues: https://github.com/apache/cordova-android/issues
3. Check Stack Overflow with tag `cordova`
4. Run `cordova info` to get system information for bug reports
