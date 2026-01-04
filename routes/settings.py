from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from config.config_manager import load_config, save_config, validate_config
from core.mealie_client import MealieClient
from core.tandoor_client import TandoorClient

settings_bp = Blueprint('settings', __name__)


@settings_bp.route('/')
def settings():
    """Settings page"""
    config = load_config()
    return render_template('settings.html', config=config)


@settings_bp.route('/update', methods=['POST'])
def update_settings():
    """Update configuration settings"""
    config = load_config()

    # Update Mealie settings
    config['mealie']['enabled'] = request.form.get('mealie_enabled') == 'on'
    config['mealie']['url'] = request.form.get('mealie_url', '').strip()
    config['mealie']['api_token'] = request.form.get('mealie_token', '').strip()

    # Update Tandoor settings
    config['tandoor']['enabled'] = request.form.get('tandoor_enabled') == 'on'
    config['tandoor']['url'] = request.form.get('tandoor_url', '').strip()
    config['tandoor']['api_key'] = request.form.get('tandoor_key', '').strip()

    # Update scraper settings
    try:
        config['scraper']['target_recipes_per_site'] = int(request.form.get('target_recipes', 50))
        config['scraper']['scan_depth'] = int(request.form.get('scan_depth', 1000))
    except ValueError:
        flash('Invalid numeric values provided', 'error')
        return redirect(url_for('settings.settings'))

    config['scraper']['dry_run'] = request.form.get('dry_run') == 'on'

    # Validate configuration
    is_valid, errors = validate_config(config)
    if not is_valid:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('settings.settings'))

    # Save configuration
    if save_config(config):
        flash('Settings saved successfully!', 'success')
    else:
        flash('Error saving settings', 'error')

    return redirect(url_for('settings.settings'))


@settings_bp.route('/test-connection/<service>', methods=['POST'])
def test_connection(service):
    """Test API connection for Mealie or Tandoor"""
    config = load_config()

    try:
        if service == 'mealie':
            if not config['mealie']['url'] or not config['mealie']['api_token']:
                return jsonify({
                    "success": False,
                    "message": "Please configure Mealie URL and API token first"
                }), 400

            client = MealieClient(
                config['mealie']['url'],
                config['mealie']['api_token']
            )
            success, message = client.test_connection()

        elif service == 'tandoor':
            if not config['tandoor']['url'] or not config['tandoor']['api_key']:
                return jsonify({
                    "success": False,
                    "message": "Please configure Tandoor URL and API key first"
                }), 400

            client = TandoorClient(
                config['tandoor']['url'],
                config['tandoor']['api_key']
            )
            success, message = client.test_connection()

        else:
            return jsonify({
                "success": False,
                "message": "Invalid service"
            }), 400

        return jsonify({"success": success, "message": message})

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        }), 500
