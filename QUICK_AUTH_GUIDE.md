# 🚀 Quick Start - 4 Minutes to Analyzing Satellite Images

## Your Credentials Format ✅

Your credentials file with this format is **now fully supported**:
```json
{
  "refresh_token": "1//06uh90XQAF2EUQCgYIARAAGAYSNwF...",
  "redirect_uri": "http://localhost:8085",
  "scopes": [...]
}
```

---

## 4-Minute Setup

### ⏱️ Minute 1: Prepare
- Locate your credentials file: `~/.config/earthengine/credentials`
- Or run to get a fresh one: `earthengine authenticate`

### ⏱️ Minute 2: Get Project ID
- Visit: https://code.earthengine.google.com
- Look at the top - you'll see your Project ID
- Examples: `ee-john-doe`, `vegetation-analysis`, `ee-yourname`

### ⏱️ Minute 3: Start App
```bash
streamlit run streamlit_app.py
```
Browser opens at: http://localhost:8501

### ⏱️ Minute 4: Authenticate
In the sidebar:
1. Click "📁 Select credentials file" button
2. Select your credentials file
3. See: "✅ Refresh token found!" and "✅ File loaded!"
4. Paste Project ID in the "Project ID" field
5. Click "🔗 Connect to Google Earth Engine"
6. See: "✅ Successfully authenticated!" + 🎉

**Done!** Start analyzing satellite imagery! 🛰️

---

## What You Can Do Now

✅ **Satellite Analysis**
- Select any location (coordinates or map)
- Choose date range
- Calculate vegetation indices: NDVI, SAVI, EVI, GNDVI, NDMI, NDRE
- View beautiful satellite maps

✅ **Compare Images**
- View satellite imagery over time
- Track vegetation changes
- Multiple satellite sources (Sentinel-2, Landsat, MODIS)

✅ **Upload Images**
- Analyze drone or camera photos
- Same vegetation indices
- Compare with satellite data

✅ **View Analytics**
- App usage statistics
- Feature popularity

---

## If File Upload Fails

### Issue: "❌ Invalid JSON file"
**Solution:** Make sure it's the right file
```bash
# Check file content
cat ~/.config/earthengine/credentials

# Should contain "refresh_token"
# If not, get a fresh one:
earthengine authenticate
```

### Issue: "❌ Connection failed"
**Solution:** Check your Project ID
```
1. Visit: https://code.earthengine.google.com
2. Copy the Project ID from the top
3. Paste exactly as shown (no typos!)
4. Format is usually: ee-yourname
```

### Issue: "❌ Refresh token missing"
**Solution:** File doesn't have refresh_token
```bash
# Get fresh credentials
earthengine authenticate

# Then upload the new file in the app
```

---

## Command Reference

| Task | Command |
|------|---------|
| Start app | `streamlit run streamlit_app.py` |
| Get credentials | `earthengine authenticate` |
| Check file | `cat ~/.config/earthengine/credentials` |
| Find Project ID | Visit code.earthengine.google.com |

---

## Your Credentials File Should Have

✅ `"refresh_token"` - Long lived credential
✅ `"redirect_uri"` - OAuth redirect URL
✅ `"scopes"` - Permissions list

It should look like:
```json
{
  "redirect_uri": "http://localhost:8085",
  "refresh_token": "1//06uh90XQAF2EUQCgYIARAAGAYSNwF...",
  "scopes": ["https://www.googleapis.com/auth/earthengine", ...]
}
```

---

## Project ID Format

Common examples:
- `ee-aashish-gautam` (with hyphens)
- `ee-john` (simple)
- `vegetation-analysis` (custom name)
- `agri-monitoring-prod` (production)

**Get the exact one from:** https://code.earthengine.google.com

---

## File Locations

| Item | Location |
|------|----------|
| **Credentials File** | `~/.config/earthengine/credentials` |
| **App File** | `./streamlit_app.py` |
| **Project ID** | code.earthengine.google.com (top of page) |

---

## Success Indicators

You'll know it's working when you see:

1. ✅ "Refresh token found!" - File is correct
2. ✅ "File loaded!" - JSON parsed successfully  
3. ✅ "Successfully authenticated!" - GEE connection established
4. 🎉 Balloons appear - You're authenticated!
5. 🛰️ "Satellite Analysis" page loads - Ready to use!

---

## Troubleshooting Checklist

- [ ] Credentials file exists: `ls ~/.config/earthengine/credentials`
- [ ] Contains refresh_token: `grep refresh_token ~/.config/earthengine/credentials`
- [ ] Project ID copied: From code.earthengine.google.com
- [ ] No typos in Project ID
- [ ] Internet connection working
- [ ] Google account has Earth Engine access

---

## Need More Help?

- Read: [CREDENTIALS_FILE_UPLOAD_FIXED.md](CREDENTIALS_FILE_UPLOAD_FIXED.md) - Complete guide
- Check: App's "❓ Credentials Help" section (expander in sidebar)
- Run: `earthengine authenticate` again for fresh credentials

---

## You're Ready! 🎉

Start the app now:
```bash
streamlit run streamlit_app.py
```

Then follow the 4-step process above.

**Happy analyzing!** 🛰️🌾📊
