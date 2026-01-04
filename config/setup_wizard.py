"""Setup wizard for first-run configuration"""
from pathlib import Path
from config.config_manager import load_config, save_config


def is_first_run() -> bool:
    """
    Check if this is the first run (config needs setup)

    Returns:
        True if config needs to be set up, False otherwise
    """
    try:
        config = load_config()

        # Check if Mealie settings are still default/empty
        mealie_url = config.get('mealie', {}).get('url', '')
        mealie_token = config.get('mealie', {}).get('api_token', '')

        # If URL contains placeholder text or token is placeholder/empty, needs setup
        if (not mealie_url or
            'YOUR_MEALIE' in mealie_url or
            not mealie_token or
            'YOUR_MEALIE' in mealie_token or
            mealie_token == ''):
            return True

        return False

    except Exception as e:
        # If config can't be loaded, definitely needs setup
        return True


def save_wizard_config(form_data: dict) -> tuple:
    """
    Save configuration from setup wizard

    Args:
        form_data: Dictionary with form fields

    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Load existing config or create new one
        config = load_config()

        # Update Mealie settings
        mealie_url = form_data.get('mealie_url', '').strip()
        mealie_token = form_data.get('mealie_token', '').strip()

        if not mealie_url or not mealie_token:
            return (False, "Mealie URL and API token are required")

        # Ensure URL has protocol
        if not mealie_url.startswith(('http://', 'https://')):
            mealie_url = f"http://{mealie_url}"

        config['mealie']['enabled'] = True
        config['mealie']['url'] = mealie_url
        config['mealie']['api_token'] = mealie_token

        # Update Tandoor settings if provided
        tandoor_url = form_data.get('tandoor_url', '').strip()
        tandoor_key = form_data.get('tandoor_key', '').strip()

        if tandoor_url and tandoor_key:
            if not tandoor_url.startswith(('http://', 'https://')):
                tandoor_url = f"http://{tandoor_url}"

            config['tandoor']['enabled'] = True
            config['tandoor']['url'] = tandoor_url
            config['tandoor']['api_key'] = tandoor_key
        else:
            config['tandoor']['enabled'] = False

        # Save configuration
        if save_config(config):
            return (True, "Configuration saved successfully!")
        else:
            return (False, "Failed to save configuration file")

    except Exception as e:
        return (False, f"Error saving configuration: {str(e)}")
