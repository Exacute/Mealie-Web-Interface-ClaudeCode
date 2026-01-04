# 🚀 Building an Executable File

Create a standalone `.exe` file that runs on any Windows computer without needing Python installed!

---

## 📋 Prerequisites

1. **PyInstaller** (already installed!)
2. All dependencies installed: `pip install -r requirements.txt`

---

## 🎯 Quick Build (Recommended)

### Option 1: Single Executable File (Easiest to Share)

```bash
cd web_interface
pyinstaller --onefile --name "Recipe_Dredger" --add-data "templates;templates" --add-data "static;static" --add-data "data/*.txt;data" --add-data "data/config.example.json;data" --hidden-import flask --hidden-import jinja2 --hidden-import lxml --hidden-import bs4 app.py
```

**Result:** Single `Recipe_Dredger.exe` file in `dist/` folder

**Pros:**
- ✅ Single file - easy to share
- ✅ No installation needed
- ✅ Portable

**Cons:**
- ⚠️ Slower startup (unpacks to temp folder)
- ⚠️ Larger file size (~30-40 MB)

---

### Option 2: Folder with Executable (Faster)

```bash
cd web_interface
pyinstaller --onedir --name "Recipe_Dredger" --add-data "templates;templates" --add-data "static;static" --add-data "data/*.txt;data" --add-data "data/config.example.json;data" --hidden-import flask --hidden-import jinja2 --hidden-import lxml --hidden-import bs4 app.py
```

**Result:** `Recipe_Dredger/` folder in `dist/` with `Recipe_Dredger.exe` inside

**Pros:**
- ✅ Faster startup
- ✅ Smaller main exe file

**Cons:**
- ⚠️ Must distribute entire folder
- ⚠️ Many files to manage

---

### Option 3: Using Spec File (Most Control)

I've created a custom spec file for you!

```bash
cd web_interface
pyinstaller recipe_dredger.spec
```

**Result:** `Recipe_Dredger.exe` in `dist/` folder

**Pros:**
- ✅ Customizable
- ✅ Repeatable builds
- ✅ All settings in one place

---

## 📦 What Gets Included

The executable includes:
- ✅ Python interpreter
- ✅ Flask and all dependencies
- ✅ Your application code
- ✅ Templates (HTML files)
- ✅ Static files (CSS, JavaScript)
- ✅ Site lists (all .txt files)
- ✅ Example config file

**NOT included:**
- ❌ Your actual `config.json` (stays local - contains API tokens!)
- ❌ Log files (created when app runs)

---

## 🎯 Step-by-Step Build Process

### Step 1: Clean Previous Builds (Optional)
```bash
cd web_interface
rmdir /s /q build dist
del *.spec
```

### Step 2: Build the Executable
```bash
pyinstaller recipe_dredger.spec
```

### Step 3: Find Your Executable
Look in: `web_interface/dist/Recipe_Dredger.exe`

### Step 4: Test It
```bash
cd dist
Recipe_Dredger.exe
```

Browser should open to: `http://localhost:5000`

---

## 📂 File Structure After Build

```
web_interface/
├── dist/
│   └── Recipe_Dredger.exe    ← Your executable!
├── build/                     ← Temporary build files (can delete)
├── recipe_dredger.spec        ← Build configuration
└── [other files]
```

---

## 🚀 Distributing Your Executable

### What to Share

**For Single File Build:**
```
Recipe_Dredger.exe               ← The executable
README.md                        ← Instructions
FIRST_RUN_SETUP.md              ← Setup guide
```

**For Folder Build:**
```
Recipe_Dredger/                  ← Entire folder
├── Recipe_Dredger.exe
├── _internal/                   ← Dependencies (include all!)
├── data/
│   ├── config.example.json
│   └── sites*.txt
└── README.md
```

### What NOT to Share
- ❌ Your `config.json` (contains API tokens!)
- ❌ `build/` folder
- ❌ Log files
- ❌ `__pycache__/`

---

## 📝 User Instructions

When sharing your executable, tell users:

### First Time Setup
1. **Run `Recipe_Dredger.exe`**
2. **Browser opens automatically** to http://localhost:5000
3. **Setup Wizard appears** - fill in your Mealie details
4. **Click "Complete Setup"**
5. **Start scraping!**

### Requirements
- ✅ Windows 7 or later
- ✅ No Python installation needed!
- ✅ No dependencies to install!
- ✅ Internet connection (to scrape recipes)
- ✅ Mealie or Tandoor running somewhere

---

## 🛠️ Advanced Options

### Add Custom Icon
```bash
pyinstaller recipe_dredger.spec --icon=icon.ico
```

Place `icon.ico` in the `web_interface` folder first.

### Hide Console Window
Edit `recipe_dredger.spec`, change:
```python
console=True,  # Show console
```
To:
```python
console=False,  # Hide console (Windows GUI mode)
```

