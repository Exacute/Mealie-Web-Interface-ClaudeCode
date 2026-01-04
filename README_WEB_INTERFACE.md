# Mealie Recipe Dredger - Web Interface

A simple Flask web interface for the Mealie Recipe Dredger, allowing you to control and configure the scraper through your browser.

## Features

- **Web-Based Configuration**: Enable/disable Mealie and Tandoor from the UI
- **Multiple Site Lists**: Easily switch between different recipe site lists (e.g., Italian, Asian, etc.)
- **Real-Time Progress**: Monitor scraping progress with live updates
- **Start/Stop Controls**: Control the scraper from the dashboard
- **Connection Testing**: Test your Mealie/Tandoor connections before scraping
- **Log Viewer**: View scraper logs directly in the browser

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Migrate Your Configuration (First Time Only)

If you have an existing `mealie_dredger.py` with hardcoded settings:

```bash
python migrate.py
```

This will:
- Extract your config into `data/config.json`
- Extract your site list into `data/sites.txt`
- Create category-based site lists (optional)

### 3. Start the Web Server

```bash
python app.py
```

The web interface will be available at: **http://localhost:5000**

## File Structure

```
mealie-recipe-dredger/
├── app.py                      # Flask application
├── config/
│   ├── config_manager.py       # Configuration management
├── core/
│   ├── scraper.py              # Scraping logic
│   ├── mealie_client.py        # Mealie API client
│   └── tandoor_client.py       # Tandoor API client
├── routes/
│   ├── main.py                 # Dashboard and logs
│   ├── settings.py             # Settings management
│   └── scraper_control.py      # Scraper controls
├── templates/                  # HTML templates
├── static/                     # CSS and JavaScript
├── data/
│   ├── config.json             # Your configuration
│   ├── sites.txt               # Default site list
│   └── sites_*.txt             # Optional category lists
└── logs/
    └── scraper.log             # Scraper logs
```

## Configuration

### config.json

Located in `data/config.json`:

```json
{
  "mealie": {
    "enabled": true,
    "url": "http://192.168.1.79:9000",
    "api_token": "your-token-here"
  },
  "tandoor": {
    "enabled": false,
    "url": "http://YOUR_TANDOOR_IP:8080",
    "api_key": "your-key-here"
  },
  "scraper": {
    "dry_run": false,
    "target_recipes_per_site": 50,
    "scan_depth": 1000,
    "delay_between_imports": 1.5
  },
  "active_site_list": "sites.txt"
}
```

### Site Lists (data/sites.txt)

Plain text file format:
- One URL per line
- Lines starting with `#` are comments/categories
- Blank lines are ignored

Example:

```
# ITALIAN CUISINE
https://www.example-italian.com
https://www.another-italian-site.com

# ASIAN CUISINE
https://www.example-asian.com
```

## Creating Multiple Site Lists

You can create multiple site list files for different cuisines or categories:

1. Create a new file in the `data/` directory (e.g., `data/sites_italian.txt`)
2. Add URLs following the same format as `sites.txt`
3. Select it from the Dashboard's "Site Lists" section

## Using the Web Interface

### Dashboard

- View scraper status and progress in real-time
- Start/stop the scraper
- Switch between different site lists
- See current configuration summary

### Settings

- Enable/disable Mealie and Tandoor
- Configure API URLs and tokens
- Adjust scraper settings (target recipes, scan depth, dry run mode)
- Test your API connections

### Logs

- View scraper logs in real-time
- Automatically refreshes when scraper is running

## API Tokens

### Mealie

1. Log into your Mealie instance
2. Go to **User Profile → Manage API Tokens**
3. Create a new token
4. Copy and paste into the web interface

### Tandoor

1. Log into your Tandoor instance
2. Go to **Settings → API Tokens**
3. Create a new token
4. Copy and paste into the web interface

## Tips

- **Dry Run Mode**: Enable this in settings to test the scraper without actually importing recipes
- **Test Connections**: Always test your Mealie/Tandoor connections before starting a scrape
- **Multiple Lists**: Organize your sites into category-based lists for easier management
- **Monitor Progress**: The dashboard auto-refreshes every 2 seconds while scraping

## Troubleshooting

### Port Already in Use

If port 5000 is in use, edit `app.py` and change:

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

To:

```python
app.run(host='0.0.0.0', port=8080, debug=True)  # or any other port
```

### Can't Connect to Mealie/Tandoor

1. Make sure the URLs are correct (include http:// or https://)
2. Test the connection using the "Test Connection" buttons
3. Verify your API tokens are valid
4. Check that your Mealie/Tandoor instances are accessible from this machine

### Scraper Won't Start

1. Make sure at least one service (Mealie or Tandoor) is enabled
2. Verify you have sites in your active site list
3. Check the logs for error messages

## Original CLI Script

The original `mealie_dredger.py` script is still available and functional if you prefer the command-line interface.

## Docker Support (Coming Soon)

Docker support will be added in a future update to make deployment even easier.

## License

MIT License - See LICENSE file for details
