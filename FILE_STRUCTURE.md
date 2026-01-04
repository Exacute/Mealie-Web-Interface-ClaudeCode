# Web Interface - Complete File Structure

## 📋 Complete File Listing

```
web_interface/
│
├── 📄 GETTING_STARTED.md           ⭐ START HERE - Quick setup guide
├── 📄 README.md                    📖 Main documentation
├── 📄 README_WEB_INTERFACE.md      📖 Detailed technical docs
├── 📄 FILE_STRUCTURE.md            📋 This file
│
├── 🐍 app.py                       ▶️  Main Flask application - RUN THIS
├── 🐍 migrate.py                   🔧 Migration tool (optional)
├── 📄 requirements.txt             📦 Python dependencies
│
├── 📁 config/                      ⚙️  Configuration Management
│   ├── __init__.py
│   └── config_manager.py           - Config file loader/saver
│
├── 📁 core/                        🎯 Core Scraping Logic
│   ├── __init__.py
│   ├── scraper.py                  - Main scraper class
│   ├── mealie_client.py            - Mealie API client
│   └── tandoor_client.py           - Tandoor API client
│
├── 📁 routes/                      🌐 Flask Routes/Endpoints
│   ├── __init__.py
│   ├── main.py                     - Dashboard & logs routes
│   ├── settings.py                 - Settings page routes
│   └── scraper_control.py          - Start/stop/status API
│
├── 📁 templates/                   🎨 HTML Templates
│   ├── base.html                   - Base layout with navigation
│   ├── dashboard.html              - Main dashboard page
│   ├── settings.html               - Settings/configuration page
│   └── logs.html                   - Log viewer page
│
├── 📁 static/                      💅 Static Assets (CSS/JS)
│   ├── css/
│   │   └── style.css               - All styling
│   └── js/
│       └── app.js                  - JavaScript utilities
│
├── 📁 data/                        💾 Configuration & Site Lists
│   ├── config.json                 ⚙️  Your configuration (EDIT THIS)
│   │
│   ├── sites.txt                   📝 Complete list (all 157 sites)
│   │
│   ├── 🌍 CATEGORIZED SITE LISTS:
│   ├── sites_african_soul_food.txt         (18 sites)
│   ├── sites_caribbean.txt                 (12 sites)
│   ├── sites_indian_middle_eastern.txt     (21 sites)
│   ├── sites_latin_american.txt            (9 sites)
│   ├── sites_east_asian.txt                (18 sites)
│   ├── sites_instant_pot_air_fryer.txt     (12 sites)
│   └── sites_general_high_quality.txt      (67 sites)
│
└── 📁 logs/                        📊 Runtime Logs
    └── scraper.log                 - Scraper execution logs
```

---

## 🎯 Key Files Explained

### Essential Files (Must Have)

#### ▶️ **app.py**
- Main Flask application
- **Run this to start the web server**
- Command: `python app.py`

#### ⚙️ **data/config.json**
- Your configuration file
- **EDIT THIS with your Mealie/Tandoor settings**
- Contains API tokens, URLs, scraper settings

#### 📝 **data/sites.txt** (or any category list)
- List of recipe site URLs to scrape
- One URL per line
- Lines starting with `#` are comments

#### 📄 **requirements.txt**
- Python package dependencies
- Install with: `pip install -r requirements.txt`

---

### Documentation Files (Read These)

#### ⭐ **GETTING_STARTED.md**
- **START HERE if you're new**
- Quick 3-step setup guide
- Common issues & solutions
- Your first scrape walkthrough

#### 📖 **README.md**
- Main documentation
- Feature overview
- Directory structure
- Tips & tricks

#### 📖 **README_WEB_INTERFACE.md**
- Detailed technical documentation
- Advanced configuration
- API token setup
- Troubleshooting guide

#### 📋 **FILE_STRUCTURE.md**
- This file
- Complete file listing
- Purpose of each file

---

### Backend Python Files

#### 🐍 **config/config_manager.py**
- Loads and saves `config.json`
- Manages site list files
- Validates configuration

