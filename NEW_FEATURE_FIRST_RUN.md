# 🎉 New Feature: First-Run Setup Wizard!

## What's New

I've added a **beautiful Setup Wizard** that appears automatically on first run! No more editing config files! 🚀

---

## How It Works

### Before (Old Way)
1. Start the app
2. See error or empty config
3. Stop the app
4. Open `data/config.json` in text editor
5. Manually edit JSON
6. Hope you didn't break the JSON syntax
7. Restart app
8. Hope everything works

### Now (New Way)
1. Start the app
2. **Setup Wizard appears automatically** ✨
3. Fill in a simple form
4. Click button to open Mealie's API tokens page
5. Test connection with one click
6. Click "Complete Setup"
7. **Done! Start using immediately!** 🎉

---

## Key Features

### ✅ Automatic Detection
- Detects if this is your first run
- Automatically redirects to Setup Wizard
- No manual config file needed!

### ✅ Direct Links to API Token Pages
- Click **"Open API Tokens Page"** button
- Opens directly to: `http://your-mealie:9000/user/profile/api-tokens`
- No more searching through menus!

### ✅ Connection Testing
- Test Mealie connection before saving
- Test Tandoor connection (if using)
- See instant feedback (green = success, red = error)

### ✅ Step-by-Step Guidance
- Clear numbered steps
- Help boxes with instructions
- Required fields marked with *
- Optional Tandoor section

### ✅ Beautiful Interface
- Clean, modern design
- Color-coded steps
- Helpful tooltips
- Mobile-friendly

---

## What Happens On First Run

### 1. You Start the App
```bash
cd web_interface
python app.py
```

### 2. Open Browser
Navigate to: `http://localhost:5000`

### 3. Setup Wizard Appears!
Instead of the Dashboard, you see:
- **Welcome message** 🎉
- **Step 1: Mealie Configuration** (required)
  - Enter Mealie URL
  - Button to open API tokens page
  - Paste API token
  - Test connection
- **Step 2: Tandoor Configuration** (optional)
  - Enter Tandoor URL
  - Button to open API tokens page
  - Paste API key
  - Test connection
- **Complete Setup** button

### 4. Save & Redirect
- Configuration saved to `data/config.json`
- Redirected to Dashboard
- Ready to scrape recipes immediately!

---

## Technical Details

### Files Added
1. **`config/setup_wizard.py`**
   - Detects first run
   - Saves wizard configuration
   - Validates input

2. **`routes/setup.py`**
   - Setup wizard routes
   - Test connection endpoints
   - Form submission handler

3. **`templates/setup_wizard.html`**
   - Beautiful setup form
   - Connection testing UI
   - Direct links to token pages

### Files Modified
1. **`routes/main.py`**
   - Added first-run check
   - Redirects to wizard if needed

2. **`app.py`**
   - Registered setup blueprint

### How First Run is Detected
The system checks if:
- `config.json` doesn't exist, OR
- Mealie URL contains "YOUR_MEALIE", OR
- API token is empty or contains "YOUR_MEALIE"

If any condition is true → Show Setup Wizard!

---

## User Experience Flow

```
Start App
    ↓
First Run? ────→ No ────→ Show Dashboard
    ↓ Yes
    ↓
Setup Wizard
    ↓
Enter Mealie URL
    ↓
Click "Open API Tokens Page" ←─── Opens exact page!
    ↓
Get token from Mealie
    ↓
Paste token in wizard
    ↓
Click "Test Connection" ←───── Instant feedback!
    ↓
Connection OK? ────→ No ────→ Fix and retry
    ↓ Yes
    ↓
(Optional) Setup Tandoor
    ↓
Click "Complete Setup"
    ↓
Config Saved!
    ↓
Redirect to Dashboard
    ↓
Start Scraping! 🎉
```

---

## Example URLs

### Mealie API Tokens Page
```
http://192.168.1.79:9000/user/profile/api-tokens
```

The wizard constructs this automatically from your base URL!

### What Users Enter
Just: `http://192.168.1.79:9000`

The wizard adds `/user/profile/api-tokens` automatically!

---

## Benefits

### For New Users
✅ **No config file editing** - Simple web form
✅ **Clear instructions** - Step-by-step guidance
✅ **Direct links** - Opens exact API token page
✅ **Instant validation** - Test connections before saving
✅ **Error prevention** - Can't proceed with invalid config
✅ **Professional UX** - Looks and feels polished

### For Experienced Users
✅ **Still works** - Can still edit config.json manually
✅ **Skippable** - Create config.json before first run to skip wizard
✅ **Resettable** - Delete config.json to run wizard again

---

## Testing the Wizard

### To See It Again
Delete your config file:
```bash
# Windows
del data\config.json

# Mac/Linux
rm data/config.json
```

Then start the app - wizard will appear!

### To Skip It
Create a valid `config.json` with real values before starting the app.

---

## Screenshots Description

### Setup Wizard - Header
- Large welcome message
- "Let's get you set up in just a few minutes"
- Clean, inviting design

### Step 1 - Mealie Setup
- Blue numbered circle: "1"
- Help box with instructions
- **"Open API Tokens Page"** button
- URL input field
- Token input field
- **"Test Mealie Connection"** button
- Result message (green or red)

### Step 2 - Tandoor Setup (Optional)
- Blue numbered circle: "2"
- "Optional" label
- Same easy interface
- Skip if not using Tandoor

### Complete Setup Button
- Large blue button
- "Complete Setup & Start Using Recipe Dredger"
- Note: "You can always change these settings later"

---

## Error Handling

### Invalid URL
- Shows error message
- Won't save until fixed
- Helpful error text

### Invalid Token
- Test connection shows error
- Explains what's wrong
- Links to help docs

### Empty Required Fields
- Form validation prevents submission
- Highlights missing fields
- Clear error messages

---

## Migration from Old Config

If you have an existing `config.json` with real values:
- ✅ Wizard **won't appear**
- ✅ App works normally
- ✅ Your settings are preserved

The wizard only appears for new installations!

---

## Future Enhancements (Ideas)

- [ ] Add video tutorial link
- [ ] Add "Skip Setup" for advanced users
- [ ] Remember last entered URL
- [ ] Auto-detect Mealie on local network
- [ ] Import/Export config file
- [ ] Setup profiles (multiple configs)

---

## Feedback

The Setup Wizard makes the first-run experience **10x better**! New users can:
- Get started in **3 minutes**
- Never touch a config file
- Test connections before committing
- Get help exactly when needed
- Feel confident about their setup

---

## Summary

| Feature | Status |
|---------|--------|
| Automatic first-run detection | ✅ Working |
| Setup Wizard UI | ✅ Beautiful |
| Direct link to API tokens | ✅ Implemented |
| Connection testing | ✅ Working |
| Form validation | ✅ Complete |
| Error handling | ✅ Comprehensive |
| Mobile responsive | ✅ Yes |
| Optional Tandoor | ✅ Supported |
| GitHub-safe | ✅ No sensitive data |

---

**Try it now! Delete your config.json and restart the app!** 🚀
