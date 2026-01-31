#!/usr/bin/env python3
"""
Cordova APK Builder Script
Automates building debug and release APKs for Cordova applications
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(cmd, cwd=None, check=True):
    """Execute a shell command and return the result"""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    if check and result.returncode != 0:
        print(f"❌ Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    return result


def check_cordova_project(project_dir):
    """Verify this is a valid Cordova project"""
    config_xml = project_dir / "config.xml"
    if not config_xml.exists():
        print(f"❌ Not a Cordova project: config.xml not found in {project_dir}")
        sys.exit(1)
    print(f"✅ Found Cordova project at {project_dir}")


def check_cordova_installed():
    """Check if Cordova CLI is installed"""
    result = run_command("cordova --version", check=False)
    if result.returncode != 0:
        print("❌ Cordova CLI not installed")
        print("Install with: npm install -g cordova")
        sys.exit(1)
    print(f"✅ Cordova CLI installed: {result.stdout.strip()}")


def check_requirements(project_dir):
    """Check Android build requirements"""
    print("\n📋 Checking build requirements...")
    result = run_command("cordova requirements", cwd=project_dir, check=False)
    return result.returncode == 0


def clean_build(project_dir):
    """Clean previous build artifacts"""
    print("\n🧹 Cleaning previous build...")
    run_command("cordova clean android", cwd=project_dir)


def build_debug_apk(project_dir):
    """Build debug APK"""
    print("\n🔨 Building debug APK...")
    run_command("cordova build android --debug", cwd=project_dir)

    apk_path = project_dir / "platforms/android/app/build/outputs/apk/debug/app-debug.apk"
    if apk_path.exists():
        print(f"\n✅ Debug APK built successfully!")
        print(f"📦 Location: {apk_path}")
        print(f"📊 Size: {apk_path.stat().st_size / 1024 / 1024:.2f} MB")
        return str(apk_path)
    else:
        print("❌ Debug APK not found at expected location")
        sys.exit(1)


def build_release_apk(project_dir):
    """Build release APK (unsigned)"""
    print("\n🔨 Building release APK...")
    run_command("cordova build android --release", cwd=project_dir)

    apk_path = project_dir / "platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk"
    if apk_path.exists():
        print(f"\n✅ Release APK built successfully!")
        print(f"📦 Location: {apk_path}")
        print(f"📊 Size: {apk_path.stat().st_size / 1024 / 1024:.2f} MB")
        print("\n⚠️  Note: This APK is unsigned and needs to be signed before distribution")
        print("Use sign_apk.py to sign the APK")
        return str(apk_path)
    else:
        print("❌ Release APK not found at expected location")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Build Cordova Android APK",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "project_dir",
        nargs="?",
        default=".",
        help="Path to Cordova project directory (default: current directory)"
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="Build release APK instead of debug"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean build artifacts before building"
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip environment requirement checks"
    )

    args = parser.parse_args()

    # Convert to absolute path
    project_dir = Path(args.project_dir).resolve()

    print("=" * 60)
    print("Cordova APK Builder")
    print("=" * 60)

    # Verify Cordova project
    check_cordova_project(project_dir)

    # Check Cordova CLI
    check_cordova_installed()

    # Check requirements
    if not args.skip_checks:
        if not check_requirements(project_dir):
            print("\n⚠️  Some requirements are not met")
            print("You can continue with --skip-checks, but build may fail")
            sys.exit(1)

    # Clean if requested
    if args.clean:
        clean_build(project_dir)

    # Build APK
    if args.release:
        apk_path = build_release_apk(project_dir)
    else:
        apk_path = build_debug_apk(project_dir)

    print("\n✨ Build complete!")
    print(f"APK: {apk_path}")


if __name__ == "__main__":
    main()
