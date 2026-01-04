from flask import Blueprint, render_template, current_app
from config.config_manager import load_config, get_site_lists
from pathlib import Path

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def dashboard():
    """Main dashboard showing current configuration and status"""
    config = load_config()
    site_lists = get_site_lists()

    # Get scraper status
    scraper_instance = current_app.get_scraper_instance()
    if scraper_instance:
        scraper_status = scraper_instance.get_status()
    else:
        scraper_status = {
            "running": False,
            "progress": 0,
            "current_site": "",
            "total_imported": 0,
            "sites_completed": 0,
            "sites_total": 0
        }

    return render_template(
        'dashboard.html',
        config=config,
        site_lists=site_lists,
        scraper_status=scraper_status
    )


@main_bp.route('/logs')
def logs():
    """Display scraper logs"""
    log_file = Path(__file__).parent.parent / 'logs' / 'scraper.log'

    log_lines = []
    if log_file.exists():
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                # Read last 500 lines
                all_lines = f.readlines()
                log_lines = all_lines[-500:]
        except Exception as e:
            log_lines = [f"Error reading log file: {e}"]
    else:
        log_lines = ["No logs yet. Start the scraper to generate logs."]

    return render_template('logs.html', log_lines=log_lines)
