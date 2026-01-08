# =============================================================================
# VEGETATION INDICES MODULE
# =============================================================================
# This file contains functions to calculate various vegetation indices
# Each function explains what the index does and how it's calculated
# =============================================================================

import ee

# =============================================================================
# MULTISPECTRAL INDICES (for satellite imagery with NIR band)
# =============================================================================

def calculate_ndvi(image, nir_band, red_band):
    """
    NDVI - Normalized Difference Vegetation Index
    
    What it does:
    - Measures vegetation health and density
    - Values range from -1 to 1
    - Higher values (0.6-0.9) = dense, healthy vegetation
    - Lower values (0-0.2) = bare soil, water, or sparse vegetation
    
    Formula: (NIR - Red) / (NIR + Red)
    
    Parameters:
    - image: The satellite image
    - nir_band: Name of the Near-Infrared band
    - red_band: Name of the Red band
    """
    ndvi = image.normalizedDifference([nir_band, red_band]).rename('NDVI')
    return ndvi


def calculate_savi(image, nir_band, red_band, L=0.5):
    """
    SAVI - Soil Adjusted Vegetation Index
    
    What it does:
    - Better for sparse vegetation areas where soil is visible
    - Reduces soil brightness influence
    - Values similar to NDVI but more accurate in arid regions
    
    Formula: ((NIR - Red) / (NIR + Red + L)) * (1 + L)
    
    Parameters:
    - image: The satellite image
    - nir_band: Name of the Near-Infrared band
    - red_band: Name of the Red band
    - L: Soil brightness correction factor (0.5 is default, use 0 for high vegetation, 1 for low)
    """
    nir = image.select(nir_band)
    red = image.select(red_band)
    savi = nir.subtract(red).divide(nir.add(red).add(L)).multiply(1 + L).rename('SAVI')
    return savi


def calculate_evi(image, nir_band, red_band, blue_band):
    """
    EVI - Enhanced Vegetation Index
    
    What it does:
    - Better for dense vegetation areas
    - Reduces atmospheric effects
    - More sensitive in high biomass regions
    
    Formula: 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
    
    Parameters:
    - image: The satellite image
    - nir_band: Name of the Near-Infrared band
    - red_band: Name of the Red band
    - blue_band: Name of the Blue band
    """
    nir = image.select(nir_band)
    red = image.select(red_band)
    blue = image.select(blue_band)
    
    evi = nir.subtract(red).multiply(2.5).divide(
        nir.add(red.multiply(6)).subtract(blue.multiply(7.5)).add(1)
    ).rename('EVI')
    return evi


def calculate_gndvi(image, nir_band, green_band):
    """
    GNDVI - Green Normalized Difference Vegetation Index
    
    What it does:
    - Measures chlorophyll content in plants
    - More sensitive to chlorophyll concentration than NDVI
    - Good for assessing crop nitrogen status
    
    Formula: (NIR - Green) / (NIR + Green)
    """
    gndvi = image.normalizedDifference([nir_band, green_band]).rename('GNDVI')
    return gndvi


def calculate_ndmi(image, nir_band, swir_band):
    """
    NDMI - Normalized Difference Moisture Index
    
    What it does:
    - Measures vegetation water content
    - Good for drought monitoring
    - Higher values = more moisture
    
    Formula: (NIR - SWIR) / (NIR + SWIR)
    """
    ndmi = image.normalizedDifference([nir_band, swir_band]).rename('NDMI')
    return ndmi


def calculate_ndre(image, nir_band, rededge_band):
    """
    NDRE - Normalized Difference Red Edge Index
    
    What it does:
    - Uses red edge band (only available in Sentinel-2)
    - More sensitive to chlorophyll than NDVI
    - Better for monitoring crop health and nitrogen
    
    Formula: (NIR - RedEdge) / (NIR + RedEdge)
    """
    ndre = image.normalizedDifference([nir_band, rededge_band]).rename('NDRE')
    return ndre


# =============================================================================
# RGB-ONLY INDICES (for drone/camera images with only Red, Green, Blue)
# =============================================================================

def calculate_exg(image, red_band='R', green_band='G', blue_band='B'):
    """
    ExG - Excess Green Index
    
    What it does:
    - Simple index using only RGB bands
    - Good for separating vegetation from soil/background
    - Positive values = vegetation, negative = non-vegetation
    
    Formula: 2*Green - Red - Blue
    
    Use case: Drone images, regular cameras
    """
    r = image.select(red_band)
    g = image.select(green_band)
    b = image.select(blue_band)
    
    exg = g.multiply(2).subtract(r).subtract(b).rename('ExG')
    return exg


