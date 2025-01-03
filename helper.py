import cv2
import numpy as np
from matplotlib.colors import to_rgb

# def colorRange(color):
#     #Convert color to RGB values
#     rgb = to_rgb(color)
#     #Conver RGB values into BGR Values
#     bgr_array = np.uint8([[[rgb[2]*255, rgb[1]*255, rgb[0]*255]]])
#     #Convert to HSV
#     hsvColor = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2HSV)

#     # Compute the lower and upper limits
#     lowerLimit = np.array([hsvColor[0][0][0] - 10, 100, 100])
#     upperLimit = np.array([hsvColor[0][0][0] + 10, 255, 255])


#     return lowerLimit, upperLimit

def colorRange(color):
    # Give specific color ranges
    # Format: (lower limit HSV, upper limit HSV)
    color_ranges = {
        'blue': (np.array([95, 50, 50]), np.array([135, 255, 255])),
        'green': (np.array([35, 50, 50]), np.array([85, 255, 255])),
        'purple': (np.array([125, 50, 50]), np.array([155, 255, 255])),
        'red': (np.array([0, 50, 50]), np.array([10, 255, 255])),
        'red2': (np.array([170, 50, 50]), np.array([180, 255, 255])),  # Red needs two ranges, wraps around
        'yellow': (np.array([20, 50, 50]), np.array([35, 255, 255])),
        'orange': (np.array([5, 50, 50]), np.array([20, 255, 255]))
    }
    
    color = color.lower()
    if color == 'red':
        return color_ranges['red'], color_ranges['red2']  # Return both red ranges
    elif color in color_ranges:
        return color_ranges[color]
    else:
        raise ValueError(f"Color '{color}' not supported. Supported colors are: {', '.join(color_ranges.keys())}")