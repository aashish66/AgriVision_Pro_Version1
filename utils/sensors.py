# =============================================================================
# SATELLITE SENSORS MODULE
# =============================================================================
# This file contains configurations for different satellite sensors
# Each sensor has band mappings and cloud masking functions
# =============================================================================

import ee
import streamlit as st

# =============================================================================
# SENTINEL-2 CONFIGURATION
# =============================================================================

SENTINEL2_BANDS = {
    'blue': 'B2',      # Blue band (490nm)
    'green': 'B3',     # Green band (560nm)
    'red': 'B4',       # Red band (665nm)
    'rededge1': 'B5',  # Red Edge 1 (705nm)
    'rededge2': 'B6',  # Red Edge 2 (740nm)
    'rededge3': 'B7',  # Red Edge 3 (783nm)
    'nir': 'B8',       # Near-Infrared (842nm)
    'nir_narrow': 'B8A',  # NIR Narrow (865nm)
    'swir1': 'B11',    # Short Wave Infrared 1 (1610nm)
    'swir2': 'B12'     # Short Wave Infrared 2 (2190nm)
}


def get_sentinel2_collection(start_date, end_date, aoi, cloud_percent=20):
    """
    Get Sentinel-2 image collection with cloud filtering
    
    Steps:
    1. Load Sentinel-2 Harmonized collection (consistent across time)
    2. Filter by date range
    3. Filter by area of interest
    4. Filter by cloud percentage in metadata
    5. Apply cloud masking
    
    Parameters:
    - start_date: Start date string 'YYYY-MM-DD'
    - end_date: End date string 'YYYY-MM-DD'
    - aoi: Area of interest (ee.Geometry)
    - cloud_percent: Maximum cloud coverage percentage (default 20%)
    """
    
    # Step 1: Load the Sentinel-2 collection
    collection = ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
    
    # Step 2: Filter by date
    collection = collection.filterDate(start_date, end_date)
    
    # Step 3: Filter by location
    collection = collection.filterBounds(aoi)
    
    # Step 4: Filter by cloud percentage
    collection = collection.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloud_percent))
    
    # Step 5: Apply cloud mask to each image
    collection = collection.map(mask_sentinel2_clouds)
    
    return collection


def mask_sentinel2_clouds(image):
    """
    Remove clouds from Sentinel-2 image using QA60 band
    
    How it works:
    - QA60 band contains cloud information
    - Bit 10 = clouds, Bit 11 = cirrus
    - We set these pixels to transparent (masked)
    """
    # Get the QA60 band
    qa = image.select('QA60')
    
    # Bits 10 and 11 are clouds and cirrus
    cloud_bit = 1 << 10  # 1024
    cirrus_bit = 1 << 11  # 2048
    
    # Create mask: 0 where there are clouds
    mask = qa.bitwiseAnd(cloud_bit).eq(0).And(
           qa.bitwiseAnd(cirrus_bit).eq(0))
    
    # Apply mask and return
    return image.updateMask(mask)


# =============================================================================
# LANDSAT 8/9 CONFIGURATION
# =============================================================================

LANDSAT89_BANDS = {
    'blue': 'SR_B2',      # Blue band
    'green': 'SR_B3',     # Green band
    'red': 'SR_B4',       # Red band
    'nir': 'SR_B5',       # Near-Infrared
    'swir1': 'SR_B6',     # Short Wave Infrared 1
    'swir2': 'SR_B7'      # Short Wave Infrared 2
}


def get_landsat89_collection(start_date, end_date, aoi, cloud_percent=20):
    """
    Get Landsat 8/9 image collection with cloud filtering
    
    Steps:
    1. Load Landsat 8 and 9 collections
    2. Merge them together
    3. Filter and apply cloud mask
    """
    
    # Load Landsat 8 Surface Reflectance
    landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    
    # Load Landsat 9 Surface Reflectance
    landsat9 = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2')
    
    # Merge collections
    collection = landsat8.merge(landsat9)
    
    # Filter by date and location
    collection = collection.filterDate(start_date, end_date) \
                          .filterBounds(aoi) \
                          .filter(ee.Filter.lt('CLOUD_COVER', cloud_percent))
    
    # Apply cloud mask and scale factors
    collection = collection.map(mask_landsat_clouds) \
                          .map(apply_landsat_scale_factors)
    
    return collection


def mask_landsat_clouds(image):
    """
    Remove clouds from Landsat image using QA_PIXEL band
    
    QA_PIXEL bit values:
    - Bit 3: Cloud shadow
    - Bit 4: Cloud
    """
    qa = image.select('QA_PIXEL')
    
    # Bits for cloud and cloud shadow
    cloud_shadow = 1 << 3  # 8
    cloud = 1 << 4         # 16
    
    # Create mask
    mask = qa.bitwiseAnd(cloud_shadow).eq(0).And(
           qa.bitwiseAnd(cloud).eq(0))
    
    return image.updateMask(mask)


def apply_landsat_scale_factors(image):
    """
    Apply scale factors to Landsat data
    
    Why needed:
    - Landsat stores data as integers to save space
    - Must apply scale and offset to get real reflectance values
    """
    # Optical bands scale
    optical = image.select('SR_B.').multiply(0.0000275).add(-0.2)
    
    # Thermal bands scale (if needed)
    thermal = image.select('ST_B.*').multiply(0.00341802).add(149.0)
    
    return image.addBands(optical, None, True) \
                .addBands(thermal, None, True)


