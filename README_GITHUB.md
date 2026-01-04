# Mealie Recipe Dredger - Web Interface

A Flask-based web application for automatically importing recipes from 150+ high-quality food blogs into Mealie or Tandoor recipe managers.

## ✨ Features

- 🌐 **Web-based Interface** - Control everything from your browser
- 🔄 **Real-time Progress** - Monitor scraping with live updates
- 🎯 **Smart Duplicate Detection** - Automatically skips recipes you already have
- 📂 **Categorized Site Lists** - Pre-organized by cuisine type (African, Caribbean, Asian, etc.)
- ⚙️ **Easy Configuration** - Simple JSON config file
- 🔌 **Dual Service Support** - Works with Mealie and/or Tandoor
- 🧪 **Dry Run Mode** - Test without importing
- 📊 **Built-in Logs** - View scraper activity in real-time

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Mealie or Tandoor recipe manager (or both)
- API token from your recipe manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mealie-recipe-dredger.git
cd mealie-recipe-dredger/web_interface
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create your configuration**
```bash
# Windows
copy data\config.example.json data\config.json

# Mac/Linux
cp data/config.example.json data/config.json
```

4. **Edit `data/config.json`** with your details
```json
{
  "mealie": {
    "enabled": true,
    "url": "http://your-mealie-ip:9000",
    "api_token": "your-api-token"
  }
}
```

5. **Start the application**
```bash
python app.py
```

6. **Open your browser**
```
http://localhost:5000
```

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup instructions
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - First-time user guide
- **[README.md](README.md)** - Complete feature documentation
- **[FILE_STRUCTURE.md](FILE_STRUCTURE.md)** - Project organization

## 🌍 Recipe Sources

The application includes curated lists of 157 high-quality recipe blogs:

- **African & Soul Food** (18 sites)
- **Caribbean** (12 sites)
- **Indian & Middle Eastern** (21 sites)
- **Latin American** (9 sites)
- **East Asian** (18 sites)
- **Instant Pot & Air Fryer** (12 sites)
- **General High Quality** (67 sites)

All sites are thoroughly vetted for recipe quality and proper schema markup.

## 🎯 How It Works

1. **Discovers Recipes** - Finds recipe URLs via sitemaps
2. **Verifies Content** - Checks for Recipe schema markup
3. **Avoids Duplicates** - Skips recipes you already have
4. **Imports Efficiently** - Respects rate limits with configurable delays
5. **Tracks Progress** - Real-time updates in the dashboard

## 📸 Screenshots

### Dashboard
Monitor scraping progress in real-time with status updates, progress bars, and statistics.

### Settings
Configure Mealie/Tandoor connections, test API connections, and adjust scraper settings.

### Site Lists
Switch between different cuisine categories with pre-organized site lists.

## ⚙️ Configuration Options

```json
{
  "scraper": {
    "dry_run": false,               // Test mode (doesn't import)
    "target_recipes_per_site": 50,  // Max new recipes per site
    "scan_depth": 1000,             // Sitemap entries to check
    "delay_between_imports": 1.5    // Seconds between imports
  }
}
```

## 🔒 Security

- All sensitive data (API tokens, URLs) is stored in `config.json`
- `config.json` is excluded from Git via `.gitignore`
- Only the example template (`config.example.json`) is version controlled
- Never commit your actual `config.json` file

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (use dry run mode)
5. Submit a pull request

**Important:** Never commit your `config.json` with actual API tokens!

## 📝 Requirements

- Python 3.8 or higher
- Flask 3.0.0
- BeautifulSoup4
- lxml
- requests

All dependencies are listed in `requirements.txt`.

## 🐛 Troubleshooting

### "lxml parser not found"
```bash
pip install lxml --upgrade
```

### "Connection failed"
1. Verify your Mealie/Tandoor URL is correct
2. Check the API token is valid
3. Ensure the service is running and accessible
4. Use the "Test Connection" button in Settings

### "No new recipes found"
1. You may have already imported all recent recipes
2. Try a different site list category
3. Increase the `scan_depth` in settings

See [SETUP.md](SETUP.md) for more troubleshooting tips.

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- Recipe blogs for providing structured recipe data
- Mealie and Tandoor teams for excellent recipe management software
- Contributors and users of this project

## ⚠️ Disclaimer

This tool is for personal use only. Please respect the terms of service of the recipe blogs you scrape. The included site lists feature blogs that:
- Have proper schema.org Recipe markup
- Allow automated access via sitemaps
- Are popular, reputable food blogs

Be respectful with scraping frequency and use the built-in delays.

## 📧 Support

- Check the [documentation](SETUP.md) first
- Open an issue for bugs or feature requests
- Include relevant logs when reporting issues

---

**Happy Recipe Collecting! 🍳**
