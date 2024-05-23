# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # Load the image
# image = cv2.imread('Retinal_Images/12.png')

# # Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# clahe_image = clahe.apply(gray)

# # Apply Gaussian blur for noise removal
# blur_image = cv2.GaussianBlur(clahe_image, (3,3), 0)

# # Show the cropped image using matplotlib
# fig, ax = plt.subplots(figsize=(8, 6))
# ax.imshow(blur_image, cmap='gray')

# # Initialize list to store center coordinates
# centers = []

# # Mark the two points and calculate radius and draw circle
# def onclick(event):
#     x, y = int(event.xdata), int(event.ydata)
#     ax.plot(x, y, 'ro', markersize=10)
#     fig.canvas.draw()
 
#     if len(ax.lines) == 2:
#         # Calculate radius and draw circle
#         x1, y1 = ax.lines[0].get_xdata()[0], ax.lines[0].get_ydata()[0]
#         x2, y2 = ax.lines[1].get_xdata()[0], ax.lines[1].get_ydata()[0]
#         x3, y3 = (x1+x2)/2, (y1+y2)/2
#         radius = int(((x3 - x1)**2 + (y3 - y1)**2)**0.5)
#         circle = plt.Circle((x3, y3), radius, color='r', fill=False)
#         ax.add_artist(circle)
#         print(f"Center coordinates: ({x3}, {y3})")


#         # Draw a horizontal and vertical line intersecting at the center of the circle
#         ax.axhline(y3, color='r', linestyle='-')
#         ax.axvline(x3, color='r', linestyle='-')
                
# fig.canvas.mpl_connect('button_press_event', onclick)
# plt.show()

import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Open a GUI to choose an image file
root = Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])

# Check if a file was selected
if file_path:
    # Load the selected image
    image = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray)

    # Apply Gaussian blur for noise removal
    blur_image = cv2.GaussianBlur(clahe_image, (3, 3), 0)

    # Show the cropped image using matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(blur_image, cmap='gray')

    # Initialize list to store center coordinates
    centers = []

    # Mark the two points and calculate radius and draw circle
    def onclick(event):
        x, y = int(event.xdata), int(event.ydata)
        ax.plot(x, y, 'ro', markersize=10)
        fig.canvas.draw()

        if len(ax.lines) == 2:
            # Calculate radius and draw circle
            x1, y1 = ax.lines[0].get_xdata()[0], ax.lines[0].get_ydata()[0]
            x2, y2 = ax.lines[1].get_xdata()[0], ax.lines[1].get_ydata()[0]
            x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2
            radius = int(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
            circle = plt.Circle((x3, y3), radius, color='r', fill=False)
            ax.add_artist(circle)

            # Draw a horizontal and vertical line intersecting at the center of the circle
            ax.axhline(y3, color='r', linestyle='-')
            ax.axvline(x3, color='r', linestyle='-')

            # Display center coordinates on the image
            ax.text(x3, y3, f'Center: ({x3}, {y3})', color='r', fontsize=10)

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

