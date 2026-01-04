# 🚀 First Run Setup - Super Easy!

## What Happens on First Run

When you start the Recipe Dredger for the first time, you'll see a **beautiful Setup Wizard** instead of having to edit config files!

---

## Setup Process (3 Minutes)

### Step 1: Start the Application
```bash
cd web_interface
python app.py
```

### Step 2: Open Your Browser
Navigate to: **http://localhost:5000**

You'll automatically be redirected to the **Setup Wizard** 🎉

### Step 3: Follow the Wizard

#### Mealie Configuration (Required)

1. **Enter your Mealie URL**
   - Example: `http://192.168.1.100:9000`
   - Include `http://` or `https://`
   - Include the port number (usually 9000)

2. **Get your API Token**
   - Click the **"Open Mealie"** button (opens your Mealie in a new tab)
   - In Mealie: Go to **User Profile → Manage API Tokens**
   - Click **Create New Token**
   - Give it a name like "Recipe Dredger"
   - Copy the token (long string starting with `eyJ...`)
   - Paste it into the wizard

3. **Test Connection**
   - Click **"Test Mealie Connection"**
   - You should see a green success message!

#### Tandoor Configuration (Optional)

Skip this section if you only use Mealie!

1. **Enter your Tandoor URL** (optional)
   - Example: `http://192.168.1.101:8080`
   - Include `http://` or `https://`
   - Include the port number (usually 8080)

2. **Get your API Key** (if using Tandoor)
   - Click the **"Open Tandoor"** button
   - In Tandoor: Go to **Settings → API Tokens**
   - Create a new token
   - Copy and paste it into the wizard

3. **Test Connection**
   - Click **"Test Tandoor Connection"**

### Step 4: Complete Setup
Click the big blue **"Complete Setup & Start Using Recipe Dredger"** button!

You'll be redirected to the Dashboard and can start scraping immediately! 🎉

---

## Features of the Setup Wizard

✅ **No config file editing required**
✅ **Test connections before saving**
✅ **Direct links to API token pages**
✅ **Step-by-step guidance**
✅ **Beautiful, user-friendly interface**
✅ **Validates your input**
✅ **Optional Tandoor setup**

---

## After Setup

Once setup is complete:
- Your configuration is saved to `data/config.json`
- You can access the Dashboard at http://localhost:5000
- You can change settings anytime from the **Settings** page
- The Setup Wizard won't appear again unless you reset your config

---

## Resetting Setup

If you want to run the Setup Wizard again:

### Option 1: Delete config file
```bash
# Windows
del data\config.json

# Mac/Linux
rm data/config.json
```

### Option 2: Edit config file
Open `data/config.json` and change the URL or token to placeholder values:
```json
{
  "mealie": {
    "url": "http://YOUR_MEALIE_IP:9000",
    "api_token": "YOUR_MEALIE_API_TOKEN_HERE"
  }
}
```

Next time you start the app, the Setup Wizard will appear!

---

## Screenshots

### Setup Wizard - Step 1: Mealie
- Clean, modern interface
- Helpful instructions
- Direct link to open Mealie
- Test connection button

### Setup Wizard - Step 2: Tandoor (Optional)
- Skip if you don't use Tandoor
- Same easy setup process

### Success!
- Redirects to Dashboard
- Ready to start importing recipes

---

## Troubleshooting

### "Connection failed" error
1. ✅ Check your URL has `http://` or `https://`
2. ✅ Verify the port number (9000 for Mealie, 8080 for Tandoor)
3. ✅ Ensure Mealie/Tandoor is running
4. ✅ Try opening the URL in your browser first
5. ✅ Check the API token is correct

### Can't get API token
1. Make sure you're logged into Mealie/Tandoor
2. Look for "User Profile" or "Settings" in the menu
3. Find "API Tokens" or "Manage API Tokens"
4. Create a new token
5. Copy the entire token (they're very long!)

### Wizard doesn't appear
The wizard only appears if:
- `config.json` doesn't exist, OR
- `config.json` has placeholder values

If you've already set up, go to Settings to make changes.

---

## Comparison: Old vs New Setup

### Old Way (Manual)
1. Open `data/config.json` in a text editor
2. Find your Mealie URL
3. Get API token from Mealie
4. Carefully edit JSON (don't break the syntax!)
5. Save file
6. Hope everything is correct
7. Start app and test

### New Way (Setup Wizard)
1. Start app
2. Fill in the form
3. Test connections
4. Click "Complete Setup"
5. Done! 🎉

---

## For Advanced Users

If you prefer the command line:
- You can still edit `data/config.json` directly
- The Setup Wizard won't override your settings
- You can skip the wizard entirely by creating a valid config file before first run

---

## Questions?

**Q: Do I need both Mealie and Tandoor?**
A: No! You only need one. Most people use just Mealie.

**Q: Can I change settings later?**
A: Yes! Go to Settings page anytime to update your configuration.

**Q: Is my API token stored securely?**
A: Yes! It's stored locally in `data/config.json` which is excluded from Git.

**Q: What if I make a mistake?**
A: No worries! Just go to Settings and update your configuration, or delete `config.json` to run the wizard again.

---

**Enjoy your new easy setup experience! 🎉**
