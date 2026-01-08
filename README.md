# 🌾 AgriVision Pro - Vegetation Analysis Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agrivision-pro.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-Enabled-green)

**Advanced satellite and drone imagery analysis for agricultural vegetation monitoring**

---

## 🚀 Quick Start (2 Options)

### Option 1: Use Online (Easiest)
Visit: **[https://agrivision-pro.streamlit.app](https://agrivision-pro.streamlit.app)**

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/aashish66/AgriVision_Pro.git
cd AgriVision_Pro

# Install dependencies
pip install -r requirements.txt

# Authenticate with Earth Engine
earthengine authenticate

# Run the app
streamlit run app.py
```

---

## 🔐 Authentication (Required)

To use satellite imagery features, you need to authenticate with Google Earth Engine.

### Three Methods Available:

#### 1. Cloud Project ID (Recommended)
1. Sign up at [earthengine.google.com/signup](https://earthengine.google.com/signup/)
2. Create a Google Cloud Project
3. Enter your Project ID in the app sidebar
4. Format: `ee-projectname` or `your-project-id`

#### 2. Service Account File (Production)
1. Download JSON key from [Google Cloud Console](https://console.cloud.google.com/)
2. Upload the file in the app sidebar
3. File contains your authentication credentials (like a license file)
4. Located typically at: Downloaded as `project-name-xxxxx.json`

#### 3. Local Credentials (Development)
```bash
earthengine authenticate
```
- Credentials saved automatically at:
  - Windows: `C:\Users\YourName\.config\earthengine\credentials`
  - Mac/Linux: `~/.config/earthengine/credentials`

📖 **[Complete Authentication Guide](AUTHENTICATION_GUIDE.md)** - Detailed step-by-step instructions

---

## 📖 How to Use Each Feature

### 🛰️ Satellite Imagery Analysis

1. **Define your area** using one of three methods:
   - Enter coordinates + buffer radius
   - Upload GeoJSON or Shapefile (zip)
   - Draw directly on map
2. **Set date range** (default: last 30 days)
3. **Search for images** - see all available with date and cloud %
4. **Select a specific image** or use composite
5. **Choose vegetation index** and generate map

### 🔄 Compare Two Images

1. Define your area with coordinates
2. Search for images at two different dates
3. Select images from the list
4. Generate side-by-side comparison
5. View the **difference map** (change detection)

### 📷 Upload Image Analysis (Drone/Camera)

1. Upload your RGB image (JPEG, PNG, or TIFF)
2. Choose an RGB-based vegetation index:
   - **ExG** (Excess Green) - Simple vegetation detection
   - **VARI** - Vegetation fraction estimation
   - **GLI** - Green leaf detection
3. View results with statistics

### 📊 Visitor Statistics

Track app usage with:
- Total visits
- Daily/Monthly/Yearly charts
- Data table export

---

## 🌱 Vegetation Index Guide

### Satellite Indices (require NIR band)

| Index | Formula | Best For |
|-------|---------|----------|
| **NDVI** | (NIR-Red)/(NIR+Red) | General vegetation health |
| **SAVI** | ((NIR-Red)/(NIR+Red+L))×(1+L) | Sparse vegetation, soil visible |
| **EVI** | 2.5×(NIR-Red)/(NIR+6×Red-7.5×Blue+1) | Dense vegetation, forests |
| **GNDVI** | (NIR-Green)/(NIR+Green) | Chlorophyll content |
| **NDMI** | (NIR-SWIR)/(NIR+SWIR) | Water stress detection |
| **NDRE** | (NIR-RedEdge)/(NIR+RedEdge) | Crop health (Sentinel-2 only) |

### RGB-Only Indices (for drone/camera images)

| Index | Formula | Best For |
|-------|---------|----------|
| **ExG** | 2×G - R - B | Simple vegetation detection |
| **VARI** | (G-R)/(G+R-B) | Vegetation fraction |
| **GLI** | (2×G-R-B)/(2×G+R+B) | Green leaf detection |
| **RGBVI** | (G²-R×B)/(G²+R×B) | General RGB vegetation |
| **NGRDI** | (G-R)/(G+R) | Quick assessment |
| **ExGR** | 3×G - 2.4×R - B | Vegetation vs soil |

---

## 📁 Project Structure

```
Sen2Vegetation/
├── app.py                         # Main Streamlit application
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── AgriVision_Pro_Tutorial.ipynb  # Jupyter notebook (can run app!)
├── visitor_analytics.json         # Visit tracking data
├── utils/
│   ├── __init__.py
│   ├── indices.py                 # Vegetation index calculations
│   ├── sensors.py                 # Satellite sensor configurations
│   └── image_processing.py        # Image upload & RGB processing
└── GreenSentinelReportPlus.js     # Original GEE reference script
```

---

## 🔧 Troubleshooting

### "Google Earth Engine not authenticated"

Run this command in your terminal:
```bash
earthengine authenticate
```

### "No images found for the selected date range"

- Try extending your date range
- Increase the cloud cover percentage (default is 30%)
- Check that your coordinates are correct

### "Module not found" errors

Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

---

## 📜 License

MIT License - Free to use and modify

---

**AgriVision Pro v2.0** | 🛰️ Satellite | 🚁 Drone | 📊 Analysis
