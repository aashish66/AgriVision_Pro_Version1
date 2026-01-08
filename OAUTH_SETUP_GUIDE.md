# 🔐 Google Earth Engine OAuth Authentication Guide

## Simple 3-Step Process

### Step 1: Click Authorization Link
- In the app sidebar, click the blue link: **"Click here to authorize with Google"**
- Your browser opens
- A Google authorization screen appears

### Step 2: Copy Authorization Code
- Click **"Authorize"** to grant permissions
- Google shows you a code (looks like: `4/0AY0e...`)
- Click **"Copy"** button to copy the code
- Or select and copy it manually

### Step 3: Submit Code in App
- Paste the code in the **"Authorization Code:"** text box
- Click the **"✅ Submit Code"** button
- Wait for confirmation: ✅ "Code accepted! Credentials ready."
- Enter your **Project ID** (from code.earthengine.google.com)
- Click **"🔗 Connect to Google Earth Engine"**
- Done! ✅ You're authenticated!

---

## Getting Your Project ID 📋

1. Visit: **https://code.earthengine.google.com**
2. Look at the top of the page
3. You'll see your **Project ID** (usually looks like: `ee-yourname`)
4. Copy it and paste in the app

---

## Complete Flow Visualization

```
┌─────────────────────────────────────────┐
│  AgriVision Pro App (Streamlit)         │
└─────────────────────────────────────────┘
              │
              │ 1. Click Authorization Link
              ▼
┌─────────────────────────────────────────┐
│  Google OAuth Browser Page              │
│  "Click here to authorize with Google"  │
└─────────────────────────────────────────┘
              │
              │ 2. User clicks "Authorize"
              ▼
┌─────────────────────────────────────────┐
│  Google Account Page                    │
│  Grant permissions to Earth Engine      │
└─────────────────────────────────────────┘
              │
              │ 3. Google shows authorization code
              │    "4/0AY0e..."
              ▼
┌─────────────────────────────────────────┐
│  User copies code                       │
└─────────────────────────────────────────┘
              │
              │ 4. Paste code in app
              │    Click "Submit Code"
              ▼
┌─────────────────────────────────────────┐
│  App exchanges code for refresh token   │
│  Backend: OAuth2 token exchange         │
└─────────────────────────────────────────┘
              │
              │ 5. Success: Code accepted
              │    Credentials ready
              ▼
┌─────────────────────────────────────────┐
│  User enters Project ID                 │
│  Clicks "Connect to Google Earth Engine"│
└─────────────────────────────────────────┘
              │
              │ 6. App connects to GEE
              │    Using refresh token
              ▼
┌─────────────────────────────────────────┐
│  ✅ Successfully Authenticated!         │
│  Ready to analyze satellite imagery     │
└─────────────────────────────────────────┘
```

---

## Troubleshooting

### ❌ "Authorization code not found"
- Make sure you clicked the link
- You should see Google's authorization page
- You need to click "Authorize"

### ❌ "Code not accepted / Invalid code"
- Make sure you copied the ENTIRE code
- Check there are no extra spaces before/after
- Make sure you copied the code, not the whole message
- Try getting a fresh code and try again

### ❌ "Code is invalid_grant"
- The code has expired (valid for ~10 minutes)
- Go back and click the authorization link again
- Get a fresh code and try again

### ❌ "Connection failed"
- Verify your **Project ID** is correct
- Visit code.earthengine.google.com to confirm your Project ID
- Make sure your Google account has Earth Engine access
- Check your internet connection

### ❌ Still not working?
1. Try a different browser (Chrome, Firefox, Safari)
2. Clear your browser cache
3. Try in incognito/private mode
4. Wait a few moments and try again
5. Check you're using the same Google account each time

---

## What Happens Behind the Scenes

1. **User clicks authorization link**
   - App shows Google's OAuth authorization URL
   - Google redirects to consent screen

2. **User authorizes**
   - Google shows permissions request
   - User clicks "Authorize"
   - Google returns authorization code

3. **User submits code**
   - App receives authorization code
   - App exchanges code for credentials using OAuth token endpoint
   - Code is converted to **refresh token** (long-lived credential)

4. **App connects to Earth Engine**
   - Using refresh token to authenticate
   - GEE confirms authentication
   - App can now access satellite imagery

5. **Analysis starts**
   - User can now use all features
   - Satellite analysis, image comparison, etc.

---

## Security Notes 🔒

✅ **Safe:**
- Authorization code is short-lived (expires in ~10 minutes)
- Only valid once - can't reuse it
- Refresh token is stored securely in Streamlit session
- No passwords are transmitted

⚠️ **Keep Secure:**
- Don't share your authorization code
- Don't share your refresh token
- Don't commit credentials to Git
- Clear cookies/cache if using shared computer

---

## Key Points to Remember

| Item | What to Do |
|------|-----------|
| **Authorization Link** | Click once, Google opens in browser |
| **Authorization Code** | Copy from Google (looks like `4/0AY0e...`) |
| **Submit Code** | Paste in app, click submit button |
| **Project ID** | Get from code.earthengine.google.com |
| **If Code Expires** | Click authorization link again |
| **If Connection Fails** | Check Project ID, try again |

---

## FAQ

**Q: How long is the authorization code valid?**
A: About 10 minutes. If it expires, click the authorization link again.

**Q: Can I use multiple Google accounts?**
A: Yes, but use the same account each time for consistent Project ID.

**Q: What if I close the browser?**
A: No problem - app session is separate. Just get a new code and try again.

**Q: Is my data safe?**
A: Yes. Only Earth Engine API credentials are used. No personal data is stored.

**Q: Can I use this on multiple devices?**
A: Yes - each device gets its own credentials through the same process.

---

## What's Next? 🚀

Once authenticated, you can:

✅ **Satellite Analysis** - Vegetation indices (NDVI, SAVI, EVI, etc.)
✅ **Compare Images** - Time-series satellite data
✅ **Upload Images** - Analyze drone/camera photos
✅ **View Analytics** - App usage stats

Enjoy analyzing! 🛰️🌱
