# 🔐 AgriVision Pro - Authentication Troubleshooting Guide

## Overview
This guide helps you fix authentication issues with Google Earth Engine (GEE) in AgriVision Pro.

---

## ✅ Quick Fixes

### Issue 1: "Credentials file missing client_id or client_secret"

**Cause:** Wrong credentials file format or incomplete OAuth credentials.

**Solution:**

#### Option A: Use OAuth Credentials (Recommended for Local Use)
```bash
# In your terminal:
earthengine authenticate

# Follow browser prompts to sign in
# This creates ~/.config/earthengine/credentials
```

Then in the app:
1. Go to "🔐 GEE Authentication" in sidebar
2. Enter your Project ID
3. Click "Option 1: Upload your credentials file"
4. Upload the file from `~/.config/earthengine/credentials`
5. Click "Connect with Uploaded Credentials"

#### Option B: Use Service Account (For Production/Cloud)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new Service Account
3. Download the JSON key
4. Upload it in Option 1

---

### Issue 2: "Got authorization code but don't know where to add it"

**Solution:** The app now has a built-in input field!

1. Click "🌐 Sign in with Google"
2. A new browser window/tab will open
3. Complete the Google sign-in process
4. You'll see an **authorization code** (long alphanumeric string)
5. **Copy the entire code**
6. **Paste it** in the text field that appears: "🔐 Paste authorization code here:"
7. Press Enter or wait for automatic authentication

---

## 📋 Three Authentication Methods

### Method 1: Upload Credentials File (Easiest for Local Use)
```bash
# Step 1: Get credentials
earthengine authenticate

# Step 2: In Streamlit app
# 1. Enter Project ID
# 2. Upload file from ~/.config/earthengine/credentials
# 3. Click Connect
```
✅ Pros: Simple, one-time setup  
❌ Cons: Need terminal access initially

---

### Method 2: OAuth Authorization Code (Best for Streamlit Cloud)
```
Step 1: Click "🌐 Sign in with Google"
Step 2: Browser opens, sign in with Google
Step 3: Get authorization code
Step 4: Paste in app text field
Step 5: Wait for authentication
```
✅ Pros: No files needed, works on Streamlit Cloud  
❌ Cons: Need to repeat authorization code if session expires

---

### Method 3: Service Account JSON (Production/Automation)
```bash
# Create Service Account
# 1. Go to: https://console.cloud.google.com/
# 2. Create → Service Account
# 3. Create Key → JSON format
# 4. Download JSON file
# 5. Upload in app
```
✅ Pros: Works on servers/cloud, long-lived  
❌ Cons: More complex setup

---

## 🆘 Troubleshooting by Error Message

