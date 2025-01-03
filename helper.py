import cv2
import numpy as np
from matplotlib.colors import to_rgb

def colorRange(color):
    #Convert color to RGB values
    rgb = to_rgb(color)
    #Conver RGB values into BGR Values
    bgr_array = np.uint8([[[rgb[2]*255, rgb[1]*255, rgb[0]*255]]])
    #Convert to HSV
    hsvColor = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2HSV)

    # Compute the lower and upper limits
    lowerLimit = np.array([hsvColor[0][0][0] - 10, 100, 100])
    upperLimit = np.array([hsvColor[0][0][0] + 10, 255, 255])


    return lowerLimit, upperLimit