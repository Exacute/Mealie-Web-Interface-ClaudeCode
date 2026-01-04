# Getting Started with Mealie Recipe Dredger Web Interface

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd web_interface
pip install -r requirements.txt
```

### Step 2: Configure Your Settings
Edit `data/config.json` with your Mealie/Tandoor details:

```json
{
  "mealie": {
    "enabled": true,
    "url": "http://192.168.1.79:9000",
    "api_token": "YOUR_MEALIE_TOKEN_HERE"
  },
  "tandoor": {
    "enabled": false,
    "url": "http://192.168.1.80:8080",
    "api_key": "YOUR_TANDOOR_KEY_HERE"
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

**Getting Your API Tokens:**
- **Mealie**: Login → User Profile → Manage API Tokens → Create New
- **Tandoor**: Login → Settings → API Tokens → Create New

### Step 3: Start the Server
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

---

## 🎯 Your First Scrape

### Option A: Use All Sites (Recommended First Time)
1. Go to Dashboard: http://localhost:5000
2. Settings page → Test your Mealie connection
3. Dashboard → Click "Start Scraper"
4. Watch the progress bar and stats update in real-time!

### Option B: Use a Category List
1. Dashboard → Find "Site Lists" section
2. Select a category (e.g., "sites_caribbean.txt")
3. Click "Start Scraper"
4. Only Caribbean recipes will be imported!

---

## 📁 Available Site Lists

Your `data/` folder contains these pre-made lists:

| File Name | Sites | Description |
|-----------|-------|-------------|
| `sites.txt` | 157 | **All recipe sites** - complete collection |
| `sites_african_soul_food.txt` | 18 | African & Soul Food recipes |
| `sites_caribbean.txt` | 12 | Caribbean island recipes |
| `sites_indian_middle_eastern.txt` | 21 | Indian, Pakistani, Middle Eastern |
| `sites_latin_american.txt` | 9 | Mexican & Latin American |
| `sites_east_asian.txt` | 18 | Chinese, Japanese, Korean, Thai |
| `sites_instant_pot_air_fryer.txt` | 12 | Modern appliance recipes |
| `sites_general_high_quality.txt` | 67 | Top food blogs, diverse recipes |

---

## 🎨 Creating Your Own List

Want to create a custom list? Easy!

1. Create a new file: `data/sites_italian.txt`
2. Add this header:
```
# ========================================
# ITALIAN CUISINE
# ========================================
# Best Italian recipe blogs
```
3. Add URLs (one per line):
```
https://www.italianrecipe1.com
https://www.italianrecipe2.com
```
4. Go to Dashboard → Select your new list → Start!

---

## ⚙️ Important Settings Explained

### In the Settings Page:

**Target Recipes per Site** (default: 50)
- How many NEW recipes to grab from each site
- Lower = faster, Higher = more recipes

**Scan Depth** (default: 1000)
- How many sitemap entries to check
- Increase if sites have many non-recipe pages

**Dry Run** (default: off)
- When enabled: Finds recipes but doesn't import
- Use this to test without adding to your collection!

**Delay Between Imports** (default: 1.5 seconds)
- Time to wait between recipe imports
- Be polite to recipe sites - don't lower this too much

---

## 🔍 Understanding the Dashboard

### Status Card Shows:
- **Status**: Running (green) or Stopped (gray)
- **Progress**: 0-100% completion
- **Current Site**: Which blog is being scraped right now
- **Total Imported**: Number of recipes successfully added
- **Sites Progress**: 5/157 means 5 sites done, 157 total

### Real-Time Updates
The dashboard refreshes every 2 seconds automatically - no need to reload!

---

## 🚨 Common Issues & Solutions

### "Scraper won't start"
✅ **Solution**:
1. Enable at least Mealie OR Tandoor in Settings
2. Make sure your selected site list has URLs
3. Check the Logs page for error messages

### "Connection failed" when testing
✅ **Solution**:
1. Verify URL includes `http://` or `https://`
2. Check port number is correct (9000 for Mealie, 8080 for Tandoor)
3. Ensure Mealie/Tandoor is running and accessible
4. Test in browser: open the URL to confirm it loads

### "No new recipes found"
✅ **Solution**:
1. You may have already imported all recent recipes!
2. Try a different site list
3. Increase "Scan Depth" in Settings to 2000
4. Some sites may not have posted new recipes recently

### Port 5000 already in use
✅ **Solution**:
Edit `app.py`, change this line:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```
To:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```
Then access at: http://localhost:8080

---

## 💡 Pro Tips

### Tip 1: Start Small
First time? Use **Dry Run Mode** and a small category list (like Caribbean with 12 sites) to see how it works!

### Tip 2: Schedule Regular Runs
Run the scraper weekly/monthly to get new recipes as blogs post them.

### Tip 3: Organize by Cuisine
Create separate lists for:
- Quick weeknight meals
- Desserts and baking
- Healthy options
- Your favorite bloggers

### Tip 4: Monitor the Logs
The Logs page shows detailed info about what's happening - great for troubleshooting!

### Tip 5: Use Both Services
Enable both Mealie and Tandoor to keep your collections in sync!

---

## 📊 What Happens During a Scrape?

1. **Loads existing recipes** from Mealie/Tandoor (so it doesn't import duplicates)
2. **Visits each site** in your selected list
3. **Finds the sitemap** (XML file with all recipe URLs)
4. **Checks each URL** to verify it's actually a recipe (not an "About" page)
5. **Imports new recipes** that aren't already in your collection
6. **Waits politely** between imports (1.5 seconds by default)
7. **Continues** until it hits the target recipes per site, or runs out of new recipes

---

## 🎉 Success!

Once you see recipes importing:
- ✅ Check Mealie/Tandoor - new recipes should appear
- ✅ Watch the "Total Imported" counter climb
- ✅ The scraper will stop automatically when done
- ✅ Check the Logs page to see what was imported

---

## 📚 More Help

- **Detailed Docs**: See `README.md` in this folder
- **Technical Details**: See `README_WEB_INTERFACE.md`
- **Config Issues**: Edit `data/config.json` carefully (valid JSON required)

---

**Need more help?** Check the Logs page first - it usually tells you exactly what's wrong!

**Happy Cooking! 🍳👨‍🍳**
