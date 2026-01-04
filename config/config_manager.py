import json
import os
from pathlib import Path
from typing import List, Tuple, Dict

# Base directory
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CONFIG_FILE = DATA_DIR / "config.json"


def create_default_config() -> dict:
    """Generate default configuration"""
    return {
        "mealie": {
            "enabled": True,
            "url": "http://YOUR_MEALIE_IP:9000",
            "api_token": "YOUR_MEALIE_API_TOKEN_HERE"
        },
        "tandoor": {
            "enabled": False,
            "url": "http://YOUR_TANDOOR_IP:8080",
            "api_key": "YOUR_TANDOOR_API_KEY_HERE"
        },
        "scraper": {
            "dry_run": False,
            "target_recipes_per_site": 50,
            "scan_depth": 1000,
            "delay_between_imports": 1.5
        },
        "active_site_list": "sites.txt"
    }


def load_config() -> dict:
    """Load configuration from config.json with error handling"""
    try:
        if not CONFIG_FILE.exists():
            print(f"Config file not found, creating default at {CONFIG_FILE}")
            config = create_default_config()
            save_config(config)
            return config

        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Ensure all required keys exist (merge with defaults)
        default_config = create_default_config()
        for key in default_config:
            if key not in config:
                config[key] = default_config[key]
            elif isinstance(default_config[key], dict):
                for subkey in default_config[key]:
                    if subkey not in config[key]:
                        config[key][subkey] = default_config[key][subkey]

        return config
    except json.JSONDecodeError as e:
        print(f"Error parsing config file: {e}")
        return create_default_config()
    except Exception as e:
        print(f"Error loading config: {e}")
        return create_default_config()


def save_config(config: dict) -> bool:
    """Save configuration to config.json with validation"""
    try:
        # Ensure data directory exists
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        # Validate before saving
        is_valid, errors = validate_config(config)
        if not is_valid:
            print(f"Config validation errors: {errors}")
            return False

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False


def validate_config(config: dict) -> Tuple[bool, List[str]]:
    """Validate configuration, returns (is_valid, error_list)"""
    errors = []

    # Check required top-level keys
    required_keys = ['mealie', 'tandoor', 'scraper', 'active_site_list']
    for key in required_keys:
        if key not in config:
            errors.append(f"Missing required key: {key}")

    if 'mealie' in config:
        mealie_keys = ['enabled', 'url', 'api_token']
        for key in mealie_keys:
            if key not in config['mealie']:
                errors.append(f"Missing mealie.{key}")

        # Validate URL format if enabled
        if config['mealie'].get('enabled') and config['mealie'].get('url'):
            url = config['mealie']['url']
            if not url.startswith(('http://', 'https://')):
                errors.append("Mealie URL must start with http:// or https://")

    if 'tandoor' in config:
        tandoor_keys = ['enabled', 'url', 'api_key']
        for key in tandoor_keys:
            if key not in config['tandoor']:
                errors.append(f"Missing tandoor.{key}")

        # Validate URL format if enabled
        if config['tandoor'].get('enabled') and config['tandoor'].get('url'):
            url = config['tandoor']['url']
            if not url.startswith(('http://', 'https://')):
                errors.append("Tandoor URL must start with http:// or https://")

    if 'scraper' in config:
        scraper_keys = ['dry_run', 'target_recipes_per_site', 'scan_depth', 'delay_between_imports']
        for key in scraper_keys:
            if key not in config['scraper']:
                errors.append(f"Missing scraper.{key}")

        # Validate numeric values
        if 'target_recipes_per_site' in config['scraper']:
            val = config['scraper']['target_recipes_per_site']
            if not isinstance(val, int) or val < 1 or val > 1000:
                errors.append("target_recipes_per_site must be between 1 and 1000")

        if 'scan_depth' in config['scraper']:
            val = config['scraper']['scan_depth']
            if not isinstance(val, int) or val < 100 or val > 5000:
                errors.append("scan_depth must be between 100 and 5000")

    return (len(errors) == 0, errors)


def get_site_lists() -> List[str]:
    """List all .txt files in data/ directory"""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        txt_files = [f.name for f in DATA_DIR.glob("*.txt")]
        return sorted(txt_files)
    except Exception as e:
        print(f"Error listing site lists: {e}")
        return []


def load_site_list(filename: str) -> List[str]:
    """
    Parse text file and return list of valid URLs
    - Skip empty lines
    - Skip lines starting with #
    - Validate URLs (must start with http:// or https://)
    """
    try:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            print(f"Site list file not found: {filename}")
            return []

        sites = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Strip whitespace
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Skip comments
                if line.startswith('#'):
                    continue

                # Validate URL format
                if line.startswith(('http://', 'https://')):
                    sites.append(line)
                else:
                    print(f"Warning: Invalid URL on line {line_num} in {filename}: {line}")

        return sites
    except Exception as e:
        print(f"Error loading site list {filename}: {e}")
        return []


def save_site_list(filename: str, sites: List[str]) -> bool:
    """Write URLs to text file"""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        file_path = DATA_DIR / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            for site in sites:
                # Validate URL before writing
                if site.startswith(('http://', 'https://')):
                    f.write(f"{site}\n")

        return True
    except Exception as e:
        print(f"Error saving site list {filename}: {e}")
        return False


def get_config_path() -> Path:
    """Return path to config file"""
    return CONFIG_FILE


def get_data_dir() -> Path:
    """Return path to data directory"""
    return DATA_DIR