### Error: "Credentials file missing refresh_token"
**Problem:** The uploaded file is not a valid credentials file
**Solution:**
- Make sure you uploaded the file from `~/.config/earthengine/credentials`
- Not from Google Cloud Console (that's a service account, which is different)
- Re-run: `earthengine authenticate` and upload again

### Error: "Failed to initialize with service account"
**Problem:** Service account doesn't have Earth Engine access
**Solution:**
1. Go to [code.earthengine.google.com](https://code.earthengine.google.com)
2. Sign in with the Google account that owns the service account
3. Make sure Earth Engine is enabled for this account
4. Try again

### Error: "Credentials file format not recognized"
**Problem:** Uploaded file is not JSON or wrong type
**Solution:**
- Make sure file is valid JSON
- Try copying to `.json` extension to verify
- Supported formats:
  - OAuth: `~/.config/earthengine/credentials` (no extension)
  - Service Account: `.json` files from Google Cloud

### Error: "Failed to initialize with OAuth"
**Problem:** Authorization code issue or token expired
**Solution:**
1. Get a fresh authorization code by clicking "🌐 Sign in with Google"
2. Complete the sign-in process
3. Copy the NEW authorization code
4. Paste it in the text field

---

## 🔑 Getting Your Project ID

**Where to find it:**
1. Go to [code.earthengine.google.com](https://code.earthengine.google.com)
2. Look at the browser URL or top of the page
3. It looks like: `ee-yourname` or `projects/your-project-id`

**Or:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project from dropdown
3. Project ID is visible in the project list

**Common formats:**
- `ee-projectname`
- `my-gee-project`
- `ee-12345`

---

## 📝 Step-by-Step: First-Time Setup

### For Local Machine:
```bash
# Step 1: Create GEE account
# Go to: https://earthengine.google.com/signup/

# Step 2: Get credentials
earthengine authenticate
# Follow browser prompts

# Step 3: Get Project ID
# Visit: https://code.earthengine.google.com

# Step 4: Run Streamlit app
pip install -r requirements.txt
streamlit run streamlit_app.py

# Step 5: Enter Project ID in app sidebar

# Step 6: Upload credentials file from ~/.config/earthengine/credentials

# Step 7: Click "Connect with Uploaded Credentials"
```

### For Streamlit Cloud:
```bash
# Step 1-3: Same as above (get credentials locally first)

# Step 4: Add to .streamlit/secrets.toml
# gee_project_id = "your-project-id"
# gee_credentials = '{"type": "service_account", ...}'

# Or use OAuth:
# 1. Click "🌐 Sign in with Google" in deployed app
# 2. Paste authorization code when prompted
```

---

## 🐛 Debug Information

### To see what credentials type was detected:
- Open browser DevTools (F12)
- Watch for messages like:
  - "📋 Service Account credentials detected"
  - "🔐 OAuth credentials detected"

### Common issues checklist:
- ✅ Project ID is entered
- ✅ Credentials file is valid JSON
- ✅ File is from `~/.config/earthengine/credentials` (not Google Cloud)
- ✅ Authorization code is fresh (within 10 minutes)
- ✅ Browser allows popups for OAuth
- ✅ Google account has Earth Engine access

---

## 📞 Still Not Working?

### 1. Try Alternative Method
If OAuth code method doesn't work:
```bash
earthengine authenticate
# Then upload credentials file
```

If credentials file doesn't work:
```bash
# Try OAuth code method
# Click "🌐 Sign in with Google"
# Paste authorization code
```

### 2. Verify Setup
```bash
# Check if Earth Engine is installed
python -c "import ee; print(ee.__version__)"

# Check if credentials file exists
cat ~/.config/earthengine/credentials

# Test authentication
earthengine ls projects/earthengine-legacy/assets/
```

### 3. Reset Everything
```bash
# Remove old credentials
rm ~/.config/earthengine/credentials

# Fresh authentication
earthengine authenticate

# Try again in app
```

### 4. Check Google Account
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Verify account is active
3. Go to [code.earthengine.google.com](https://code.earthengine.google.com)
4. Should show "Welcome" with your account

---

## 🎯 Best Practices

### Local Development:
- Use OAuth credentials (`earthengine authenticate`)
- Upload credentials file in Option 1
- Simplest and fastest

### Streamlit Cloud:
- Use Service Account JSON
- Store in Streamlit Secrets
- More reliable for production

### Production Servers:
- Use Service Account JSON
- Store credentials securely (env vars, secrets manager)
- Never commit to git

---

## 📚 Additional Resources

- **Earth Engine Docs:** https://developers.google.com/earth-engine
- **Authentication Guide:** https://developers.google.com/earth-engine/guides/auth
- **Streamlit Secrets:** https://docs.streamlit.io/develop/concepts/connections/secrets-management
- **Google Cloud Setup:** https://console.cloud.google.com/

---

## ✅ Verification

Once authenticated, you should see:
- ✅ "✅ Connected to Google Earth Engine" message
- ✅ Green success indicator in sidebar
- ✅ Authentication method shown (OAuth, Service Account, etc.)
- ✅ Can select "🛰️ Satellite Analysis" page

---

**Version:** 2.1 (Improved Authentication)  
**Last Updated:** January 8, 2026  
**Status:** ✅ All issues fixed
