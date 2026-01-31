---
name: cordova-apk-builder
description: Build, sign, and deploy Android APK packages from Cordova applications. Use when users need to package Cordova apps into APK files, including debug builds for testing, release builds for distribution, APK signing with keystores, environment verification, or troubleshooting build issues. Supports automated building, signing workflows, and deployment to devices.
---

# Cordova APK Builder

Automates the process of building, signing, and deploying Android APK packages from Cordova applications.

## Quick Start

### Build Debug APK

```bash
python3 scripts/build_apk.py /path/to/cordova/project
```

### Build Release APK

```bash
python3 scripts/build_apk.py /path/to/cordova/project --release
```

### Sign Release APK

```bash
python3 scripts/sign_apk.py \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk \
  --keystore my-release-key.keystore \
  --alias my-key-alias
```

## Scripts

### build_apk.py

Builds Android APK from Cordova project.

**Usage**:
```bash
python3 scripts/build_apk.py [PROJECT_DIR] [OPTIONS]
```

**Options**:
- `--release`: Build release APK instead of debug
- `--clean`: Clean build artifacts before building
- `--skip-checks`: Skip environment requirement checks

**Examples**:
```bash
# Build debug APK in current directory
python3 scripts/build_apk.py

# Build release APK with clean
python3 scripts/build_apk.py /path/to/project --release --clean

# Build without environment checks
python3 scripts/build_apk.py --skip-checks
```

**Output Locations**:
- Debug: `platforms/android/app/build/outputs/apk/debug/app-debug.apk`
- Release: `platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk`

### sign_apk.py

Signs Android APK with keystore for release distribution.

**Usage**:
```bash
python3 scripts/sign_apk.py APK_PATH --keystore KEYSTORE --alias ALIAS [OPTIONS]
```

**Options**:
- `--keystore`: Path to keystore file (required)
- `--alias`: Key alias in keystore (required)
- `--output`: Output path for signed APK (default: <apk>-signed.apk)
- `--zipalign`: Optimize APK with zipalign before signing
- `--verify`: Verify signature after signing (default: true)

**Examples**:
```bash
# Basic signing
python3 scripts/sign_apk.py app-release-unsigned.apk \
  --keystore release.keystore \
  --alias release-key

# Sign with zipalign optimization
python3 scripts/sign_apk.py app-release-unsigned.apk \
  --keystore release.keystore \
  --alias release-key \
  --zipalign \
  --output app-signed.apk
```

### check_environment.py

Verifies that all required tools for Cordova Android builds are installed.

**Usage**:
```bash
python3 scripts/check_environment.py [OPTIONS]
```

**Options**:
- `--project-dir`: Cordova project directory (for requirements check)

**Checks**:
- Node.js and npm
- Cordova CLI
- Java JDK and JAVA_HOME
- Android SDK and ANDROID_HOME
- Gradle
- Cordova requirements (if project directory provided)

**Example**:
```bash
# Check environment
python3 scripts/check_environment.py

# Check with Cordova project
python3 scripts/check_environment.py --project-dir /path/to/project
```

## Workflows

### Complete Debug Build Workflow

```bash
# 1. Check environment
python3 scripts/check_environment.py --project-dir .

# 2. Build debug APK
python3 scripts/build_apk.py . --clean

# 3. Install on device (if connected)
adb install -r platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

### Complete Release Build and Sign Workflow

```bash
# 1. Check environment
python3 scripts/check_environment.py --project-dir .

# 2. Build release APK
python3 scripts/build_apk.py . --release --clean

# 3. Sign APK
python3 scripts/sign_apk.py \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk \
  --keystore my-release-key.keystore \
  --alias my-key-alias \
  --zipalign \
  --output app-release-signed.apk

# 4. Verify signature
apksigner verify -v app-release-signed.apk
```

### First-Time Setup Workflow

```bash
# 1. Check what's missing
python3 scripts/check_environment.py

# 2. Install missing components (example for Ubuntu)
# Install Java JDK
sudo apt install openjdk-11-jdk

