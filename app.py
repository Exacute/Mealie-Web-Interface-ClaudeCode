from flask import Flask
import logging
import secrets
import os
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)

# Generate secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

# Configure logging
log_dir = Path(__file__).parent / 'logs'
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'scraper.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Global scraper state
scraper_thread = None
scraper_instance = None

def get_scraper_instance():
    """Get the global scraper instance"""
    global scraper_instance
    return scraper_instance

def set_scraper_instance(instance):
    """Set the global scraper instance"""
    global scraper_instance
    scraper_instance = instance

def get_scraper_thread():
    """Get the global scraper thread"""
    global scraper_thread
    return scraper_thread

def set_scraper_thread(thread):
    """Set the global scraper thread"""
    global scraper_thread
    scraper_thread = thread

# Make these available to blueprints
app.get_scraper_instance = get_scraper_instance
app.set_scraper_instance = set_scraper_instance
app.get_scraper_thread = get_scraper_thread
app.set_scraper_thread = set_scraper_thread

# Register blueprints
from routes.main import main_bp
from routes.settings import settings_bp
from routes.scraper_control import scraper_bp
from routes.setup import setup_bp

app.register_blueprint(main_bp)
app.register_blueprint(settings_bp, url_prefix='/settings')
app.register_blueprint(scraper_bp, url_prefix='/scraper')
app.register_blueprint(setup_bp)

if __name__ == '__main__':
    print("=" * 60)
    print("Mealie Recipe Dredger - Web Interface")
    print("=" * 60)
    print()
    print("Starting Flask server...")
    print("Access the web interface at: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    print()

    app.run(host='0.0.0.0', port=5000, debug=True)
