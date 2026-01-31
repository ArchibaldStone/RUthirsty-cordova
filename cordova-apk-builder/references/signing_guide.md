# APK Signing Guide

## Overview

Android requires all APKs to be digitally signed before they can be installed on devices or distributed through app stores. This guide covers the complete APK signing process.

## Signing Methods

### Method 1: Using sign_apk.py Script (Recommended)

The easiest way to sign APKs:

```bash
python3 scripts/sign_apk.py \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk \
  --keystore my-release-key.keystore \
  --alias my-key-alias \
  --output app-release-signed.apk
```

### Method 2: Using apksigner (Manual)

```bash
apksigner sign \
  --ks my-release-key.keystore \
  --ks-key-alias my-key-alias \
  --out app-release-signed.apk \
  app-release-unsigned.apk
```

### Method 3: Using jarsigner (Legacy)

```bash
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore my-release-key.keystore \
  app-release-unsigned.apk \
  my-key-alias
```

## Creating a Keystore

### Generate New Keystore

```bash
keytool -genkey -v \
  -keystore my-release-key.keystore \
  -alias my-key-alias \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000
```

You'll be prompted for:
- **Keystore password**: Choose a strong password
- **Key password**: Can be same as keystore password
- **Name and organization**: Your details
- **Organizational unit**: Optional
- **City, State, Country**: Your location

### Important Notes

- **Keep keystore safe**: Store in secure location with backups
- **Remember passwords**: You cannot recover them if lost
- **Validity**: 10000 days = ~27 years (sufficient for app lifetime)
- **Key size**: 2048 bits minimum for security

### Keystore Information

View keystore details:

```bash
keytool -list -v -keystore my-release-key.keystore
```

## Signing Workflow

### Complete Release Build and Sign Process

```bash
# 1. Build release APK
cordova build android --release

# 2. Sign the APK
python3 scripts/sign_apk.py \
  platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk \
  --keystore my-release-key.keystore \
  --alias my-key-alias \
  --output app-release-signed.apk \
  --zipalign

# 3. Verify signature
apksigner verify -v app-release-signed.apk
```

## APK Optimization

### Zipalign

Zipalign optimizes APK for faster loading and reduced memory usage:

```bash
# Zipalign before signing (recommended)
zipalign -v 4 app-release-unsigned.apk app-release-aligned.apk

# Then sign the aligned APK
apksigner sign --ks my-release-key.keystore \
  --out app-release-signed.apk \
  app-release-aligned.apk
```

**Note**: The sign_apk.py script can do this automatically with `--zipalign` flag.

### Why Zipalign?

- Aligns uncompressed data on 4-byte boundaries
- Reduces RAM consumption when running app
- Required for Google Play Store submission

## Verification

### Verify APK Signature

```bash
# Using apksigner (recommended)
apksigner verify -v app-release-signed.apk

# Using jarsigner (legacy)
jarsigner -verify -verbose -certs app-release-signed.apk
```

### Check APK Information

```bash
# View APK details
aapt dump badging app-release-signed.apk

# View signing certificate
apksigner verify --print-certs app-release-signed.apk
```

## Automated Signing with Cordova

### Configure build.json

Create `build.json` in project root:

```json
{
  "android": {
    "release": {
      "keystore": "my-release-key.keystore",
      "storePassword": "your-keystore-password",
      "alias": "my-key-alias",
      "password": "your-key-password",
      "keystoreType": ""
    }
  }
}
```

**Security Warning**: Don't commit build.json with passwords to version control!

### Build with Automatic Signing

```bash
cordova build android --release --buildConfig=build.json
```

This produces a signed APK directly at:
```
platforms/android/app/build/outputs/apk/release/app-release.apk
```

## Security Best Practices

### Keystore Security

1. **Never commit keystore to version control**
   - Add to .gitignore: `*.keystore`

2. **Store securely**
   - Keep encrypted backups in multiple locations
   - Use password manager for passwords
   - Consider hardware security module (HSM) for enterprise

