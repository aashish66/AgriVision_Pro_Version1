"""
AgriVision Pro V3 - Download Utilities Module
==============================================
Image export and download functions.
"""

import ee
import requests
from typing import Optional, Tuple


def download_ee_image_bytes(
    image: ee.Image,
    aoi: ee.Geometry,
    scale: int,
    name: str = "export",
    max_attempts: int = 4
) -> Tuple[Optional[bytes], Optional[int]]:
    """
    Fetch an Earth Engine image as GeoTIFF bytes.

    Google Earth Engine's direct download URL rejects requests over ~48MB.
    Large areas or fine resolutions hit that limit, so this retries at
    progressively coarser scales until the request fits.

    Returns:
        (file_bytes, scale_used) on success, or (None, None) on failure.
    """
    current_scale = scale
    for _ in range(max_attempts):
        try:
            url = image.getDownloadURL({
                'name': name,
                'scale': current_scale,
                'region': aoi,
                'format': 'GEO_TIFF'
            })
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            return response.content, current_scale
        except Exception as e:
            message = str(e).lower()
            if "size" in message or "50331648" in message or "too large" in message:
                current_scale *= 2
                continue
            return None, None
    return None, None
