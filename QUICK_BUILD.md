# ⚡ Quick Build Guide

## 🎯 Super Easy Method (Recommended)

### Just Double-Click This:
```
build.bat
```

That's it! The executable will be in the `dist/` folder! 🎉

---

## 🚀 Manual Build (One Command)

```bash
cd web_interface
pyinstaller recipe_dredger.spec
```

**Output:** `dist/Recipe_Dredger.exe`

---

## 📦 What You Get

✅ **Single executable file:** `Recipe_Dredger.exe` (~30-40 MB)
✅ **No Python needed** to run it
✅ **Works on any Windows PC** (7 or later)
✅ **Includes setup wizard** for first-run
✅ **All site lists included**

---

## 🎁 How to Share

### Option 1: Just the EXE
1. Find: `dist/Recipe_Dredger.exe`
2. Share it (email, USB drive, cloud storage)
3. Done!

### Option 2: With Documentation
1. Create a folder named `Recipe_Dredger_v1.0`
2. Copy these files:
   - `dist/Recipe_Dredger.exe`
   - `FIRST_RUN_SETUP.md`
   - `README.md`
3. Zip the folder
4. Share the ZIP file

---

## 👤 User Instructions

When someone receives your executable:

1. **Run** `Recipe_Dredger.exe`
2. **Browser opens** automatically
3. **Setup wizard** appears
4. **Fill in** Mealie URL and API token
5. **Start scraping!** 🎉

No installation, no Python, no config files to edit!

---

## ⚠️ Common Issues

### "Windows protected your PC" warning
**This is normal!**
- Click "More info"
- Click "Run anyway"

This appears because the EXE isn't digitally signed.

### Build failed
```bash
pip install -r requirements.txt
pip install pyinstaller --upgrade
```

### EXE file is large (30+ MB)
**This is normal!** It includes:
- Python interpreter
- Flask framework
- All dependencies
- Your application

---

## 🔧 Advanced Options

See `BUILD_EXECUTABLE.md` for:
- Adding custom icon
- Hiding console window
- Reducing file size
- Creating release packages
- Troubleshooting

---

## ✅ Quick Checklist

Before building:
- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] PyInstaller installed: `pip install pyinstaller`
- [ ] In the `web_interface` folder
- [ ] Your `config.json` has real values (for testing)

After building:
- [ ] Test the EXE: Run `dist/Recipe_Dredger.exe`
- [ ] Browser opens to http://localhost:5000
- [ ] Setup wizard works
- [ ] Can import recipes

Ready to share:
- [ ] EXE file works on your PC
- [ ] Include documentation
- [ ] Don't share your `config.json`!

---

## 📊 Build Time

- **First build:** 2-3 minutes
- **Subsequent builds:** 1-2 minutes
- **File size:** 30-40 MB

---

## 🎉 That's It!

**Easiest way:** Just run `build.bat`

**Your executable:** `dist/Recipe_Dredger.exe`

**Share it:** Anyone with Windows can run it!

No Python, no installation, no hassle! 🚀
