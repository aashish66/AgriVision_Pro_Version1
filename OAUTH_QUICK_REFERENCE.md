# 🚀 Quick Reference - OAuth Authentication

## 4-Minute Setup

### Step 1: Start App (30 seconds)
```bash
cd /path/to/agrivision
streamlit run streamlit_app.py
```

### Step 2: Click Authorization Link (1 minute)
- Sidebar: Click blue link **"🔗 Click here to authorize with Google"**
- Browser opens
- Click **"Authorize"** to grant permissions
- Google shows a code

### Step 3: Copy & Paste Code (1 minute)
- Copy code from Google (looks like: `4/0AY0e...`)
- Paste in app's **"Authorization Code:"** text box
- Click **"✅ Submit Code"** button
- See message: **"✅ Code accepted! Credentials ready."**

### Step 4: Connect to Earth Engine (1 minute)
- Get your **Project ID** from: https://code.earthengine.google.com
- Paste in app's **"Project ID"** field
- Click **"🔗 Connect to Google Earth Engine"** button
- See message: **"✅ Successfully authenticated!"**

### Done! 🎉
Start analyzing satellite imagery!

---

## What You'll See

### In Browser:
```
1. Click link
   ↓
2. See: "Google Account Authorization"
   ↓
3. See: "AgriVision Pro is asking to access your Google Account"
   ↓
4. Click: "Authorize"
   ↓
5. See: "Copy this code: 4/0AY0e..."
```

### In App Sidebar:
```
📍 Authorization Code:
┌─────────────────────────────┐
│ [4/0AY0e...]                │
└─────────────────────────────┘

✅ Submit Code

🔗 Click here to authorize with Google

─────────────────

🆔 Project ID:
┌─────────────────────────────┐
│ [ee-yourname]               │
└─────────────────────────────┘

🔗 Connect to Google Earth Engine
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Browser didn't open | Click link manually |
| Can't find code on Google | Scroll down, look for "Copy this code:" |
| Code doesn't work | Make sure you copied ENTIRE code, no spaces |
| "Connection failed" | Check your Project ID at code.earthengine.google.com |
| Code expired | Click authorization link again |

---

## Project ID Locations

### Where to Find It:
1. Visit: https://code.earthengine.google.com
2. Look at TOP of page
3. You'll see: **"Project: ee-yourname"** or **"my-project-123"**
4. That's your Project ID

### Format Examples:
- `ee-aashish`
- `ee-john-doe`
- `vegetation-analysis-prod`
- `agriculture-monitoring-2024`

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Copy code from Google | Ctrl+C (Cmd+C on Mac) |
| Paste in app | Ctrl+V (Cmd+V on Mac) |
| Submit | Click button OR press Enter |

---

## Features After Login

✅ **Satellite Analysis** - NDVI, SAVI, EVI calculations
✅ **Compare Images** - Time-series analysis
✅ **Upload Images** - Drone/camera analysis
✅ **View Maps** - Interactive satellite imagery
✅ **Download Results** - Export data and images

---

## Help in App

### Need Help?
- Click **"❓ Authentication Help"** in sidebar
- Read troubleshooting tips
- See common issues and solutions

### Still Stuck?
- Read **OAUTH_SETUP_GUIDE.md** (full guide)
- Check **OAUTH_AUTHENTICATION_RESTORED.md** (technical details)
- Check error messages in app (often show solutions)

---

## Remember

✅ Authorization code is **temporary** (expires in ~10 min)
✅ Only valid **one time** (can't reuse it)
✅ Get **fresh code** if first attempt fails
✅ Use **same Google account** each time
✅ Project ID from **code.earthengine.google.com** only

---

## Workflow

```
START
  ↓
Click Authorization Link
  ↓
Google Opens → Authorize → Get Code
  ↓
Copy Code
  ↓
Paste in App → Click Submit
  ↓
App says: "Code accepted!"
  ↓
Get Project ID (from code.earthengine.google.com)
  ↓
Paste Project ID in App
  ↓
Click: Connect to Earth Engine
  ↓
App says: "Successfully authenticated!"
  ↓
START ANALYZING! 🛰️🌱
```

---

## Tech Stack

- **OAuth 2.0** - Google authorization
- **Streamlit** - Web app framework
- **Earth Engine API** - Satellite imagery
- **Refresh Token** - Long-lived credentials
- **Python requests** - OAuth token exchange

---

All set! Start the app and follow the steps above. You'll be analyzing satellite imagery in under 5 minutes! 🚀
