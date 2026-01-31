#!/bin/bash

# Water Tracker App - Build Script
# 喝水打卡应用 - 构建脚本

echo "================================"
echo "Water Tracker App - Build Script"
echo "喝水打卡应用 - 构建脚本"
echo "================================"
echo ""

# Check if Cordova is installed
if ! command -v cordova &> /dev/null; then
    echo "❌ Cordova is not installed. Installing..."
    npm install -g cordova
fi

# Check requirements
echo "📋 Checking requirements..."
cordova requirements

echo ""
echo "Select build option:"
echo "1) Build debug APK (调试版本)"
echo "2) Build release APK (发布版本)"
echo "3) Run on device (在设备上运行)"
echo "4) Run on emulator (在模拟器上运行)"
echo "5) Browser preview (浏览器预览)"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🔨 Building debug APK..."
        cordova build android
        echo "✅ Debug APK built successfully!"
        echo "📦 Location: platforms/android/app/build/outputs/apk/debug/app-debug.apk"
        ;;
    2)
        echo "🔨 Building release APK..."
        cordova build android --release
        echo "✅ Release APK built successfully!"
        echo "📦 Location: platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk"
        echo "⚠️  Note: You need to sign the APK before distribution"
        ;;
    3)
        echo "📱 Running on device..."
        cordova run android
        ;;
    4)
        echo "📱 Running on emulator..."
        cordova emulate android
        ;;
    5)
        echo "🌐 Starting browser preview..."
        echo "Opening http://localhost:8080"
        cd www
        python3 -m http.server 8080
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✨ Done!"
