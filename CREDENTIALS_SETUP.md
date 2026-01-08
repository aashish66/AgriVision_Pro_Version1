# 🔐 Credentials Setup Guide

## Quick Start (Recommended)

### Option 1: Use `earthengine authenticate`

This is the fastest and easiest way to get started.

#### Steps:

1. **Open terminal** and run:
   ```bash
   earthengine authenticate
   ```

2. **Browser opens** automatically - click "Authorize"

3. **Grant permissions** to Google Earth Engine

4. **Credentials file created** at:
   ```
   ~/.config/earthengine/credentials
   ```

5. **Upload in app**: 
   - Open the AgriVision app
   - Upload the credentials file (no extension, it's a JSON file)
   - Enter your Project ID
   - Click "Connect to Google Earth Engine"

---

## Option 2: Google Cloud Service Account (Production)

For server deployments or production environments.

### Steps:

1. **Go to [Google Cloud Console](https://console.cloud.google.com)**

2. **Create a Service Account**:
   - Click "Create Project" or select existing
   - Go to "Service Accounts" in the left menu
   - Click "Create Service Account"
   - Fill in the details and click "Create"

3. **Create a JSON Key**:
   - Click on the service account you created
   - Go to "Keys" tab
   - Click "Add Key" → "Create New Key"
   - Select "JSON" format
   - Click "Create"
   - JSON file downloads automatically

4. **Upload in app**:
   - Open the AgriVision app
   - Upload the downloaded JSON file
   - Enter your Project ID
   - Click "Connect to Google Earth Engine"

---

## Finding Your Project ID

Your Project ID is needed to use Google Earth Engine.

### Method 1 (Easiest):
- Visit [code.earthengine.google.com](https://code.earthengine.google.com)
- Your project ID is displayed in the console
- Format: `ee-yourname` or `your-project-id`

### Method 2 (Google Cloud Console):
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Look at the top of the page for your project dropdown
- Your project ID is shown there

---

## Troubleshooting

### "Invalid JSON file"
- Make sure you uploaded a JSON file (from either method above)
- The credentials file should be plain text JSON format
- If using service account, make sure it's the downloaded JSON file

### "Credentials file missing client_id or client_secret"
- This usually means you uploaded the wrong file type
- Try again with the correct credentials file from step above

### "Project ID not found"
- Make sure your Project ID is entered correctly
- Format is usually: `ee-yourname` (all lowercase, with dashes)
- Visit code.earthengine.google.com to verify

### "Still having issues?"
1. Check your internet connection
2. Verify your Google account has Earth Engine access
3. Try creating a fresh credentials file with `earthengine authenticate`
4. Ensure your Project ID is correct (from code.earthengine.google.com)

---

## What's Next?

Once authenticated, you can:

✅ **Satellite Analysis** - Analyze vegetation indices (NDVI, SAVI, EVI, etc.)

✅ **Compare Images** - View satellite imagery over time

✅ **Upload Image** - Analyze drone or camera images

✅ **Visitor Stats** - See app usage analytics

---

## Security Notes

- Your credentials file contains sensitive authentication data
- **Never** share your credentials file with others
- **Never** commit credentials to GitHub
- For production deployments, use service accounts with limited permissions
- Rotate credentials regularly for security

---

## More Resources

- [Google Earth Engine Documentation](https://developers.google.com/earth-engine)
- [Earth Engine Python API](https://developers.google.com/earth-engine/apidocs)
- [Geemap Documentation](https://geemap.org/)
