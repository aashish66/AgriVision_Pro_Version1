# 🛰️ Google Earth Engine Setup Guide

Complete step-by-step guide to set up Google Earth Engine (GEE) authentication for AgriVision Pro.

---

## 📋 Prerequisites

Before you begin, you'll need:
- A Google account (Gmail)
- Python installed on your computer
- Internet connection

---

## Step 1: Sign Up for Google Earth Engine

1. **Visit the signup page**: [https://earthengine.google.com/signup/](https://earthengine.google.com/signup/)

2. **Click "Get Started"** and sign in with your Google account

3. **Complete the registration form**:
   - Select your intended use (Research/Education recommended)
   - Fill in your organization details
   - Accept the terms of service

4. **Wait for approval**: Usually instant for educational/research use

> **Note**: GEE is FREE for research, education, and non-commercial use!

---

## Step 2: Install Earth Engine API

Open your terminal or command prompt:

### Windows
```bash
# Open Command Prompt (search "cmd" in Start menu)
pip install earthengine-api
```

### Mac/Linux
```bash
# Open Terminal
pip install earthengine-api
```

---

## Step 3: Authenticate with Google Earth Engine

Run this command in your terminal:

```bash
earthengine authenticate
```

### What happens next:

1. **A browser window opens** (or a URL is displayed to copy/paste)

2. **Sign in with Google**: Use the SAME account you registered with GEE

3. **Grant permissions**: Allow the Earth Engine Authenticator to access your account

4. **Authorization code**: Copy the code from the browser back to terminal (if prompted)

5. **Success!** Credentials are now saved to your computer

---

## Step 4: Find Your Credentials File

Your credentials are automatically saved at:

| Operating System | Credentials Location |
|-----------------|---------------------|
| **Windows** | `C:\Users\[YOUR_USERNAME]\.config\earthengine\credentials` |
| **Mac** | `~/.config/earthengine/credentials` |
| **Linux** | `~/.config/earthengine/credentials` |

> **Important**: The file is named exactly `credentials` with NO file extension (not .json, not .txt)

### To navigate there on Windows:
1. Open File Explorer
2. Type `%USERPROFILE%\.config\earthengine` in the address bar
3. Press Enter

---

## Step 5: Get Your GEE Project ID

1. **Go to Google Cloud Console**: [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. **Select or create a project** from the dropdown at the top

3. **Copy your Project ID** (e.g., `ee-yourusername` or `my-gee-project-12345`)

4. **Enable Earth Engine API** (if not already enabled):
   - Go to "APIs & Services" → "Library"
   - Search for "Earth Engine"
   - Click "Enable"

---

## 🌐 Using AgriVision Pro on Streamlit Cloud

When using the live app at [https://agrivision-pro.streamlit.app/](https://agrivision-pro.streamlit.app/):

### Option A: Upload Credentials File (Recommended)
1. Click **"Upload Credentials File"** in the authentication sidebar
2. Navigate to your credentials file location (Step 4 above)
3. Select the `credentials` file
4. Enter your GEE Project ID
5. Click **"Initialize GEE"**

### Option B: Manual Entry
1. Open your credentials file in a text editor
2. Copy the entire contents (it's JSON format)
3. Paste into the credentials text area in the app
4. Enter your GEE Project ID
5. Click **"Initialize GEE"**

---

## 🖥️ Running Locally

When running locally, credentials are auto-detected:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

The app will automatically find credentials at `~/.config/earthengine/credentials`

---

## 🔧 Troubleshooting

### "invalid_client" Error
- Re-run `earthengine authenticate` to get fresh credentials
- Make sure you're using the correct Google account

### "Project not found" Error
- Verify your Project ID in Google Cloud Console
- Ensure Earth Engine API is enabled for your project

### Credentials file not found
- Run `earthengine authenticate` again
- Check the file location matches your OS (Step 4)

### Authentication expired
- Credentials can expire after several months
- Re-run `earthengine authenticate` to refresh

---

## 📞 Need Help?

- **GEE Documentation**: [https://developers.google.com/earth-engine](https://developers.google.com/earth-engine)
- **GEE Signup Issues**: [https://earthengine.google.com/faq/](https://earthengine.google.com/faq/)
- **App Issues**: Open an issue on [GitHub](https://github.com/aashish66/AgriVision_Pro_Version1/issues)

---

⬅️ [Back to Main README](README.md)
