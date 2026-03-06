import json
import os

def load_lore(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as file:
        lore = json.load(file)
    
    if "title" not in lore:
        raise ValueError("Lore JSON is missing required key: 'title'")
    if "entries" not in lore:
        raise ValueError("Lore JSON is missing required key: 'entries'")
    
    if not isinstance(lore["entries"], list):
        raise ValueError("Lore JSON key 'entries' must be a list")
    if "facts" not in lore or not isinstance(lore["facts"], dict):
        lore["facts"] = {}

    for entry in lore["entries"]:
        if "name" not in entry:
            raise ValueError("Every entry must have a 'name' field")
        if "type" not in entry:
            raise ValueError(f"Entry '{entry.get('name', 'UNKNOWN')}' is missing 'type'")
        if "aliases" not in entry:
            entry["aliases"] = []
        if "faction" not in entry:
            entry["faction"] = []
        if "description" not in entry:
            entry["description"] = []
        if "race" not in entry:
            entry["race"] = []
        if "created_by" not in entry:
            entry["created_by"] = []
        if "weapons" not in entry:
            entry["weapons"] = []
        if "mounts" not in entry:
            entry["mounts"] = []
        if "companions" not in entry:
            entry["companions"] = []
        if "catchphrase" not in entry:
            entry["catchphrase"] = None
        if "helped_by" not in entry:
            entry["helped_by"] = []
        if "escaped_from" not in entry:
            entry["escaped_from"] = []
    return lore