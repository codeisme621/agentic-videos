#!/usr/bin/env python3
"""
Clean up .excalidraw files from validation-app/public/excalidraw/ after validation.
Usage: python clean_validation_app.py
"""

import os
import sys
from pathlib import Path

def clean_validation_app() -> bool:
    """Remove all .excalidraw files from validation app public folder."""

    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    excalidraw_dir = project_root / "validation-app" / "public" / "excalidraw"

    # Check if directory exists
    if not excalidraw_dir.exists():
        print("✅ Excalidraw directory doesn't exist - nothing to clean")
        return True

    # Find all .excalidraw files
    excalidraw_files = list(excalidraw_dir.glob("*.excalidraw"))

    if not excalidraw_files:
        print("✅ No .excalidraw files found - directory is already clean")
        return True

    # List files to be removed
    print(f"📁 Found {len(excalidraw_files)} .excalidraw file(s) to remove:")
    total_size = 0
    for file in excalidraw_files:
        file_size = file.stat().st_size
        total_size += file_size
        print(f"  - {file.name} ({file_size:,} bytes)")

    print(f"📊 Total size: {total_size:,} bytes")
    print()

    # Confirm deletion
    response = input("🗑️  Remove all .excalidraw files? (y/N): ").lower().strip()
    if response != 'y':
        print("❌ Cleanup cancelled by user")
        return False

    # Remove files
    removed_count = 0
    failed_files = []

    for file in excalidraw_files:
        try:
            file.unlink()
            print(f"✅ Removed: {file.name}")
            removed_count += 1
        except Exception as e:
            print(f"❌ Failed to remove {file.name}: {e}")
            failed_files.append(file.name)

    print()
    if removed_count > 0:
        print(f"✅ Successfully removed {removed_count} file(s)")

    if failed_files:
        print(f"❌ Failed to remove {len(failed_files)} file(s): {', '.join(failed_files)}")
        return False

    # Check if directory is now empty (except for .gitkeep if present)
    remaining_files = [f for f in excalidraw_dir.iterdir() if f.name != '.gitkeep']
    if not remaining_files:
        print("🎉 Excalidraw directory is now clean and ready for next validation")
    else:
        print(f"⚠️  Directory still contains {len(remaining_files)} non-.excalidraw file(s)")

    return True

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h']:
            print("Clean up .excalidraw files from validation app after validation")
            print()
            print("Usage: python clean_validation_app.py")
            print()
            print("This script removes all .excalidraw files from:")
            print("  validation-app/public/excalidraw/")
            print()
            print("Use this after visual validation is complete to ensure")
            print("a clean state for the next skill run.")
            sys.exit(0)
        else:
            print("Error: No arguments expected")
            print("Usage: python clean_validation_app.py")
            print("Use --help for more information")
            sys.exit(1)

    print("🧹 Excalidraw Validation App Cleanup")
    print("=====================================")
    print()

    success = clean_validation_app()

    if success:
        print()
        print("🚀 Next steps:")
        print("1. Validation app is ready for next .excalidraw file")
        print("2. Use: python scripts/copy_to_validation.py <file.excalidraw>")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()