# =============================================================================
# IMAGE PROCESSING MODULE
# =============================================================================
# This file handles user-uploaded images (drone, camera, etc.)
# Works with RGB and multispectral images
# =============================================================================

import numpy as np
from PIL import Image
import io
import streamlit as st

# =============================================================================
# RGB IMAGE PROCESSING (for drone/camera images)
# =============================================================================

@st.cache_data(show_spinner="Loading image...")
def load_uploaded_image(uploaded_file):
    """
    Load an uploaded image file
    
    Supports: JPEG, PNG, TIFF
    
    Returns: numpy array with shape (height, width, channels)
    """
    try:
        # Read the image
        image = Image.open(uploaded_file)
        
        # Resize if too large (optimization)
        max_size = 2048
        if max(image.size) > max_size:
            image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        # Convert to numpy array
        img_array = np.array(image)
        
        return img_array
    except Exception as e:
        raise ValueError(f"Error loading image: {str(e)}")


def normalize_image(img_array):
    """
    Normalize image values to 0-1 range
    
    Why needed:
    - Most images have values 0-255
    - Index calculations expect 0-1 range
    """
    if img_array.max() > 1:
        return img_array.astype(float) / 255.0
    return img_array.astype(float)


def split_rgb_bands(img_array):
    """
    Split RGB image into separate bands
    
    Returns: Dictionary with 'R', 'G', 'B' arrays
    """
    if len(img_array.shape) == 2:
        # Grayscale image
        return {'R': img_array, 'G': img_array, 'B': img_array}
    
    return {
        'R': img_array[:, :, 0],
        'G': img_array[:, :, 1],
        'B': img_array[:, :, 2]
    }


# =============================================================================
# RGB-BASED VEGETATION INDICES (for uploaded images)
# =============================================================================

def calculate_exg_numpy(img_array):
    """
    ExG - Excess Green Index (numpy version)
    Formula: 2*Green - Red - Blue
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    exg = 2 * bands['G'] - bands['R'] - bands['B']
    return exg


def calculate_vari_numpy(img_array):
    """
    VARI - Visible Atmospherically Resistant Index (numpy version)
    Formula: (Green - Red) / (Green + Red - Blue)
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    numerator = bands['G'] - bands['R']
    denominator = bands['G'] + bands['R'] - bands['B']
    
    # Avoid division by zero
    denominator = np.where(denominator == 0, 0.0001, denominator)
    
    vari = numerator / denominator
    return np.clip(vari, -1, 1)


def calculate_gli_numpy(img_array):
    """
    GLI - Green Leaf Index (numpy version)
    Formula: (2*Green - Red - Blue) / (2*Green + Red + Blue)
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    numerator = 2 * bands['G'] - bands['R'] - bands['B']
    denominator = 2 * bands['G'] + bands['R'] + bands['B']
    
    # Avoid division by zero
    denominator = np.where(denominator == 0, 0.0001, denominator)
    
    gli = numerator / denominator
    return np.clip(gli, -1, 1)


def calculate_rgbvi_numpy(img_array):
    """
    RGBVI - RGB Vegetation Index (numpy version)
    Formula: (Green² - Red*Blue) / (Green² + Red*Blue)
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    g_squared = bands['G'] ** 2
    r_times_b = bands['R'] * bands['B']
    
    numerator = g_squared - r_times_b
    denominator = g_squared + r_times_b
    
    # Avoid division by zero
    denominator = np.where(denominator == 0, 0.0001, denominator)
    
    rgbvi = numerator / denominator
    return np.clip(rgbvi, -1, 1)


def calculate_ngrdi_numpy(img_array):
    """
    NGRDI - Normalized Green-Red Difference Index (numpy version)
    Formula: (Green - Red) / (Green + Red)
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    numerator = bands['G'] - bands['R']
    denominator = bands['G'] + bands['R']
    
    # Avoid division by zero
    denominator = np.where(denominator == 0, 0.0001, denominator)
    
    ngrdi = numerator / denominator
    return np.clip(ngrdi, -1, 1)


def calculate_exgr_numpy(img_array):
    """
    ExGR - Excess Green minus Excess Red (numpy version)
    Formula: 3*Green - 2.4*Red - Blue
    """
    img = normalize_image(img_array)
    bands = split_rgb_bands(img)
    
    exgr = 3 * bands['G'] - 2.4 * bands['R'] - bands['B']
    return exgr


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_rgb_indices():
    """
    Returns list of available RGB-only indices
    """
    return {
        'ExG': 'Excess Green - Simple vegetation detection',
        'VARI': 'Visible Atmospherically Resistant Index',
        'GLI': 'Green Leaf Index',
        'RGBVI': 'RGB Vegetation Index',
        'NGRDI': 'Normalized Green-Red Difference',
        'ExGR': 'Excess Green minus Red'
    }


@st.cache_data(show_spinner="Calculating index...")
def calculate_rgb_index(img_array, index_name):
    """
    Calculate any RGB index by name
    
    Parameters:
    - img_array: numpy array of the image
    - index_name: Name of the index ('ExG', 'VARI', etc.)
    
    Returns: numpy array of the calculated index
    """
    try:
        index_functions = {
            'ExG': calculate_exg_numpy,
            'VARI': calculate_vari_numpy,
            'GLI': calculate_gli_numpy,
            'RGBVI': calculate_rgbvi_numpy,
            'NGRDI': calculate_ngrdi_numpy,
            'ExGR': calculate_exgr_numpy
        }
        
        if index_name not in index_functions:
            raise ValueError(f"Unknown RGB index: {index_name}")
        
        return index_functions[index_name](img_array)
    except Exception as e:
        raise ValueError(f"Error calculating {index_name}: {str(e)}")


@st.cache_data
def create_colormap_image(index_array, colormap='RdYlGn'):
    """
    Convert index array to colored image for display
    
    Parameters:
    - index_array: 2D numpy array of index values
    - colormap: Matplotlib colormap name
    
    Returns: PIL Image object
    """
    import matplotlib.pyplot as plt
    from matplotlib import cm
    
    try:
        # Normalize to 0-1 for colormap
        vmin = np.nanmin(index_array)
        vmax = np.nanmax(index_array)
        
        if vmin == vmax:
            normalized = np.zeros_like(index_array)
        else:
            normalized = (index_array - vmin) / (vmax - vmin)
        
        # Handle NaN values
        normalized = np.nan_to_num(normalized, nan=0.5)
        
        # Apply colormap
        cmap = cm.get_cmap(colormap)
        colored = cmap(normalized)
        
        # Convert to 8-bit RGB
        rgb = (colored[:, :, :3] * 255).astype(np.uint8)
        
        return Image.fromarray(rgb)
    except Exception as e:
        raise ValueError(f"Error creating colormap: {str(e)}")
