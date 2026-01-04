from flask import Blueprint, render_template, request, redirect, url_for, flash
from config.setup_wizard import is_first_run, save_wizard_config
from core.mealie_client import MealieClient
from core.tandoor_client import TandoorClient

setup_bp = Blueprint('setup', __name__)


@setup_bp.route('/setup', methods=['GET'])
def setup_wizard():
    """Display the setup wizard"""
    return render_template('setup_wizard.html')


@setup_bp.route('/setup/save', methods=['POST'])
def save_setup():
    """Save setup wizard configuration"""
    form_data = {
        'mealie_url': request.form.get('mealie_url', '').strip(),
        'mealie_token': request.form.get('mealie_token', '').strip(),
        'tandoor_url': request.form.get('tandoor_url', '').strip(),
        'tandoor_key': request.form.get('tandoor_key', '').strip(),
    }

    # Save configuration
    success, message = save_wizard_config(form_data)

    if success:
        flash(message, 'success')
        return redirect(url_for('main.dashboard'))
    else:
        flash(message, 'error')
        return redirect(url_for('setup.setup_wizard'))


@setup_bp.route('/setup/test-mealie', methods=['POST'])
def test_mealie_setup():
    """Test Mealie connection during setup"""
    data = request.get_json()
    mealie_url = data.get('url', '').strip()
    mealie_token = data.get('token', '').strip()

    if not mealie_url or not mealie_token:
        return {'success': False, 'message': 'URL and token are required'}, 400

    # Ensure URL has protocol
    if not mealie_url.startswith(('http://', 'https://')):
        mealie_url = f"http://{mealie_url}"

    try:
        client = MealieClient(mealie_url, mealie_token)
        success, message = client.test_connection()
        return {'success': success, 'message': message}
    except Exception as e:
        return {'success': False, 'message': f"Error: {str(e)}"}, 500


@setup_bp.route('/setup/test-tandoor', methods=['POST'])
def test_tandoor_setup():
    """Test Tandoor connection during setup"""
    data = request.get_json()
    tandoor_url = data.get('url', '').strip()
    tandoor_key = data.get('token', '').strip()

    if not tandoor_url or not tandoor_key:
        return {'success': False, 'message': 'URL and key are required'}, 400

    # Ensure URL has protocol
    if not tandoor_url.startswith(('http://', 'https://')):
        tandoor_url = f"http://{tandoor_url}"

    try:
        client = TandoorClient(tandoor_url, tandoor_key)
        success, message = client.test_connection()
        return {'success': success, 'message': message}
    except Exception as e:
        return {'success': False, 'message': f"Error: {str(e)}"}, 500