def calculate_exr(image, red_band='R', green_band='G'):
    """
    ExR - Excess Red Index
    
    What it does:
    - Highlights red features (soil, dead vegetation)
    - Used with ExG to create ExGR
    
    Formula: 1.4*Red - Green
    """
    r = image.select(red_band)
    g = image.select(green_band)
    
    exr = r.multiply(1.4).subtract(g).rename('ExR')
    return exr


def calculate_exgr(image, red_band='R', green_band='G', blue_band='B'):
    """
    ExGR - Excess Green minus Excess Red
    
    What it does:
    - Combines ExG and ExR
    - Better separation of vegetation from soil
    - Positive = green vegetation, negative = soil/dead plants
    
    Formula: ExG - ExR = 2*Green - Red - Blue - (1.4*Red - Green)
            = 3*Green - 2.4*Red - Blue
    """
    r = image.select(red_band)
    g = image.select(green_band)
    b = image.select(blue_band)
    
    exgr = g.multiply(3).subtract(r.multiply(2.4)).subtract(b).rename('ExGR')
    return exgr


def calculate_vari(image, red_band='R', green_band='G', blue_band='B'):
    """
    VARI - Visible Atmospherically Resistant Index
    
    What it does:
    - Works with visible bands only
    - Reduces atmospheric effects
    - Good for estimating vegetation fraction
    
    Formula: (Green - Red) / (Green + Red - Blue)
    """
    r = image.select(red_band)
    g = image.select(green_band)
    b = image.select(blue_band)
    
    vari = g.subtract(r).divide(g.add(r).subtract(b)).rename('VARI')
    return vari


def calculate_gli(image, red_band='R', green_band='G', blue_band='B'):
    """
    GLI - Green Leaf Index
    
    What it does:
    - Simple RGB-based vegetation index
    - Good for detecting green leaves
    - Values typically range from -1 to 1
    
    Formula: (2*Green - Red - Blue) / (2*Green + Red + Blue)
    """
    r = image.select(red_band)
    g = image.select(green_band)
    b = image.select(blue_band)
    
    gli = g.multiply(2).subtract(r).subtract(b).divide(
        g.multiply(2).add(r).add(b)
    ).rename('GLI')
    return gli


def calculate_rgbvi(image, red_band='R', green_band='G', blue_band='B'):
    """
    RGBVI - Red-Green-Blue Vegetation Index
    
    What it does:
    - Uses relationship between RGB channels
    - Good for general vegetation mapping with RGB cameras
    
    Formula: (Green² - Red*Blue) / (Green² + Red*Blue)
    """
    r = image.select(red_band)
    g = image.select(green_band)
    b = image.select(blue_band)
    
    g_squared = g.multiply(g)
    r_times_b = r.multiply(b)
    
    rgbvi = g_squared.subtract(r_times_b).divide(
        g_squared.add(r_times_b)
    ).rename('RGBVI')
    return rgbvi


def calculate_ngrdi(image, red_band='R', green_band='G'):
    """
    NGRDI - Normalized Green-Red Difference Index
    
    What it does:
    - Simple ratio using only green and red
    - Quick vegetation assessment
    - Similar to NDVI but for visible spectrum
    
    Formula: (Green - Red) / (Green + Red)
    """
    r = image.select(red_band)
    g = image.select(green_band)
    
    ngrdi = g.subtract(r).divide(g.add(r)).rename('NGRDI')
    return ngrdi


# =============================================================================
# HELPER FUNCTION - Get all available indices
# =============================================================================

def get_available_indices():
    """
    Returns a dictionary of all available indices organized by type
    """
    return {
        'multispectral': {
            'NDVI': 'Normalized Difference Vegetation Index - General vegetation health',
            'SAVI': 'Soil Adjusted Vegetation Index - Sparse vegetation areas',
            'EVI': 'Enhanced Vegetation Index - Dense vegetation',
            'GNDVI': 'Green NDVI - Chlorophyll content',
            'NDMI': 'Normalized Difference Moisture Index - Water content',
            'NDRE': 'Normalized Difference Red Edge - Crop health (Sentinel-2 only)'
        },
        'rgb_only': {
            'ExG': 'Excess Green - Simple vegetation detection',
            'ExR': 'Excess Red - Soil/dead vegetation',
            'ExGR': 'Excess Green-Red - Vegetation vs soil',
            'VARI': 'Visible Atmospherically Resistant - Vegetation fraction',
            'GLI': 'Green Leaf Index - Green leaf detection',
            'RGBVI': 'RGB Vegetation Index - General RGB vegetation',
            'NGRDI': 'Normalized Green-Red Difference - Quick assessment'
        }
    }
