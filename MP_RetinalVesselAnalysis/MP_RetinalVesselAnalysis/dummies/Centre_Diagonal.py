import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import numpy as np

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

    height, width = blur_image.shape
    center_x, center_y = int(width / 2), int(height / 2)

    # Define the size of the cropped image
    crop_size = 800

    # Calculate the coordinates for the top-left corner of the cropped image
    crop_x = center_x - int(crop_size / 2)
    crop_y = center_y - int(crop_size / 2)

    # Crop the image
    crop_image = blur_image[crop_y:crop_y + crop_size, crop_x:crop_x + crop_size]

    # Show the cropped image using matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(crop_image, cmap='gray')

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
            fig.canvas.draw()

            # Draw the two perpendicular lines
            angle = np.pi / 4  # 45 degrees angle in radians
            line1_x = [x3 - radius * np.cos(angle), x3 + radius * np.cos(angle)]
            line1_y = [y3 - radius * np.sin(angle), y3 + radius * np.sin(angle)]
            ax.plot(line1_x, line1_y, 'b', linewidth=2)

            line2_x = [x3 - radius * np.sin(angle), x3 + radius * np.sin(angle)]
            line2_y = [y3 + radius * np.cos(angle), y3 - radius * np.cos(angle)]
            ax.plot(line2_x, line2_y, 'b', linewidth=2)
            fig.canvas.draw()

        elif len(ax.lines) == 4:
            # Calculate radius and draw circle
            x4, y4 = ax.lines[2].get_xdata()[0], ax.lines[2].get_ydata()[0]
            x5, y5 = ax.lines[3].get_xdata()[0], ax.lines[3].get_ydata()[0]
            x6, y6 = (x4 + x5) / 2, (y4 + y5) / 2
            radius2 = int(((x6 - x4) ** 2 + (y6 - y4) ** 2) ** 0.5)
            circle2 = plt.Circle((x6, y6), radius2, color='g', fill=False)
            ax.add_artist(circle2)
            fig.canvas.draw()

            # Draw the two perpendicular lines
            angle = np.pi / 4  # 45 degrees angle in radians
            line1_x = [x6 - radius2 * np.cos(angle), x6 + radius2 * np.cos(angle)]
            line1_y = [y6 - radius2 * np.sin(angle), y6 + radius2 * np.sin(angle)]
            ax.plot(line1_x, line1_y, 'm', linewidth=2)

            line2_x = [x6 - radius2 * np.sin(angle), x6 + radius2 * np.sin(angle)]
            line2_y = [y6 + radius2 * np.cos(angle), y6 - radius2 * np.cos(angle)]
            ax.plot(line2_x, line2_y, 'm', linewidth=2)
            fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.pause(0.001)
    plt.show()
