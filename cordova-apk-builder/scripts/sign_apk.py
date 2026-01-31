#!/usr/bin/env python3
"""
APK Signing Script
Signs Android APK files with a keystore for release distribution
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(cmd, check=True):
    """Execute a shell command and return the result"""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
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


def check_apk_exists(apk_path):
    """Verify APK file exists"""
    if not apk_path.exists():
        print(f"❌ APK not found: {apk_path}")
        sys.exit(1)
    print(f"✅ Found APK: {apk_path}")


def check_keystore_exists(keystore_path):
    """Verify keystore file exists"""
    if not keystore_path.exists():
        print(f"❌ Keystore not found: {keystore_path}")
        print("\nTo create a keystore, run:")
        print("keytool -genkey -v -keystore my-release-key.keystore \\")
        print("  -alias my-key-alias \\")
        print("  -keyalg RSA -keysize 2048 -validity 10000")
        sys.exit(1)
    print(f"✅ Found keystore: {keystore_path}")


def sign_apk_jarsigner(apk_path, keystore_path, alias, output_path):
    """Sign APK using jarsigner"""
    print("\n🔐 Signing APK with jarsigner...")

    # First, sign the APK
    cmd = f'jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore "{keystore_path}" "{apk_path}" "{alias}"'
    run_command(cmd)

    # Copy to output path if different
    if output_path != apk_path:
        import shutil
        shutil.copy2(apk_path, output_path)
        print(f"✅ Signed APK copied to: {output_path}")

    return output_path


def sign_apk_apksigner(apk_path, keystore_path, alias, output_path):
    """Sign APK using apksigner (recommended)"""
    print("\n🔐 Signing APK with apksigner...")

    cmd = f'apksigner sign --ks "{keystore_path}" --ks-key-alias "{alias}" --out "{output_path}" "{apk_path}"'
    result = run_command(cmd, check=False)

    if result.returncode != 0:
        print("\n⚠️  apksigner not found, falling back to jarsigner")
        return sign_apk_jarsigner(apk_path, keystore_path, alias, output_path)

    print(f"✅ Signed APK created: {output_path}")
    return output_path


def verify_signature(apk_path):
    """Verify APK signature"""
    print("\n🔍 Verifying APK signature...")

    # Try apksigner first
    result = run_command(f'apksigner verify -v "{apk_path}"', check=False)
    if result.returncode == 0:
        print("✅ APK signature verified successfully")
        return True

    # Fall back to jarsigner
    result = run_command(f'jarsigner -verify -verbose -certs "{apk_path}"', check=False)
    if result.returncode == 0:
        print("✅ APK signature verified successfully")
        return True

    print("❌ APK signature verification failed")
    return False


def zipalign_apk(apk_path, output_path):
    """Optimize APK with zipalign"""
    print("\n📦 Optimizing APK with zipalign...")

    cmd = f'zipalign -v 4 "{apk_path}" "{output_path}"'
    result = run_command(cmd, check=False)

    if result.returncode != 0:
        print("⚠️  zipalign not found or failed, skipping optimization")
        return apk_path

    print(f"✅ Optimized APK created: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Sign Android APK for release",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "apk_path",
        help="Path to unsigned APK file"
    )
    parser.add_argument(
        "--keystore",
        required=True,
        help="Path to keystore file"
    )
    parser.add_argument(
        "--alias",
        required=True,
        help="Key alias in keystore"
    )
    parser.add_argument(
        "--output",
        help="Output path for signed APK (default: <apk>-signed.apk)"
    )
    parser.add_argument(
        "--zipalign",
        action="store_true",
        help="Optimize APK with zipalign before signing"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        default=True,
        help="Verify signature after signing (default: True)"
    )

    args = parser.parse_args()

    # Convert to absolute paths
    apk_path = Path(args.apk_path).resolve()
    keystore_path = Path(args.keystore).resolve()

    # Determine output path
    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = apk_path.parent / f"{apk_path.stem}-signed.apk"

    print("=" * 60)
    print("APK Signing Tool")
    print("=" * 60)

    # Verify inputs
    check_apk_exists(apk_path)
    check_keystore_exists(keystore_path)

    # Zipalign if requested
    if args.zipalign:
        aligned_path = apk_path.parent / f"{apk_path.stem}-aligned.apk"
        apk_path = zipalign_apk(apk_path, aligned_path)

    # Sign APK
    signed_apk = sign_apk_apksigner(apk_path, keystore_path, args.alias, output_path)

    # Verify signature
    if args.verify:
        verify_signature(signed_apk)

    # Show file info
    print(f"\n📊 Signed APK size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
    print(f"\n✨ APK signed successfully!")
    print(f"📦 Signed APK: {output_path}")
    print("\nYou can now distribute this APK or upload it to Google Play Store")


if __name__ == "__main__":
    main()