#### 🐍 **core/scraper.py**
- Main scraping logic
- Recipe verification
- Sitemap parsing
- Progress tracking

#### 🐍 **core/mealie_client.py**
- Mealie API interactions
- Import recipes to Mealie
- Fetch existing recipes
- Connection testing

#### 🐍 **core/tandoor_client.py**
- Tandoor API interactions
- Import recipes to Tandoor
- Fetch existing recipes
- Connection testing

#### 🐍 **routes/main.py**
- Dashboard page route
- Logs viewer route

#### 🐍 **routes/settings.py**
- Settings page route
- Save configuration
- Test API connections

#### 🐍 **routes/scraper_control.py**
- Start scraper endpoint
- Stop scraper endpoint
- Status check endpoint
- Site list management

---

### Frontend Files

#### 🎨 **templates/base.html**
- Base template for all pages
- Navigation bar
- Flash messages
- Common layout

#### 🎨 **templates/dashboard.html**
- Main dashboard
- Status display
- Start/Stop buttons
- Site list selector
- Real-time updates

#### 🎨 **templates/settings.html**
- Configuration form
- Mealie settings
- Tandoor settings
- Scraper settings
- Test connection buttons

#### 🎨 **templates/logs.html**
- Log viewer
- Auto-refresh when running
- Last 500 log lines

#### 💅 **static/css/style.css**
- All styling
- Responsive design
- Cards, buttons, forms
- Progress bars

#### 💅 **static/js/app.js**
- JavaScript utilities
- Flash message handling
- Helper functions

---

## 📊 Data Files

### Configuration

#### **config.json**
```json
{
  "mealie": {
    "enabled": true,
    "url": "http://192.168.1.79:9000",
    "api_token": "your-token"
  },
  "tandoor": {
    "enabled": false,
    "url": "http://192.168.1.80:8080",
    "api_key": "your-key"
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

### Site Lists

All site lists follow this format:
```
# ========================================
# CATEGORY NAME
# ========================================
# Description

https://www.site1.com
https://www.site2.com
```

#### Available Lists:

1. **sites.txt** - Complete collection (157 sites)
2. **sites_african_soul_food.txt** - 18 African & Soul Food blogs
3. **sites_caribbean.txt** - 12 Caribbean recipe sites
4. **sites_indian_middle_eastern.txt** - 21 Indian/Middle Eastern blogs
5. **sites_latin_american.txt** - 9 Latin American recipe sites
6. **sites_east_asian.txt** - 18 Asian cuisine blogs
7. **sites_instant_pot_air_fryer.txt** - 12 appliance-focused sites
8. **sites_general_high_quality.txt** - 67 top-rated general food blogs

---

## 🔧 Optional Files

#### 🐍 **migrate.py**
- Migration tool for old config format
- Run once if migrating from old `mealie_dredger.py`
- Not needed if starting fresh

---

## 📁 Generated Files/Folders

These are created automatically when you run the application:

#### 📁 **logs/**
- Created automatically
- Contains `scraper.log`
- Runtime logs from scraper

#### 📄 **logs/scraper.log**
- Created when scraper runs
- Contains detailed execution logs
- Viewable from Logs page

---

## 🚀 Quick Reference

### To Start the Application:
```bash
cd web_interface
python app.py
```

### To Edit Configuration:
```
Edit: data/config.json
```

### To Add Sites:
```
Edit: data/sites.txt (or create new sites_*.txt)
```

### To View Logs:
```
Read: logs/scraper.log
OR visit: http://localhost:5000/logs
```

### To Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## 📝 Notes

- All Python files use UTF-8 encoding
- Site lists must be UTF-8 encoded
- config.json must be valid JSON
- HTML templates use Jinja2 syntax
- CSS is vanilla (no preprocessor)
- JavaScript is vanilla (no frameworks)

---

## 🆘 If Something's Missing

All these files should be present in the `web_interface/` directory. If any are missing:

1. Check you're in the correct directory
2. Re-extract from the archive
3. Check file permissions

---

**Everything Ready!** 🎉

See `GETTING_STARTED.md` for next steps!