3. **Limit access**
   - Only authorized personnel should have keystore access
   - Use different keystores for different apps

4. **Password strength**
   - Use strong, unique passwords
   - Minimum 8 characters with mixed case, numbers, symbols

### build.json Security

1. **Never commit with passwords**
   - Add to .gitignore: `build.json`

2. **Use environment variables**
   ```json
   {
     "android": {
       "release": {
         "keystore": "${KEYSTORE_PATH}",
         "storePassword": "${KEYSTORE_PASSWORD}",
         "alias": "${KEY_ALIAS}",
         "password": "${KEY_PASSWORD}"
       }
     }
   }
   ```

3. **CI/CD secrets**
   - Store credentials in CI/CD secret management
   - Never log passwords in build output

## Google Play Store Requirements

### App Signing

Google Play offers two signing options:

1. **App Signing by Google Play** (Recommended)
   - Google manages signing key
   - You upload with upload key
   - More secure and flexible

2. **Traditional signing**
   - You manage signing key
   - Upload signed APK directly

### Upload Key vs Signing Key

- **Upload key**: Used to sign APK you upload to Google Play
- **Signing key**: Used by Google Play to sign APK distributed to users

### Setting Up Google Play App Signing

1. Enroll in Google Play App Signing
2. Generate upload key (separate from signing key)
3. Upload signed APK with upload key
4. Google re-signs with signing key for distribution

## Troubleshooting

### "jarsigner: unable to sign jar"

**Cause**: Incorrect password or keystore path

**Solution**:
- Verify keystore path is correct
- Check password is correct
- Verify alias exists: `keytool -list -keystore my-release-key.keystore`

### "apksigner not found"

**Cause**: Android SDK build-tools not in PATH

**Solution**:
```bash
export PATH=$PATH:$ANDROID_HOME/build-tools/34.0.0
```

### "Verification failed"

**Cause**: APK not properly signed or corrupted

**Solution**:
- Re-sign the APK
- Ensure using correct keystore and alias
- Check APK is not corrupted

### "Key was created with errors"

**Cause**: Issues during keystore generation

**Solution**:
- Delete keystore and regenerate
- Ensure keytool is from correct Java version
- Check file permissions

## Key Rotation

### When to Rotate Keys

- Key compromise suspected
- Upgrading to stronger algorithm
- Organizational changes

### How to Rotate

**Warning**: Cannot change signing key for existing app on Play Store without Google Play App Signing.

With Google Play App Signing:
1. Generate new upload key
2. Contact Google Play support
3. Upload APK signed with new upload key

## Certificate Fingerprints

### Get SHA-1 Fingerprint

```bash
keytool -list -v -keystore my-release-key.keystore -alias my-key-alias
```

### Get SHA-256 Fingerprint

```bash
keytool -list -v -keystore my-release-key.keystore -alias my-key-alias | grep SHA256
```

### Why Fingerprints Matter

- Required for Google Maps API
- Required for Firebase
- Required for Facebook SDK
- Used for app verification

## Quick Reference

### Common Commands

```bash
# Generate keystore
keytool -genkey -v -keystore release.keystore -alias release -keyalg RSA -keysize 2048 -validity 10000

# Sign APK
apksigner sign --ks release.keystore --out signed.apk unsigned.apk

# Verify signature
apksigner verify -v signed.apk

# Zipalign
zipalign -v 4 input.apk output.apk

# View keystore
keytool -list -v -keystore release.keystore

# Get fingerprint
keytool -list -v -keystore release.keystore | grep SHA256
```

### File Locations

- **Unsigned APK**: `platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk`
- **Debug APK**: `platforms/android/app/build/outputs/apk/debug/app-debug.apk`
- **Keystore**: Store outside project directory for security
- **build.json**: Project root (add to .gitignore)

## Additional Resources

- [Android App Signing Documentation](https://developer.android.com/studio/publish/app-signing)
- [Google Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756)
- [Cordova Build Documentation](https://cordova.apache.org/docs/en/latest/guide/platforms/android/)
