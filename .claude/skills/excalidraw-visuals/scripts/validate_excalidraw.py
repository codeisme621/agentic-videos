#!/usr/bin/env python3
"""
Validate Excalidraw JSON files for structural correctness.
Usage: python validate_excalidraw.py <file.excalidraw>
"""

import json
import sys
from pathlib import Path

REQUIRED_TOP_LEVEL = ["type", "version", "elements", "appState"]
VALID_ELEMENT_TYPES = ["rectangle", "ellipse", "arrow", "text", "line", "freedraw", "diamond", "image", "frame"]
REQUIRED_ELEMENT_FIELDS = ["id", "type", "x", "y"]

def validate_element(element: dict, index: int) -> list[str]:
    """Validate a single element, return list of errors."""
    errors = []
    
    # Check required fields
    for field in REQUIRED_ELEMENT_FIELDS:
        if field not in element:
            errors.append(f"Element {index}: missing required field '{field}'")
    
    # Check element type
    if "type" in element and element["type"] not in VALID_ELEMENT_TYPES:
        errors.append(f"Element {index}: invalid type '{element['type']}'")
    
    # Check ID is string
    if "id" in element and not isinstance(element["id"], str):
        errors.append(f"Element {index}: 'id' must be a string")
    
    # Check coordinates are numbers
    for coord in ["x", "y"]:
        if coord in element and not isinstance(element[coord], (int, float)):
            errors.append(f"Element {index}: '{coord}' must be a number")
    
    # Check dimensions for applicable types
    if element.get("type") in ["rectangle", "ellipse", "diamond", "text"]:
        for dim in ["width", "height"]:
            if dim in element and not isinstance(element[dim], (int, float)):
                errors.append(f"Element {index}: '{dim}' must be a number")
    
    # Check arrow points
    if element.get("type") == "arrow":
        if "points" not in element:
            errors.append(f"Element {index}: arrow missing 'points'")
        elif not isinstance(element["points"], list):
            errors.append(f"Element {index}: 'points' must be an array")
        elif len(element["points"]) < 2:
            errors.append(f"Element {index}: arrow needs at least 2 points")
    
    return errors

def validate_file(filepath: str) -> tuple[bool, list[str]]:
    """Validate an Excalidraw file, return (is_valid, errors)."""
    errors = []
    
    # Check file exists
    path = Path(filepath)
    if not path.exists():
        return False, [f"File not found: {filepath}"]
    
    # Parse JSON
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    
    # Check top-level structure
    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
    
    # Check type
    if data.get("type") != "excalidraw":
        errors.append(f"'type' must be 'excalidraw', got '{data.get('type')}'")
    
    # Check version
    if "version" in data and not isinstance(data["version"], int):
        errors.append("'version' must be an integer")
    
    # Check elements array
    if "elements" in data:
        if not isinstance(data["elements"], list):
            errors.append("'elements' must be an array")
        else:
            # Validate each element
            for i, element in enumerate(data["elements"]):
                if not isinstance(element, dict):
                    errors.append(f"Element {i}: must be an object")
                else:
                    errors.extend(validate_element(element, i))
            
            # Check for duplicate IDs
            ids = [e.get("id") for e in data["elements"] if "id" in e]
            seen = set()
            for id in ids:
                if id in seen:
                    errors.append(f"Duplicate element ID: '{id}'")
                seen.add(id)
    
    # Check appState
    if "appState" in data and not isinstance(data["appState"], dict):
        errors.append("'appState' must be an object")
    
    return len(errors) == 0, errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_excalidraw.py <file.excalidraw>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)
    
    if is_valid:
        print("OK - Valid Excalidraw file")
        sys.exit(0)
    else:
        print("ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
