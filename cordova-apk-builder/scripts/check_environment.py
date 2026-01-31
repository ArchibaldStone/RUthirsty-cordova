#!/usr/bin/env python3
"""
Environment Check Script
Verifies that all required tools for Cordova Android builds are installed
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd, check=False):
    """Execute a shell command and return the result"""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    return result


def check_command_exists(command):
    """Check if a command exists in PATH"""
    return shutil.which(command) is not None


def check_node():
    """Check Node.js installation"""
    print("\n📦 Checking Node.js...")
    if not check_command_exists("node"):
        print("❌ Node.js not installed")
        print("   Install from: https://nodejs.org/")
        return False

    result = run_command("node --version")
    version = result.stdout.strip()
    print(f"✅ Node.js installed: {version}")
    return True


def check_npm():
    """Check npm installation"""
    print("\n📦 Checking npm...")
    if not check_command_exists("npm"):
        print("❌ npm not installed")
        return False

    result = run_command("npm --version")
    version = result.stdout.strip()
    print(f"✅ npm installed: {version}")
    return True


def check_cordova():
    """Check Cordova CLI installation"""
    print("\n📱 Checking Cordova CLI...")
    if not check_command_exists("cordova"):
        print("❌ Cordova CLI not installed")
        print("   Install with: npm install -g cordova")
        return False

    result = run_command("cordova --version")
    version = result.stdout.strip()
    print(f"✅ Cordova CLI installed: {version}")
    return True


def check_java():
    """Check Java JDK installation"""
    print("\n☕ Checking Java JDK...")
    if not check_command_exists("java"):
        print("❌ Java not installed")
        print("   Install JDK 11 or JDK 17")
        return False

    result = run_command("java -version")
    version_info = result.stderr.strip().split('\n')[0] if result.stderr else result.stdout.strip()
    print(f"✅ Java installed: {version_info}")

    # Check JAVA_HOME
    java_home = os.environ.get("JAVA_HOME")
    if java_home:
        print(f"✅ JAVA_HOME set: {java_home}")
    else:
        print("⚠️  JAVA_HOME not set (may cause issues)")

    return True


def check_android_sdk():
    """Check Android SDK installation"""
    print("\n🤖 Checking Android SDK...")

    android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
    if not android_home:
        print("❌ ANDROID_HOME not set")
        print("   Set environment variable to Android SDK location")
        print("   Example: export ANDROID_HOME=$HOME/Android/Sdk")
        return False

    print(f"✅ ANDROID_HOME set: {android_home}")

    # Check if SDK directory exists
    sdk_path = Path(android_home)
    if not sdk_path.exists():
        print(f"❌ Android SDK directory not found: {android_home}")
        return False

    print(f"✅ Android SDK directory exists")

    # Check for platform-tools
    if check_command_exists("adb"):
        result = run_command("adb --version")
        version = result.stdout.strip().split('\n')[0]
        print(f"✅ ADB installed: {version}")
    else:
        print("⚠️  ADB not found in PATH")

    return True


def check_gradle():
    """Check Gradle installation"""
    print("\n🔧 Checking Gradle...")
    if not check_command_exists("gradle"):
        print("⚠️  Gradle not in PATH (Cordova will use wrapper)")
        return True

    result = run_command("gradle --version")
    version_line = [line for line in result.stdout.split('\n') if 'Gradle' in line][0]
    print(f"✅ Gradle installed: {version_line}")
    return True


def check_cordova_requirements(project_dir=None):
    """Run Cordova requirements check"""
    print("\n🔍 Running Cordova requirements check...")

    if project_dir and Path(project_dir).exists():
        result = run_command(f"cd {project_dir} && cordova requirements")
    else:
        result = run_command("cordova requirements")

    if result.returncode == 0:
        print(result.stdout)
        print("✅ All Cordova requirements met")
        return True
    else:
        print(result.stdout)
        print(result.stderr)
        print("❌ Some Cordova requirements not met")
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Check Cordova Android build environment"
    )
    parser.add_argument(
        "--project-dir",
        help="Cordova project directory (for requirements check)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Cordova Android Build Environment Check")
    print("=" * 60)

    checks = {
        "Node.js": check_node(),
        "npm": check_npm(),
        "Cordova CLI": check_cordova(),
        "Java JDK": check_java(),
        "Android SDK": check_android_sdk(),
        "Gradle": check_gradle(),
    }

    # Run Cordova requirements if in a project
    if args.project_dir:
        checks["Cordova Requirements"] = check_cordova_requirements(args.project_dir)

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    all_passed = True
    for name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {name}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\n✅ Environment is ready for Cordova Android builds!")
        sys.exit(0)
    else:
        print("\n❌ Some requirements are missing. Please install them and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
