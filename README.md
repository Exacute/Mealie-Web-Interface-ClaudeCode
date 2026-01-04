# Mealie Recipe Dredger - Web Interface

Welcome to the web-based interface for Mealie Recipe Dredger! This is a complete, standalone Flask application that allows you to manage and control recipe scraping through your browser.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python app.py
```

### 3. Open Your Browser

Navigate to: **http://localhost:5000**

## 📁 Directory Structure

```
web_interface/
├── app.py                          # Main Flask application
├── migrate.py                      # Migration tool (if needed)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── README_WEB_INTERFACE.md         # Detailed documentation
│
├── config/                         # Configuration management
│   ├── __init__.py
│   └── config_manager.py           # Config file handlers
│
├── core/                           # Core scraping logic
│   ├── __init__.py
│   ├── scraper.py                  # Main scraper class
│   ├── mealie_client.py            # Mealie API client
│   └── tandoor_client.py           # Tandoor API client
│
├── routes/                         # Flask routes/endpoints
│   ├── __init__.py
│   ├── main.py                     # Dashboard & logs
│   ├── settings.py                 # Settings management
│   └── scraper_control.py          # Scraper controls
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── dashboard.html              # Main dashboard
│   ├── settings.html               # Settings page
│   └── logs.html                   # Log viewer
│
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css               # Styling
│   └── js/
│       └── app.js                  # JavaScript utilities
│
├── data/                           # Configuration & site lists
│   ├── config.json                 # Application configuration
│   ├── sites.txt                   # Complete site list (all 157 sites)
│   │
│   │── CATEGORIZED SITE LISTS ──
│   ├── sites_african_soul_food.txt        # 18 sites
│   ├── sites_caribbean.txt                # 12 sites
│   ├── sites_indian_middle_eastern.txt    # 21 sites
│   ├── sites_latin_american.txt           # 9 sites
│   ├── sites_east_asian.txt               # 18 sites
│   ├── sites_instant_pot_air_fryer.txt    # 12 sites
│   └── sites_general_high_quality.txt     # 67 sites
│
└── logs/                           # Scraper logs
    └── scraper.log                 # Runtime logs
```

## 🎯 Features

### Dashboard
- **Real-time Status**: Monitor scraping progress with auto-refresh every 2 seconds
- **Start/Stop Controls**: Control the scraper with a single click
- **Site List Selector**: Switch between different cuisine categories
- **Progress Bar**: Visual progress tracking
- **Statistics**: Total recipes imported, sites completed, current site

### Settings
- **Enable/Disable Services**: Toggle Mealie and Tandoor independently
- **API Configuration**: Set URLs and API tokens for both services
- **Scraper Settings**: Configure target recipes per site, scan depth, dry run mode
- **Connection Testing**: Test your API connections before starting

### Logs
- **Real-time Viewing**: See scraper logs as they're generated
- **Auto-refresh**: Automatically updates when scraper is running
- **Last 500 Lines**: Most recent log entries displayed

## 📋 Site Lists

The `data/` directory contains pre-organized site lists:

### Complete List
- **sites.txt**: All 157 recipe sites in one file

### Categorized Lists
Each category file includes descriptive headers and is ready to use:

1. **sites_african_soul_food.txt** (18 sites)
   - African and Soul Food recipes
   - Includes West African, Soul Food, and Southern cuisine

2. **sites_caribbean.txt** (12 sites)
   - Caribbean island recipes
   - Jamaican, Cuban, Dominican, Puerto Rican cuisine

3. **sites_indian_middle_eastern.txt** (21 sites)
   - Indian, Pakistani, Middle Eastern recipes
   - Curries, kebabs, Mediterranean dishes

4. **sites_latin_american.txt** (9 sites)
   - Mexican and Latin American recipes
   - Tacos, empanadas, South American cuisine

5. **sites_east_asian.txt** (18 sites)
   - Chinese, Japanese, Korean, Thai, Vietnamese
   - Stir-fries, sushi, ramen, pho

6. **sites_instant_pot_air_fryer.txt** (12 sites)
   - Modern appliance recipes
   - Pressure cooker, slow cooker, air fryer

7. **sites_general_high_quality.txt** (67 sites)
   - Top-rated general food blogs
   - Diverse recipes, baking, healthy options

## ⚙️ Configuration

### First Time Setup

1. **Edit config.json** in the `data/` directory:

```json
{
  "mealie": {
    "enabled": true,
    "url": "http://your-mealie-ip:9000",
    "api_token": "your-token-here"
  },
  "tandoor": {
    "enabled": false,
    "url": "http://your-tandoor-ip:8080",
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

2. **Get API Tokens**:
   - **Mealie**: User Profile → Manage API Tokens
   - **Tandoor**: Settings → API Tokens

3. **Test Connections**: Use the "Test Connection" buttons on the Settings page

## 🎨 Using Category Lists

To use a specific category:

1. Go to the **Dashboard**
2. Find the **Site Lists** section
3. Select the radio button for your desired category
4. Click **Start Scraper**

The scraper will only import recipes from sites in that list!

## 💡 Tips & Tricks

### Testing Before Import
Enable **Dry Run Mode** in settings to test the scraper without actually importing recipes. This helps you:
- See which recipes would be found
- Test your site lists
- Verify the scraper is working correctly

### Creating Custom Lists
1. Create a new `.txt` file in the `data/` directory
2. Name it `sites_yourname.txt`
3. Add URLs (one per line)
4. Use `#` for comments and headers
5. Select it from the Dashboard

Example format:
```
# ========================================
# MY FAVORITE BAKING BLOGS
# ========================================
https://sallysbakingaddiction.com
https://preppykitchen.com
https://sugarspunrun.com
```

### Managing Multiple Recipe Managers
You can enable both Mealie and Tandoor simultaneously! The scraper will:
- Import new recipes to both services
- Skip duplicates in each service independently
- Track progress for both

## 🐛 Troubleshooting

### Port Already in Use
Edit `app.py` and change the port:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Can't Connect to Mealie/Tandoor
1. Verify the URL includes `http://` or `https://`
2. Check the port number is correct
3. Ensure your recipe manager is running
4. Test the connection using the Settings page

### Scraper Won't Start
1. Enable at least one service (Mealie or Tandoor)
2. Verify your site list has URLs
3. Check logs for error messages

### No Recipes Found
1. The sites may not have new recipes (already imported)
2. Try a different site list
3. Increase the `scan_depth` in settings
4. Check that sites are accessible from your network

## 📊 Understanding Progress

The dashboard shows:
- **Status**: Running or Stopped
- **Progress**: Percentage complete (0-100%)
- **Current Site**: Which blog is being scraped now
- **Total Imported**: Number of recipes successfully imported
- **Sites Progress**: How many sites completed vs total

## 🔒 Security Notes

- Store your `config.json` securely (contains API tokens)
- Don't commit `config.json` to version control
- Use HTTPS URLs for Mealie/Tandoor if possible
- Consider using environment variables for sensitive data

## 📖 Additional Documentation

See `README_WEB_INTERFACE.md` for more detailed documentation including:
- Advanced configuration options
- API token setup guides
- Docker deployment (coming soon)
- Troubleshooting guide

## 🆘 Need Help?

1. Check the **Logs** page for error messages
2. Review `README_WEB_INTERFACE.md` for detailed docs
3. Verify your `config.json` is valid JSON
4. Test API connections on the Settings page

## 📝 License

MIT License - See LICENSE file for details

---

**Happy Recipe Collecting! 🍳**
