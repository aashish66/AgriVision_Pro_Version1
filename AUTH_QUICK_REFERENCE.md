# 🔐 Authentication Quick Reference

## Three Authentication Methods (Choose One)

### ✅ Method 1: Upload Credentials File (Easiest)
```bash
1. Terminal: earthengine authenticate
2. App: Enter Project ID
3. App: Upload file from ~/.config/earthengine/credentials
4. App: Click "Connect with Uploaded Credentials"
```
**Best for:** Local development
**Time:** 2 minutes

---

### ✅ Method 2: OAuth Authorization Code (Cloud-Friendly)
```
1. App: Enter Project ID
2. App: Click "🌐 Sign in with Google"
3. Browser: Complete Google sign-in
4. App: Paste authorization code in text field
5. App: Press Enter
```
**Best for:** Streamlit Cloud, no file uploads
**Time:** 1 minute

---

### ✅ Method 3: Service Account JSON (Production)
```bash
1. Cloud: Go to https://console.cloud.google.com/
2. Cloud: Create Service Account + download JSON
3. App: Upload JSON file
4. App: Click "Connect with Uploaded Credentials"
```
**Best for:** Servers, automation, production
**Time:** 5 minutes

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| "missing client_id or client_secret" | Wrong credentials file | Use Method 1: `earthengine authenticate` first |
| "don't know where to add code" | No code input field visible | NEW: Click "🌐 Sign in with Google" then paste in text box |
| "Failed to initialize" | Bad credentials | Try a different method |
| "Invalid file: not JSON" | Corrupted file | Download/re-generate credentials |

---

## Your Project ID

Find at: [code.earthengine.google.com](https://code.earthengine.google.com)

Format: `ee-yourname` or `your-project-id`

---

## 🚀 Quick Start (30 seconds)

```bash
# Terminal:
earthengine authenticate

# Then in Streamlit app:
1. Enter Project ID
2. Upload ~/.config/earthengine/credentials
3. Click Connect
4. Done! ✅
```

---

For full troubleshooting: See `AUTHENTICATION_TROUBLESHOOTING.md`