# Install Android SDK (via Android Studio or command-line tools)
# Set environment variables
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Install Cordova
npm install -g cordova

# 3. Verify setup
python3 scripts/check_environment.py --project-dir .

# 4. Build
python3 scripts/build_apk.py .
```

## Creating a Keystore

Generate a new keystore for signing release APKs:

```bash
keytool -genkey -v \
  -keystore my-release-key.keystore \
  -alias my-key-alias \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000
```

**Important**:
- Keep keystore file secure and backed up
- Remember passwords (cannot be recovered)
- Store keystore outside project directory
- Never commit keystore to version control

For detailed signing information, see [references/signing_guide.md](references/signing_guide.md).

## Manual Cordova Commands

If you prefer manual control:

```bash
# Check requirements
cordova requirements

# Build debug
cordova build android

# Build release
cordova build android --release

# Clean
cordova clean android

# Run on device
cordova run android

# Run on emulator
cordova emulate android
```

## Troubleshooting

### Common Issues

**Build fails with Gradle errors**:
```bash
# Clean and rebuild
cordova clean android
cordova platform remove android
cordova platform add android
cordova build android
```

**ANDROID_HOME not set**:
```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

**Java version issues**:
```bash
# Install JDK 11
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

**APK not found**:
```bash
# Find APK location
find platforms/android -name "*.apk"
```

For comprehensive troubleshooting, see [references/troubleshooting.md](references/troubleshooting.md).

## Environment Requirements

### Required Software

- **Node.js** (v14+)
- **npm**
- **Cordova CLI** (`npm install -g cordova`)
- **Java JDK** (JDK 11 or JDK 17)
- **Android SDK** (via Android Studio or command-line tools)
- **Gradle** (usually included with Android SDK)

### Environment Variables

```bash
# Required
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Recommended
export JAVA_HOME=/path/to/jdk
export PATH=$PATH:$JAVA_HOME/bin
```

### Android SDK Components

Install via Android Studio SDK Manager or sdkmanager:
- Android SDK Platform (matching targetSdkVersion in config.xml)
- Android SDK Build-Tools
- Android SDK Platform-Tools
- Android SDK Tools

## APK Output Locations

### Debug APK
```
platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

### Release APK (unsigned)
```
platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

### Signed APK
```
<output-path-specified> or <apk-name>-signed.apk
```

## Best Practices

### Development

1. **Use debug builds for testing**: Faster builds, no signing required
2. **Test on real devices**: Emulators may not catch all issues
3. **Check environment first**: Run `check_environment.py` before building
4. **Clean builds when switching**: Use `--clean` flag when switching between debug/release

### Release

1. **Always sign release APKs**: Required for distribution
2. **Use zipalign**: Optimizes APK for better performance
3. **Verify signatures**: Always verify after signing
4. **Test signed APK**: Install and test before distribution
5. **Keep keystore secure**: Store safely with backups

### Security

1. **Never commit keystores**: Add `*.keystore` to .gitignore
2. **Never commit build.json with passwords**: Use environment variables
3. **Use strong passwords**: For keystores and keys
4. **Backup keystores**: Store encrypted backups in multiple locations
5. **Limit keystore access**: Only authorized personnel

## Additional Resources

- **Signing Guide**: [references/signing_guide.md](references/signing_guide.md) - Comprehensive APK signing documentation
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md) - Solutions to common build issues
- **Cordova Docs**: https://cordova.apache.org/docs/
- **Android Developer**: https://developer.android.com/studio/publish/app-signing

## Quick Command Reference

```bash
# Environment check
python3 scripts/check_environment.py --project-dir .

# Build debug
python3 scripts/build_apk.py .

# Build release
python3 scripts/build_apk.py . --release --clean

# Sign APK
python3 scripts/sign_apk.py <apk> --keystore <keystore> --alias <alias> --zipalign

# Install on device
adb install -r <apk>

# View device logs
adb logcat | grep <app-name>
```
