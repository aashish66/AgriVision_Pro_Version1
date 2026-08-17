# 🌾 AgriVision Pro

**Satellite-Powered Vegetation Analysis Platform**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agrivision-pro.streamlit.app/)
[![Google Earth Engine](https://img.shields.io/badge/Powered%20by-Google%20Earth%20Engine-4285F4.svg)](https://earthengine.google.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)

> Analyze crop health, monitor vegetation dynamics, and track agricultural changes using satellite imagery from multiple sensors.

🚀 **[Launch App](https://agrivision-pro.streamlit.app/)** — no login or setup needed, just open and go.

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

Just **[open the app](https://agrivision-pro.streamlit.app/)** and start
analyzing — no account, login, or credential upload required. Satellite
access is pre-configured on the backend.

### Run Locally

```bash
# Clone repository
git clone https://github.com/aashish66/AgriVision_Pro_Version1.git
cd AgriVision_Pro_Version1

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

Locally, the app connects to Earth Engine using whichever credentials it
finds first: a service account in `.streamlit/secrets.toml`, or a prior
`earthengine authenticate` session on your machine.

> Setting up the backend (Earth Engine service account, visitor tracking,
> weekly summary email) is an admin task, not something end users need to
> do — see **[ADMIN_SETUP.md](ADMIN_SETUP.md)**.

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
│   ├── auth_component.py     # Earth Engine init (service account, no user login)
│   ├── sheets_utils.py       # Persistent visitor count & contact form (Google Sheets)
│   ├── contact_form.py       # Optional landing-page contact form
│   ├── visitor_stats.py      # Visitor counter display
│   ├── aoi_component.py      # Area of Interest selection
│   └── time_series.py        # Time series charts
├── scripts/
│   └── send_weekly_summary.py  # Weekly email summary (run by GitHub Actions)
├── .github/workflows/
│   ├── keep-alive.yml        # Pings the app so it doesn't sleep
│   └── weekly-summary.yml    # Sends the weekly summary email
└── .streamlit/
    └── config.toml           # Streamlit configuration
```

Admin/backend setup (Earth Engine service account, Google Sheet, weekly
email) is documented in **[ADMIN_SETUP.md](ADMIN_SETUP.md)** — end users
never see or need any of it.

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
- **Admin/backend setup**: [ADMIN_SETUP.md](ADMIN_SETUP.md)
- **GEE account signup**: [GEE Setup Guide](GEE_SETUP.md)

---

Made with 🌱 for agricultural research and precision farming
