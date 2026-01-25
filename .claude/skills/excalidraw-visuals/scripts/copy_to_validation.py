#!/usr/bin/env python3
"""
Copy Excalidraw files from output/ to validation-app/public/excalidraw/ for validation.
Usage: python copy_to_validation.py <file.excalidraw>
"""

import shutil
import sys
from pathlib import Path

def copy_to_validation(filename: str) -> bool:
    """Copy excalidraw file to validation app public folder."""

    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    source_file = project_root / "output" / filename
    validation_dir = project_root / "validation-app" / "public" / "excalidraw"
    dest_file = validation_dir / filename

    # Check source file exists
    if not source_file.exists():
        print(f"❌ Source file not found: {source_file}")
        print(f"Available files in output/:")
        output_dir = project_root / "output"
        if output_dir.exists():
            excalidraw_files = list(output_dir.glob("*.excalidraw"))
            if excalidraw_files:
                for file in excalidraw_files:
                    print(f"  - {file.name}")
            else:
                print("  (no .excalidraw files found)")
        return False

    # Check source file has correct extension
    if not filename.endswith('.excalidraw'):
        print(f"❌ File must have .excalidraw extension: {filename}")
        return False

    # Create destination directory if needed
    validation_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created/verified directory: {validation_dir}")

    # Check if destination file already exists
    if dest_file.exists():
        print(f"⚠️  Destination file already exists: {dest_file}")
        response = input("Overwrite? (y/N): ").lower().strip()
        if response != 'y':
            print("❌ Copy cancelled by user")
            return False

    # Copy file
    try:
        shutil.copy2(source_file, dest_file)
        print(f"✅ Successfully copied:")
        print(f"   From: {source_file}")
        print(f"   To:   {dest_file}")
        print(f"   Size: {dest_file.stat().st_size} bytes")

        # Verify the copy
        if dest_file.exists() and dest_file.stat().st_size > 0:
            print(f"✅ Copy verification successful")
            print(f"💡 File ready for validation at: http://localhost:3000")
            return True
        else:
            print(f"❌ Copy verification failed")
            return False

    except Exception as e:
        print(f"❌ Error copying file: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python copy_to_validation.py <file.excalidraw>")
        print("Example: python copy_to_validation.py ContextEngineering.excalidraw")
        sys.exit(1)

    filename = sys.argv[1]
    success = copy_to_validation(filename)

    if success:
        print()
        print("🚀 Next steps:")
        print("1. Ensure validation app is running: cd validation-app && pnpm dev")
        print("2. Open browser to: http://localhost:3000")
        print("3. After validation, clean up: python scripts/clean_validation_app.py")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()