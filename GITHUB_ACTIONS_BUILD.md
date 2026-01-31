# 🤖 GitHub Actions - Android APK Build

This repository is configured to automatically build Android APK files using GitHub Actions.

## 📋 How It Works

The workflow automatically builds the Android APK whenever you:
- Push code to the `main` or `develop` branch
- Create a pull request to `main`
- Manually trigger the workflow from GitHub

## 🚀 Manual Build Instructions

### Option 1: Push to GitHub (Automatic)

1. Commit your changes:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. The workflow will automatically start building

3. Check the progress:
   - Go to your GitHub repository
   - Click on the **Actions** tab
   - You'll see the build in progress

### Option 2: Manual Trigger

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. Select **Build Android APK** workflow
4. Click **Run workflow** button
5. Select the branch and click **Run workflow**

## 📦 Download the APK

Once the build completes:

1. Go to the **Actions** tab in your GitHub repository
2. Click on the completed workflow run
3. Scroll down to the **Artifacts** section
4. Download one of these files:
   - `water-tracker-debug-apk` - Debug version (for testing)
   - `water-tracker-release-apk-unsigned` - Release version (needs signing)

## 📱 Installing the APK

### Debug APK (for testing)

1. Download the `water-tracker-debug-apk` artifact
2. Extract the ZIP file to get `app-debug.apk`
3. Transfer to your Android device
4. Enable "Install from Unknown Sources" in Settings
5. Tap the APK file to install

### Release APK (for distribution)

The release APK needs to be signed before distribution:

1. Download the `water-tracker-release-apk-unsigned` artifact
2. Sign it using your keystore (see signing instructions below)
3. Distribute the signed APK

## 🔐 Signing the Release APK

To sign the release APK for distribution:

```bash
# Generate a keystore (first time only)
keytool -genkey -v -keystore water-tracker.keystore \
  -alias water-tracker \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000

# Sign the APK
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore water-tracker.keystore \
  app-release-unsigned.apk \
  water-tracker

# Verify the signature
jarsigner -verify -verbose -certs app-release-unsigned.apk

# Optimize with zipalign (if available)
zipalign -v 4 app-release-unsigned.apk app-release-signed.apk
```

## 🔧 Workflow Configuration

The workflow is defined in `.github/workflows/build-android-apk.yml`

### What it does:

1. ✅ Sets up Node.js 20
2. ✅ Sets up JDK 17
3. ✅ Installs Android SDK
4. ✅ Installs Cordova
5. ✅ Installs project dependencies
6. ✅ Adds Android platform
7. ✅ Builds debug APK
8. ✅ Builds release APK (unsigned)
9. ✅ Uploads APKs as artifacts

### Build Environment:

- **OS**: Ubuntu Latest
- **Node.js**: 20.x
- **Java**: JDK 17 (Temurin)
- **Cordova**: Latest version
- **Android SDK**: Automatically configured

## 📊 Build Status

You can add a build status badge to your README:

```markdown
![Build Status](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Build%20Android%20APK/badge.svg)
```

## 🐛 Troubleshooting

### Build fails

1. Check the Actions tab for error logs
2. Ensure `config.xml` is properly configured
3. Verify all dependencies in `package.json`

### APK not found

1. Check if the build completed successfully
2. Look for the Artifacts section at the bottom of the workflow run
3. Artifacts are kept for 30 days

### Can't install APK on device

1. Enable "Install from Unknown Sources"
2. For release APK, ensure it's properly signed
3. Check Android version compatibility (min SDK 24 / Android 7.0)

## 📝 Notes

- **Debug APK**: Ready to install immediately, includes debugging symbols
- **Release APK**: Smaller, optimized, but requires signing before distribution
- **Artifacts**: Automatically deleted after 30 days
- **Build time**: Typically 3-5 minutes

## 🎯 Next Steps

1. Push your code to GitHub
2. Wait for the workflow to complete
3. Download the APK from the Artifacts section
4. Install and test on your Android device

---

**Need help?** Check the [Cordova Android Documentation](https://cordova.apache.org/docs/en/latest/guide/platforms/android/)