# =============================================================================
# LANDSAT 5/7 CONFIGURATION (Historical data)
# =============================================================================

LANDSAT57_BANDS = {
    'blue': 'SR_B1',
    'green': 'SR_B2',
    'red': 'SR_B3',
    'nir': 'SR_B4',
    'swir1': 'SR_B5',
    'swir2': 'SR_B7'
}


def get_landsat57_collection(start_date, end_date, aoi, cloud_percent=20):
    """
    Get historical Landsat 5/7 data (1984-2012)
    Good for long-term vegetation change analysis
    """
    
    landsat5 = ee.ImageCollection('LANDSAT/LT05/C02/T1_L2')
    landsat7 = ee.ImageCollection('LANDSAT/LE07/C02/T1_L2')
    
    collection = landsat5.merge(landsat7)
    
    collection = collection.filterDate(start_date, end_date) \
                          .filterBounds(aoi) \
                          .filter(ee.Filter.lt('CLOUD_COVER', cloud_percent)) \
                          .map(mask_landsat_clouds) \
                          .map(apply_landsat_scale_factors)
    
    return collection


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_sensor_info():
    """
    Returns information about all available sensors
    """
    return {
        'Sentinel-2': {
            'resolution': '10m',
            'bands': SENTINEL2_BANDS,
            'start_date': '2015-06-23',
            'description': 'Best for recent data with high resolution and red edge bands'
        },
        'Landsat 8/9': {
            'resolution': '30m',
            'bands': LANDSAT89_BANDS,
            'start_date': '2013-04-11',
            'description': 'Good for recent data, lower resolution but consistent'
        },
        'Landsat 5/7': {
            'resolution': '30m',
            'bands': LANDSAT57_BANDS,
            'start_date': '1984-01-01',
            'end_date': '2012-05-05',
            'description': 'Historical data for long-term change analysis'
        },
        'MODIS': {
            'resolution': '250m',
            'bands': MODIS_BANDS,
            'start_date': '2000-02-24',
            'description': 'Daily global coverage, coarser resolution, 8-day composites'
        }
    }


def get_collection_by_sensor(sensor_name, start_date, end_date, aoi, cloud_percent=20):
    """
    Get image collection based on sensor name
    
    Parameters:
    - sensor_name: 'Sentinel-2', 'Landsat 8/9', 'Landsat 5/7', or 'MODIS'
    - start_date, end_date: Date range
    - aoi: Area of interest
    - cloud_percent: Maximum cloud coverage
    """
    if sensor_name == 'Sentinel-2':
        return get_sentinel2_collection(start_date, end_date, aoi, cloud_percent)
    elif sensor_name == 'Landsat 8/9':
        return get_landsat89_collection(start_date, end_date, aoi, cloud_percent)
    elif sensor_name == 'Landsat 5/7':
        return get_landsat57_collection(start_date, end_date, aoi, cloud_percent)
    elif sensor_name == 'MODIS':
        return get_modis_collection(start_date, end_date, aoi, cloud_percent)
    else:
        raise ValueError(f"Unknown sensor: {sensor_name}")


# =============================================================================
# MODIS CONFIGURATION
# =============================================================================

MODIS_BANDS = {
    'red': 'sur_refl_b01',     # Red (620-670nm)
    'nir': 'sur_refl_b02',     # NIR (841-876nm)
    'blue': 'sur_refl_b03',    # Blue (459-479nm)
    'green': 'sur_refl_b04',   # Green (545-565nm)
    'swir1': 'sur_refl_b06',   # SWIR1 (1628-1652nm)
    'swir2': 'sur_refl_b07'    # SWIR2 (2105-2155nm)
}


def get_modis_collection(start_date, end_date, aoi, cloud_percent=20):
    """
    Get MODIS MOD09A1 image collection (8-day surface reflectance composite)
    
    Parameters:
    - start_date: Start date string 'YYYY-MM-DD'
    - end_date: End date string 'YYYY-MM-DD'
    - aoi: Area of interest (ee.Geometry)
    - cloud_percent: Not used for MODIS (kept for API consistency)
    
    Returns:
    - Scaled image collection (values 0-1)
    """
    collection = ee.ImageCollection('MODIS/061/MOD09A1')
    collection = collection.filterDate(start_date, end_date).filterBounds(aoi)
    
    # Scale MODIS reflectance values (stored as integers, need to divide by 10000)
    def scale_modis(image):
        scaled = image.select(['sur_refl_b.*']).multiply(0.0001)
        return scaled.copyProperties(image, image.propertyNames())
    
    return collection.map(scale_modis)


def mask_modis_clouds(image):
    """
    Apply basic quality filtering for MODIS
    Uses QA bands to filter low quality pixels
    """
    qa = image.select('StateQA')
    # Keep only pixels with good quality (bits 0-1 = 00)
    mask = qa.bitwiseAnd(3).eq(0)
    return image.updateMask(mask)


def get_band_names(sensor_name):
    """
    Get band mapping for a specific sensor
    """
    if sensor_name == 'Sentinel-2':
        return SENTINEL2_BANDS
    elif sensor_name == 'Landsat 8/9':
        return LANDSAT89_BANDS
    elif sensor_name == 'Landsat 5/7':
        return LANDSAT57_BANDS
    elif sensor_name == 'MODIS':
        return MODIS_BANDS
    else:
        raise ValueError(f"Unknown sensor: {sensor_name}")
