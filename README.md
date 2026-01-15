# 🌾 AgriVision Pro

**Satellite-Powered Vegetation Analysis Platform**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agrivision-pro.streamlit.app/)
[![Google Earth Engine](https://img.shields.io/badge/Powered%20by-Google%20Earth%20Engine-4285F4.svg)](https://earthengine.google.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)

> Analyze crop health, monitor vegetation dynamics, and track agricultural changes using satellite imagery from multiple sensors.

🚀 **[Launch App](https://agrivision-pro.streamlit.app/)** | 📖 **[GEE Setup Guide](GEE_SETUP.md)**

---

## ✨ Features

### 🛰️ Multi-Sensor Support
| Sensor | Resolution | Best For |
|--------|------------|----------|
| **Sentinel-2** | 10m | High-detail crop monitoring |
| **Landsat 8/9** | 30m | Recent historical analysis |
| **Landsat 5/7** | 30m | Long-term trends (1984+) |
| **MODIS** | 250-500m | Large-scale regional studies |

### 📊 Vegetation Indices
- **NDVI** - Normalized Difference Vegetation Index
- **EVI** - Enhanced Vegetation Index
- **SAVI** - Soil Adjusted Vegetation Index
- **NDWI** - Normalized Difference Water Index
- **NDMI** - Normalized Difference Moisture Index
- **GNDVI** - Green NDVI
- **NBR** - Normalized Burn Ratio

### 🗺️ Analysis Tools
- **Single Image Analysis** - Analyze vegetation at a specific date
- **Time Series** - Track vegetation changes over months/years
- **Image Comparison** - Compare two dates side-by-side
- **Temporal Animation** - Visualize change over time
- **GeoTIFF Export** - Download analysis results

---

## 🚀 Quick Start

### Use the Live App (Recommended)

1. **Open**: [https://agrivision-pro.streamlit.app/](https://agrivision-pro.streamlit.app/)

2. **Setup GEE** (first time only): Follow the **[GEE Setup Guide](GEE_SETUP.md)**

3. **Upload credentials** and enter your Project ID

4. **Start analyzing!**

### Run Locally

```bash
# Clone repository
git clone https://github.com/aashish66/AgriVision_Pro_Version1.git
cd AgriVision_Pro_Version1

# Install dependencies
pip install -r requirements.txt

# Authenticate with GEE (first time only)
earthengine authenticate

# Run the app
streamlit run streamlit_app.py
```

---

## 🔐 Authentication

AgriVision Pro requires Google Earth Engine access. Choose your setup path:

| Method | Best For | Guide |
|--------|----------|-------|
| **Upload Credentials** | Streamlit Cloud users | [GEE Setup Guide](GEE_SETUP.md) |
| **Local Authentication** | Local development | `earthengine authenticate` |
| **Service Account** | Deployment/Production | See Deployment section |

📖 **Complete setup instructions**: **[GEE_SETUP.md](GEE_SETUP.md)**

---

## 📁 Project Structure

```
AgriVision_Pro/
├── streamlit_app.py          # Main application entry point
├── requirements.txt          # Python dependencies
├── core/                     # Core processing modules
│   ├── satellite_data.py     # Satellite data fetching
│   ├── vegetation_indices.py # Index calculations
│   ├── map_utils.py          # Map visualization
│   └── download_utils.py     # Export functionality
├── app_components/           # UI components
│   ├── auth_component.py     # GEE authentication
│   ├── aoi_component.py      # Area of Interest selection
│   └── time_series.py        # Time series charts
└── .streamlit/
    └── config.toml           # Streamlit configuration
```

---

## ☁️ Deployment on Streamlit Cloud

1. **Push to GitHub**

2. **Connect to Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)

3. **Add secrets** (optional - for service account):
   ```toml
   [gee_service_account]
   type = "service_account"
   project_id = "your-project-id"
   private_key_id = "..."
   private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   client_email = "...@....iam.gserviceaccount.com"
   # ... rest of service account JSON
   ```

---

## 📋 Requirements

- Python 3.8+
- Google Earth Engine account ([Sign up FREE](https://earthengine.google.com/signup/))
- Internet connection

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/aashish66/AgriVision_Pro_Version1/issues)
- **GEE Help**: [GEE Setup Guide](GEE_SETUP.md)

---

Made with 🌱 for agricultural research and precision farming
