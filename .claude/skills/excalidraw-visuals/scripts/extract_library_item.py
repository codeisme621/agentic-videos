#!/usr/bin/env python3
"""
Extract a specific item from an Excalidraw library by name.

Usage:
    python3 extract_library_item.py <library_path> <item_name>
    python3 extract_library_item.py <library_path> --list

Examples:
    python3 extract_library_item.py libraries/aws-architecture-icons.excalidrawlib "S3"
    python3 extract_library_item.py libraries/icons.excalidrawlib --list
"""

import json
import sys
import os


def load_library(library_path: str) -> dict:
    """Load an Excalidraw library file."""
    with open(library_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def list_items(library: dict) -> list[str]:
    """Get all item names from a library."""
    names = []
    for item in library.get('libraryItems', []):
        name = item.get('name', '')
        if name:
            names.append(name)
    return sorted(names, key=str.lower)


def find_item(library: dict, item_name: str) -> dict | None:
    """Find an item by name (case-insensitive)."""
    item_name_lower = item_name.lower()
    for item in library.get('libraryItems', []):
        if item.get('name', '').lower() == item_name_lower:
            return item
    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    library_path = sys.argv[1]

    if not os.path.exists(library_path):
        print(f"Error: Library file not found: {library_path}", file=sys.stderr)
        sys.exit(1)

    try:
        library = load_library(library_path)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in library file: {e}", file=sys.stderr)
        sys.exit(1)

    # Check library version
    if library.get('version') != 2:
        print(f"Error: Library is version {library.get('version')}, expected version 2", file=sys.stderr)
        sys.exit(1)

    if sys.argv[2] == '--list':
        # List all item names
        names = list_items(library)
        if names:
            for name in names:
                print(name)
        else:
            print("No named items found in library.", file=sys.stderr)
            sys.exit(1)
    else:
        # Find and extract specific item
        item_name = sys.argv[2]
        item = find_item(library, item_name)

        if item is None:
            print(f"Error: Item '{item_name}' not found in library.", file=sys.stderr)
            print("\nAvailable items:", file=sys.stderr)
            for name in list_items(library)[:10]:
                print(f"  - {name}", file=sys.stderr)
            if len(list_items(library)) > 10:
                print(f"  ... and {len(list_items(library)) - 10} more (use --list to see all)", file=sys.stderr)
            sys.exit(1)

        # Output just the elements array as JSON
        output = {
            "name": item.get('name'),
            "elements": item.get('elements', [])
        }
        print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
