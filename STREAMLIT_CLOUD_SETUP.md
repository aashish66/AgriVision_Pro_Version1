# Streamlit Cloud Setup Guide for AgriVision Pro

## Issue: Authentication Not Working on Streamlit Cloud

The app authentication is failing on Streamlit Cloud because:
1. Local credentials files don't exist on cloud servers
2. Username/password auth is deprecated by Google
3. Service Account credentials need to be added to Streamlit secrets

## Solution: Add GEE Service Account to Streamlit Secrets

### Step 1: Create GEE Service Account (if you haven't already)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your Earth Engine project
3. Go to **IAM & Admin** → **Service Accounts**
4. Click **Create Service Account**
5. Name it: `agrivision-pro-service-account`
6. Grant role: **Earth Engine Resource Admin**
7. Click **Done**
8. Click on the service account → **Keys** tab
9. Click **Add Key** → **Create New Key** → **JSON**
10. Download the JSON file (e.g., `agrivision-credentials.json`)

### Step 2: Register Service Account with Earth Engine

**Important:** You must register the service account email with your Earth Engine project.

```bash
# On your local machine, run:
earthengine authenticate

# Then register the service account:
earthengine acl set YOUR_ASSET_ROOT serviceAccountEmail@project.iam.gserviceaccount.com:R
```

Or use this Python script:
```python
import ee
ee.Authenticate()
ee.Initialize()

# Replace with your service account email from the JSON file
service_account_email = "agrivision-pro-service-account@your-project.iam.gserviceaccount.com"

# This grants the service account access to your Earth Engine assets
print(f"Register this email: {service_account_email}")
```

### Step 3: Add Credentials to Streamlit Cloud

1. Go to your app on Streamlit Cloud: https://agrivisionpro-vjndihjpqdcbfid5qsc3yp.streamlit.app/
2. Click **"Manage app"** (bottom right) or go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
3. Find your app **AgriVision_Pro**
4. Click **⚙️ Settings** → **Secrets**
5. Add this in the secrets editor:

```toml
[gee_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYour-Private-Key-Here\n-----END PRIVATE KEY-----\n"
client_email = "agrivision-pro-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

**How to get these values:**
- Open the JSON file you downloaded in Step 1
- Copy each field exactly as it appears
- For `private_key`, keep the `\n` characters (they're important!)

**Example format:**
```toml
[gee_service_account]
type = "service_account"
project_id = "ee-project-12345"
private_key_id = "abc123def456..."
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...\n-----END PRIVATE KEY-----\n"
client_email = "agrivision-service@ee-project-12345.iam.gserviceaccount.com"
client_id = "123456789012345678901"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/agrivision-service%40ee-project-12345.iam.gserviceaccount.com"
```

### Step 4: Save and Restart

1. Click **Save** in the Streamlit secrets editor
2. Your app will automatically restart
3. The app should now authenticate automatically using the service account
4. You won't see any authentication UI - it will just work!

---

## Alternative: Use Project ID (Simpler but Less Secure)

If you have issues with service accounts, you can use project-based authentication:

1. In Streamlit Secrets, add:
```toml
[gee]
project_id = "your-earth-engine-project-id"
```

2. Make sure your Earth Engine project allows public access or you've authenticated locally

**Note:** This requires your local machine to have authenticated with this project at least once.

---

## Troubleshooting

### "Invalid credentials" error
- Make sure you copied the entire `private_key` including `\n` characters
- Verify the service account email is registered with Earth Engine
- Check that the project_id matches your Earth Engine project

### App still slow
- First load after deployment takes 2-3 minutes (cold start)
- Subsequent loads should be fast (10-20 seconds)
- Image searches may take 5-15 seconds depending on date range

### Authentication not working
1. Check Streamlit logs: Click "Manage app" → "Logs"
2. Look for GEE initialization errors
3. Verify service account has Earth Engine access
4. Make sure secrets are formatted correctly (TOML format)

---

## Expected Performance After Fix

- **Cold start:** 2-3 minutes (first time)
- **Warm start:** 10-20 seconds
- **Image search:** 5-15 seconds
- **Map generation:** 5-10 seconds
- **Index calculation:** 3-5 seconds (cached after first time)

All operations should be significantly faster once authentication is working!
