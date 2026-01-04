from flask import Blueprint, request, jsonify, current_app
import threading
from core.scraper import RecipeScraper
from config.config_manager import load_config, load_site_list, save_config, get_site_lists

scraper_bp = Blueprint('scraper', __name__)


@scraper_bp.route('/start', methods=['POST'])
def start_scraper():
    """Start the scraping process"""
    # Check if scraper is already running
    scraper_thread = current_app.get_scraper_thread()
    if scraper_thread and scraper_thread.is_alive():
        return jsonify({
            "success": False,
            "message": "Scraper is already running"
        }), 400

    try:
        # Load configuration and site list
        config = load_config()
        site_list_file = config.get('active_site_list', 'sites.txt')
        site_list = load_site_list(site_list_file)

        if not site_list:
            return jsonify({
                "success": False,
                "message": f"No sites found in {site_list_file}"
            }), 400

        # Check if at least one service is enabled
        if not config['mealie']['enabled'] and not config['tandoor']['enabled']:
            return jsonify({
                "success": False,
                "message": "Please enable at least one service (Mealie or Tandoor) in settings"
            }), 400

        # Create scraper instance
        scraper_instance = RecipeScraper(config, site_list)
        current_app.set_scraper_instance(scraper_instance)

        # Start scraper in background thread
        thread = threading.Thread(target=scraper_instance.run_scrape, daemon=True)
        thread.start()
        current_app.set_scraper_thread(thread)

        return jsonify({
            "success": True,
            "message": "Scraper started successfully"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error starting scraper: {str(e)}"
        }), 500


@scraper_bp.route('/stop', methods=['POST'])
def stop_scraper():
    """Stop the scraping process"""
    scraper_instance = current_app.get_scraper_instance()

    if not scraper_instance or not scraper_instance.running:
        return jsonify({
            "success": False,
            "message": "Scraper is not running"
        }), 400

    try:
        scraper_instance.stop()
        return jsonify({
            "success": True,
            "message": "Scraper stopping..."
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error stopping scraper: {str(e)}"
        }), 500


@scraper_bp.route('/status', methods=['GET'])
def scraper_status():
    """Get current scraper status"""
    scraper_instance = current_app.get_scraper_instance()

    if not scraper_instance:
        return jsonify({
            "running": False,
            "progress": 0,
            "current_site": "",
            "total_imported": 0,
            "sites_completed": 0,
            "sites_total": 0
        })

    return jsonify(scraper_instance.get_status())


@scraper_bp.route('/site-lists', methods=['GET'])
def get_available_site_lists():
    """Get available site list files"""
    site_lists = get_site_lists()
    config = load_config()

    return jsonify({
        "site_lists": site_lists,
        "active": config.get('active_site_list', 'sites.txt')
    })


@scraper_bp.route('/site-lists/<filename>', methods=['GET'])
def get_site_list(filename):
    """Get contents of a specific site list"""
    try:
        sites = load_site_list(filename)
        return jsonify({
            "filename": filename,
            "sites": sites,
            "count": len(sites)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error loading site list: {str(e)}"
        }), 500


@scraper_bp.route('/site-lists/active', methods=['POST'])
def set_active_site_list():
    """Set the active site list"""
    try:
        data = request.get_json()
        filename = data.get('filename')

        if not filename:
            return jsonify({
                "success": False,
                "message": "Filename is required"
            }), 400

        # Verify file exists
        available_lists = get_site_lists()
        if filename not in available_lists:
            return jsonify({
                "success": False,
                "message": f"Site list '{filename}' not found"
            }), 404

        # Update config
        config = load_config()
        config['active_site_list'] = filename

        if save_config(config):
            return jsonify({
                "success": True,
                "message": f"Active site list set to {filename}"
            })
        else:
            return jsonify({
                "success": False,
                "message": "Error saving configuration"
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        }), 500
