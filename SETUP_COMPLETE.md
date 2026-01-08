# 🚀 Complete Setup Guide - AgriVision Pro Streamlit App

## Overview

This guide walks you through setting up and running the AgriVision Pro Streamlit application from scratch.

**Time Required: 5-10 minutes**

---

## Step 1: Prerequisites ✅

Ensure you have installed:
- Python 3.8+ 
- Git
- pip

Check:
```bash
python3 --version
git --version
pip3 --version
```

---

## Step 2: Clone/Download Project

### Option A: Clone from GitHub
```bash
git clone https://github.com/aashish66/AgriVision_Pro.git
cd AgriVision_Pro
```

### Option B: Use Existing Project
```bash
cd /path/to/your/agrivision/project
```

---

## Step 3: Install Dependencies ✅

### Install Python packages:
```bash
pip3 install -r requirements.txt
```

This installs:
- `streamlit>=1.32.0` - Web app framework
- `google-earth-engine` - Satellite imagery API
- `geemap>=0.30.0` - Earth Engine mapping tools
- `pandas>=2.0.0` - Data analysis
- `pillow>=10.0.0` - Image processing
- And more (see requirements.txt)

**Expected time: 2-3 minutes**

---

## Step 4: Get Google Earth Engine Credentials 🔐

### Quick Method (Recommended - 60 seconds):

1. **Open terminal** and run:
   ```bash
   earthengine authenticate
   ```

2. **Browser opens automatically** - Click "Authorize"

3. **Grant permissions** to Google Earth Engine

4. **Credentials saved** to:
   ```
   ~/.config/earthengine/credentials
   ```

That's it! File is ready to use in the app.

### Alternative Method: Service Account JSON

If you prefer to use Google Cloud Service Account:

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a Project
3. Go to "Service Accounts" → Create Service Account
4. Click on account → "Keys" → "Create New Key" → "JSON"
5. JSON file downloads
6. Use this file in step 6 below

---

## Step 5: Find Your Project ID 📋

Visit: https://code.earthengine.google.com

Your Project ID is displayed at the top. It looks like:
- `ee-yourname`
- `your-project-id`
- `my-ee-project-123`

**Write it down - you'll need it in the next step!**

---

## Step 6: Start the App 🚀

```bash
cd /path/to/agrivision
streamlit run streamlit_app.py
```

This opens: http://localhost:8501

---

## Step 7: Authenticate in the App ✅

### In the sidebar:

1. **Upload Credentials File**
   - Click "📁 Upload credentials file"
   - Select your credentials file from Step 4
   - See confirmation: "✅ File loaded!"

2. **Enter Project ID**
   - Paste your Project ID from Step 5
   - Format: `ee-yourname` or similar

3. **Connect**
   - Click "🔗 Connect to Google Earth Engine"
   - Wait for connection...
   - See confirmation: "✅ Successfully authenticated!"

---

## Step 8: Start Using the App! 🎉

Once authenticated, you can:

### 🛰️ Satellite Analysis
- Select location (coordinates or map)
- Choose date range
- Calculate vegetation indices:
  - NDVI (Normalized Difference Vegetation Index)
  - SAVI (Soil-Adjusted Vegetation Index)
  - EVI (Enhanced Vegetation Index)
  - GNDVI, NDMI, NDRE
- View satellite maps
- Download results

### 🔄 Compare Images
- Compare satellite imagery over time
- View change in vegetation
- Track seasonal variations
- Multiple satellite sources

### 📷 Upload Image
- Upload drone or camera images
- Analyze with same indices
- Compare with satellite data
- Batch processing support

### 📊 Visitor Stats
- App usage analytics
- Feature popularity
- Performance metrics

### ❓ Help
- Documentation
- Troubleshooting
- FAQ

---

## Troubleshooting

### ❌ "Invalid JSON file - not a credentials file"

**Solution:**
- Make sure you uploaded the correct file from Step 4
- File should be from `earthengine authenticate` or Google Cloud Service Account
- It's a JSON file (even though no `.json` extension from earthengine)

### ❌ "Refresh token missing"

**Solution:**
```bash
earthengine authenticate
```
Then upload the newly created file.

### ❌ "Project ID not found"

**Solution:**
- Visit https://code.earthengine.google.com
- Your Project ID is visible there
- Copy it exactly as shown
- Check for typos (lowercase, dashes only)

### ❌ "Connection timeout or network error"

**Solutions:**
- Check your Internet connection
- Verify you have access to Google services
- Try again in a few moments
- Ensure your Google account has Earth Engine access

### ❌ "Successfully authenticated, but features don't work"

**Solutions:**
- Verify your Project ID is correct
- Check your Google account email is correct
- Try re-authenticating:
  ```bash
  earthengine authenticate
  ```
- Check your Earth Engine API quota

---

## Performance Optimizations ⚡

The app includes performance improvements:

- **Fast startup:** ~2-3 seconds (vs 5-6 without optimization)
- **Fast searches:** <1 second cached (vs 5-10 seconds without)
- **Memory efficient:** Minimal UI, aggressive caching
- **Optimized queries:** Minimal GEE operations

These are built-in - no additional configuration needed!

---

## Security Notes 🔒

- **Never share your credentials file**
- **Never commit credentials to Git**
- **Store credentials securely** in `~/.config/earthengine/`
- **Use Service Accounts for production** deployments
- **Rotate credentials regularly** for security

---

## Running on Streamlit Cloud

To deploy on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add secrets in app dashboard:
   ```
   EARTHENGINE_CREDENTIALS = {... paste your JSON ...}
   GEE_PROJECT_ID = "ee-yourname"
   ```
4. Click "Deploy"

See [STREAMLIT_CLOUD_SETUP.md](STREAMLIT_CLOUD_SETUP.md) for details.

---

## File Structure

```
agrivision/
├── streamlit_app.py          # Main app
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Performance config
├── utils/
│   ├── indices.py           # Vegetation index calculations
│   ├── sensors.py           # Satellite sensor configs
│   └── image_processing.py  # Image analysis functions
├── README.md                # Project overview
├── QUICK_START.md          # Quick setup
├── CREDENTIALS_SETUP.md    # Credential setup (THIS)
└── ... (other docs)
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Get credentials | `earthengine authenticate` |
| Start app | `streamlit run streamlit_app.py` |
| Install dependencies | `pip3 install -r requirements.txt` |
| Check Python | `python3 --version` |
| Find Project ID | Visit code.earthengine.google.com |

---

## Support Resources

- **Earth Engine Documentation:** https://developers.google.com/earth-engine
- **Streamlit Documentation:** https://docs.streamlit.io
- **Geemap Documentation:** https://geemap.org
- **Google Cloud Help:** https://cloud.google.com/support

---

## Next Steps

1. ✅ Complete steps 1-8 above
2. ✅ Explore the app's features
3. ✅ Read [README.md](README.md) for detailed feature documentation
4. ✅ Deploy to Streamlit Cloud if desired

---

**You're ready to analyze satellite imagery! 🛰️🌱**

Happy analyzing! 📊
