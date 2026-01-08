# Google Earth Engine Authentication Guide

This guide explains how to authenticate with Google Earth Engine (GEE) to use AgriVision Pro.

## 🎯 Quick Start

AgriVision Pro supports **3 authentication methods**:

1. **Cloud Project ID** (Recommended for most users)
2. **Service Account File** (Best for production/sharing)
3. **Local Credentials** (For developers)

---

## Method 1: Cloud Project ID (Recommended)

### What You Need
- A Google Earth Engine account
- A registered Google Cloud Project

### Step-by-Step Instructions

#### 1. Sign Up for Earth Engine
- Go to [https://earthengine.google.com/signup/](https://earthengine.google.com/signup/)
- Sign in with your Google account
- Fill out the registration form
- Wait for approval (usually within 24 hours)

#### 2. Create a Cloud Project
- Go to [https://console.cloud.google.com/](https://console.cloud.google.com/)
- Click "Select a project" → "New Project"
- Enter a project name (e.g., "my-earth-engine-project")
- Click "Create"

#### 3. Register Project with Earth Engine
- Go to [https://code.earthengine.google.com/](https://code.earthengine.google.com/)
- You'll be prompted to register your project
- Select your newly created project
- Complete the registration

#### 4. Get Your Project ID
Your Project ID has one of these formats:
- `ee-yourprojectname` (newer format)
- `your-project-id-12345` (older format)

Find it at: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- Look at the top navigation bar
- Or go to Project Settings

#### 5. Use in AgriVision Pro
1. Open the app
2. In the sidebar, select "📝 Cloud Project ID"
3. Enter your Project ID
4. Click "🔗 Connect to Earth Engine"
5. ✅ You're authenticated!

---

## Method 2: Service Account File (Production)

### What You Need
- A Google Cloud Project (see Method 1)
- A Service Account with Earth Engine access

### Step-by-Step Instructions

#### 1. Create a Service Account
- Go to [https://console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- Select your project
- Click "Create Service Account"
- Enter a name (e.g., "earth-engine-service")
- Click "Create and Continue"

#### 2. Grant Permissions
- Add role: "Earth Engine Resource Admin"
- Or at minimum: "Earth Engine Resource Viewer"
- Click "Continue" → "Done"

#### 3. Create and Download Key
- Click on your new service account
- Go to "Keys" tab
- Click "Add Key" → "Create new key"
- Choose "JSON" format
- Click "Create"
- **Save the downloaded file securely!**

The file will be named something like:
```
your-project-name-abc123def456.json
```

#### 4. Use in AgriVision Pro
1. Open the app
2. In the sidebar, select "📁 Service Account File (.json)"
3. Click "Browse files" and select your JSON file
4. You'll see: "✅ File loaded: [email]"
5. Click "🔗 Connect to Earth Engine"
6. ✅ You're authenticated!

**Security Note:** Your credentials are processed securely and never stored by the app.

---

## Method 3: Local Credentials (Development)

### What You Need
- Python and Earth Engine API installed locally
- Terminal/Command Prompt access

### Step-by-Step Instructions

#### 1. Install Earth Engine API
```bash
pip install earthengine-api
```

#### 2. Authenticate in Terminal
```bash
earthengine authenticate
```

This will:
- Open a browser window
- Ask you to sign in with Google
- Give you a code to paste back in terminal
- Save credentials to your computer

**Credentials are saved at:**
- **Windows**: `C:\Users\YourName\.config\earthengine\credentials`
- **Mac/Linux**: `~/.config/earthengine/credentials`

#### 3. Use in AgriVision Pro
- Just open the app locally!
- The app will automatically detect and use your saved credentials
- You'll see: "✅ Using local credentials"

---

## 🆘 Troubleshooting

### "Authentication failed" Error

**For Cloud Project ID:**
- ✅ Make sure Project ID is correct (no spaces)
- ✅ Project must be registered with Earth Engine
- ✅ You must have access to the project
- ✅ Try format: `ee-projectname` or full project ID

**For Service Account:**
- ✅ Service account must have Earth Engine permissions
- ✅ JSON file must be valid (check it's not corrupted)
- ✅ Service account must be enabled in Cloud Console

**For Local Credentials:**
- ✅ Run `earthengine authenticate` first
- ✅ Make sure you're using the same Google account

### "No images found" Error
- ✅ First make sure you're authenticated
- ✅ Try increasing cloud cover percentage
- ✅ Expand date range
- ✅ Check your area of interest is valid

### App is Slow
- ✅ Results are cached - second searches are faster
- ✅ Try smaller date ranges (< 3 months)
- ✅ Reduce area of interest size
- ✅ Refresh page if using for extended period

### File Upload Issues
- ✅ Make sure file is valid JSON format
- ✅ File should be service account key (has "private_key" field)
- ✅ File size should be < 10KB
- ✅ Don't modify the JSON file after downloading

---

## 📋 Authentication File Locations

### Service Account File (JSON)
Downloaded from Google Cloud Console, contains:
```json
{
  "type": "service_account",
  "project_id": "your-project",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...",
  "client_email": "service-account@project.iam.gserviceaccount.com",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  ...
}
```

### Local Credentials File
Created by `earthengine authenticate`:
- **Windows**: `%USERPROFILE%\.config\earthengine\credentials`
- **Mac/Linux**: `~/.config/earthengine/credentials`

---

## 🔐 Security Best Practices

1. **Never share your service account JSON file**
2. **Don't commit credentials to GitHub**
3. **Rotate service account keys regularly**
4. **Use project-level permissions (not organization-wide)**
5. **Delete unused service accounts**
6. **Keep your credentials file secure**

---

## 🚀 Quick Reference

| Method | Best For | Setup Time | Security |
|--------|----------|------------|----------|
| **Cloud Project** | Individual users | 5 min | ⭐⭐⭐ |
| **Service Account** | Production/Teams | 10 min | ⭐⭐⭐⭐⭐ |
| **Local Credentials** | Development | 2 min | ⭐⭐⭐⭐ |

---

## 📞 Need More Help?

- **Earth Engine Docs**: [developers.google.com/earth-engine](https://developers.google.com/earth-engine/)
- **Sign Up**: [earthengine.google.com/signup](https://earthengine.google.com/signup/)
- **Cloud Console**: [console.cloud.google.com](https://console.cloud.google.com/)
- **Community Forum**: [groups.google.com/g/google-earth-engine-developers](https://groups.google.com/g/google-earth-engine-developers)

---

## ✅ Authentication Checklist

Before using AgriVision Pro, make sure you have:

- [ ] Registered for Google Earth Engine
- [ ] Created a Google Cloud Project
- [ ] Registered project with Earth Engine
- [ ] Obtained Project ID or Service Account file
- [ ] Successfully authenticated in the app
- [ ] Tested by searching for satellite images

**You're ready to go!** 🎉
