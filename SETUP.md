# Setup Guide for New Users

## 🚀 Quick Setup

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd web_interface
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Create Your Configuration File

Copy the example configuration file:

**Windows:**
```bash
copy data\config.example.json data\config.json
```

**Mac/Linux:**
```bash
cp data/config.example.json data/config.json
```

### Step 4: Edit Your Configuration

Open `data/config.json` and add your details:

```json
{
  "mealie": {
    "enabled": true,
    "url": "http://192.168.1.100:9000",
    "api_token": "your-actual-mealie-token"
  },
  "tandoor": {
    "enabled": false,
    "url": "http://192.168.1.100:8080",
    "api_key": "your-actual-tandoor-key"
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

### Step 5: Get Your API Tokens

#### For Mealie:
1. Log into your Mealie instance
2. Go to **User Profile** → **Manage API Tokens**
3. Click **Create New Token**
4. Give it a name (e.g., "Recipe Dredger")
5. Copy the token
6. Paste it into `data/config.json` as the `api_token` value

#### For Tandoor (Optional):
1. Log into your Tandoor instance
2. Go to **Settings** → **API Tokens**
3. Click **Create New Token**
4. Copy the token
5. Paste it into `data/config.json` as the `api_key` value
6. Set `"enabled": true` in the tandoor section

### Step 6: Start the Application
```bash
python app.py
```

### Step 7: Access the Web Interface
Open your browser to: **http://localhost:5000**

---

## 🔒 Security Notes

### Important Files:
- ✅ **config.example.json** - Safe to commit (contains placeholders)
- ❌ **config.json** - NEVER commit (contains your actual API tokens)

The `.gitignore` file is configured to protect `config.json` from being accidentally committed.

### Verify Your Config is Protected:
```bash
git status
```

You should NOT see `data/config.json` in the list of files to commit.

---

## 🎯 First Run Recommendations

1. **Enable Dry Run Mode** first:
   - Edit `config.json`
   - Set `"dry_run": true`
   - This tests without actually importing recipes

2. **Test with a Small List**:
   - Use `sites_caribbean.txt` (12 sites) for your first test
   - Select it from the Dashboard

3. **Test API Connections**:
   - Go to Settings page
   - Click "Test Connection" for Mealie
   - Verify it shows "Connection successful"

4. **Start Small**:
   - Click "Start Scraper" on the Dashboard
   - Watch the progress
   - Check your Mealie/Tandoor for imported recipes

5. **Disable Dry Run**:
   - Once testing is successful
   - Edit `config.json`
   - Set `"dry_run": false`
   - Start importing for real!

---

## 📁 Site Lists Included

The following site lists are ready to use:

| File | Sites | Description |
|------|-------|-------------|
| `sites.txt` | 157 | Complete collection |
| `sites_african_soul_food.txt` | 18 | African & Soul Food |
| `sites_caribbean.txt` | 12 | Caribbean recipes |
| `sites_indian_middle_eastern.txt` | 21 | Indian & Middle Eastern |
| `sites_latin_american.txt` | 9 | Latin American |
| `sites_east_asian.txt` | 18 | East Asian cuisine |
| `sites_instant_pot_air_fryer.txt` | 12 | Modern appliances |
| `sites_general_high_quality.txt` | 67 | Top food blogs |

---

## 🆘 Troubleshooting

### "Config file not found" Error
You need to create `config.json` from the example:
```bash
cp data/config.example.json data/config.json
```

### "Connection failed" Error
1. Check your URL includes `http://` or `https://`
2. Verify the port number is correct
3. Ensure Mealie/Tandoor is running
4. Test the URL in your browser first

### "lxml" Parser Error
Install the required XML parser:
```bash
pip install lxml --upgrade
```

### Port 5000 Already in Use
Edit `app.py` and change the port:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

---

## 📚 Additional Documentation

- **GETTING_STARTED.md** - Detailed first-time setup
- **README.md** - Complete feature documentation
- **FILE_STRUCTURE.md** - Project organization
- **README_WEB_INTERFACE.md** - Technical details

---

## 🤝 Contributing

If you make improvements:

1. **Never commit your config.json**
2. Update `config.example.json` if you add new config options
3. Update documentation for new features
4. Test with dry run mode first

---

## ✅ Setup Complete!

Once you have:
- ✅ Created `config.json` from the example
- ✅ Added your API tokens
- ✅ Tested the connection
- ✅ Selected a site list

You're ready to start importing recipes! 🎉

**Open http://localhost:5000 and click "Start Scraper"**