**Warning:** Hiding console makes debugging harder!

### Reduce File Size
```bash
pyinstaller recipe_dredger.spec --upx-dir=upx
```

Install UPX first: https://upx.github.io/

---

## 🐛 Troubleshooting

### Error: "Failed to execute script"
**Fix:** Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Error: "No module named 'flask'"
**Fix:** Add to spec file hiddenimports:
```python
hiddenimports=['flask', 'jinja2', 'werkzeug']
```

### Templates Not Found
**Fix:** Check the spec file includes:
```python
datas=[('templates', 'templates'), ('static', 'static')]
```

### Large File Size
**Normal!** Executables include Python + all libraries.
- Single file: 30-40 MB (normal)
- Folder: 25-35 MB total (normal)

### "Windows protected your PC" Warning
**This is normal!** Windows SmartScreen warns about unsigned executables.
- Click "More info"
- Click "Run anyway"

To avoid this: Code sign your executable (requires certificate ~$100/year)

### Slow Startup (Single File)
**Normal!** Single-file mode unpacks to temp folder on each run.
- First run: 3-5 seconds
- Subsequent runs: Faster (cached)

**Solution:** Use folder mode (--onedir) for faster startup.

---

## 🔧 Customizing the Build

### Edit `recipe_dredger.spec`

**Change Name:**
```python
name='My_Recipe_App',
```

**Add Icon:**
```python
icon='icon.ico',
```

**Hide Console:**
```python
console=False,
```

**Add More Data Files:**
```python
datas=[
    ('templates', 'templates'),
    ('static', 'static'),
    ('docs/*.md', 'docs'),  # Add documentation
],
```

---

## 📊 Build Comparison

| Option | File Size | Startup Speed | Easy to Share | Build Command |
|--------|-----------|---------------|---------------|---------------|
| Single File | 35 MB | Slow (3-5s) | ⭐⭐⭐⭐⭐ | `--onefile` |
| Folder | 30 MB total | Fast (1s) | ⭐⭐⭐ | `--onedir` |
| Spec File | Customizable | Customizable | ⭐⭐⭐⭐ | `.spec` |

**Recommendation:** Use **Single File** for easy distribution!

---

## 🎁 Creating a Release Package

### Step 1: Build the Executable
```bash
pyinstaller recipe_dredger.spec
```

### Step 2: Create Release Folder
```bash
mkdir Release
copy dist\Recipe_Dredger.exe Release\
copy FIRST_RUN_SETUP.md Release\
copy README.md Release\
```

### Step 3: Create ZIP File
```bash
# Right-click Release folder → Send to → Compressed (zipped) folder
```

### Step 4: Share!
Upload `Release.zip` to:
- GitHub releases
- Google Drive
- Dropbox
- Email (if small enough)

---

## 📝 Example README for Users

Create a `README_USERS.md` to include with your executable:

```markdown
# Recipe Dredger - Quick Start

## What You Need
- Windows 7 or later
- Mealie or Tandoor recipe manager
- Internet connection

## How to Use
1. Run `Recipe_Dredger.exe`
2. Your browser opens automatically
3. Fill in the setup wizard
4. Start importing recipes!

## First Run
The setup wizard will ask for:
- Your Mealie URL (e.g., http://192.168.1.100:9000)
- Your Mealie API token (from Mealie settings)

## Problems?
- Read `FIRST_RUN_SETUP.md` for detailed setup
- Check that Mealie is running
- Verify your API token is correct

## Security Note
This app runs locally on your computer. Your API tokens never leave your machine!
```

---

## ✅ Quick Reference

### Build Commands

**Single File (Recommended):**
```bash
pyinstaller recipe_dredger.spec
```

**With Icon:**
```bash
pyinstaller recipe_dredger.spec --icon=icon.ico
```

**Clean Build:**
```bash
rmdir /s /q build dist
pyinstaller recipe_dredger.spec
```

### Output Locations

**Executable:** `dist/Recipe_Dredger.exe`

**Logs:** Same folder as exe, creates `logs/` when run

**Config:** Same folder as exe, creates `data/` when run

---

## 🎉 Success!

You now have a standalone executable that:
- ✅ Runs on any Windows PC
- ✅ No Python installation needed
- ✅ Includes setup wizard
- ✅ Self-contained and portable
- ✅ Ready to share!

**File:** `dist/Recipe_Dredger.exe`

**Size:** ~30-40 MB

**To Run:** Just double-click! 🚀

---

## 📚 Additional Resources

- PyInstaller Docs: https://pyinstaller.org/
- Spec File Reference: https://pyinstaller.org/en/stable/spec-files.html
- UPX Compression: https://upx.github.io/

---

**Happy Building! 🎉**
