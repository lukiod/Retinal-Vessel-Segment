# import cv2
# import matplotlib.pyplot as plt
# import os
# import pandas as pd

# import openpyxl


# # Path to directory containing retinal images
# img_dir = 'imageszip'
# # Create a list of image filenames in the directory
# img_files = os.listdir(img_dir)

# # Create an empty list to store the CDR values

# data_list = []
# # Loop through each image file
# for img_file in img_files:
#     # Load the image
#     img_path = os.path.join(img_dir, img_file)
#     image = cv2.imread(img_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#     clahe_image = clahe.apply(gray)

#     # Apply Gaussian blur for noise removal
#     blur_image = cv2.GaussianBlur(clahe_image, (3,3), 0)

#     # Find the center of the image
#     height, width = blur_image.shape
#     center_x, center_y = int(width/2), int(height/2)

#     # Define ROI around the center
#     roi_width, roi_height = int(width/3), int(height/3)
#     x1, y1 = center_x - int(roi_width/2), center_y - int(roi_height/2)
#     x2, y2 = center_x + int(roi_width/2), center_y + int(roi_height/2)

#     # Crop the image
#     crop_image = blur_image[y1:y2, x1:x2]

#     # Initialize the radius list
#     radius_list = []

#     # Show the cropped image using matplotlib
#     fig, ax = plt.subplots(figsize=(8, 6))
#     ax.imshow(crop_image, cmap='gray')

#     # Mark the two points and calculate radius and draw circle
#     def onclick(event):
#         x, y = int(event.xdata), int(event.ydata)
#         ax.plot(x, y, 'ro', markersize=10)
#         fig.canvas.draw()

#         if len(ax.lines) == 2:
#             # Calculate radius and draw circle
#             x1, y1 = ax.lines[0].get_xdata()[0], ax.lines[0].get_ydata()[0]
#             x2, y2 = ax.lines[1].get_xdata()[0], ax.lines[1].get_ydata()[0]
#             x3, y3 = (x1+x2)/2, (y1+y2)/2
#             radius = int(((x3 - x1)**2 + (y3 - y1)**2)**0.5)
#             circle = plt.Circle((x3, y3), radius, color='r', fill=False)
#             ax.add_artist(circle)
#             fig.canvas.draw()

#             # Store radius value in the list and clear the lines
#             radius_list.append(radius)
#             # ax.lines.clear()

#             # Print radius of on image
#             cv2.putText(crop_image, f"Radius: {radius}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#             ax.imshow(crop_image, cmap='gray')
#             fig.canvas.draw()

#     fig.canvas.mpl_connect('button_press_event', onclick)
#     plt.show()
#     print(radius_list)
#     cdr = radius_list[0]/radius_list[1]
#     print(cdr)

#     if cdr<0.5:
#         Status = "Normal"
#     else:
#         Status = "Glucomactic"


    
#     data_list.append({"Image": img_file,
#                       'CDR': cdr,
#                       "Glucomactic or not" : Status })

#     df = pd.DataFrame(data_list)
#     filepath = "CDR Details.xlsx"
#     df.to_excel(filepath, sheet_name='Sheet1', index=False)




# ----------------------------------------------
# import cv2
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import os
# import pandas as pd
# import tkinter as tk
# from tkinter import filedialog

# # Path to directory containing retinal images
# img_dir = 'imageszip'
# # Create a list of image filenames in the directory
# img_files = os.listdir(img_dir)

# # Create an empty list to store the CDR values
# data_list = []

# # Function to process image and calculate CDR
# def process_image(img_path):
#     image = cv2.imread(img_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     clahe_image = clahe.apply(gray)

#     # Apply Gaussian blur for noise removal
#     blur_image = cv2.GaussianBlur(clahe_image, (3, 3), 0)

#     # Find the center of the image
#     height, width = blur_image.shape
#     center_x, center_y = int(width / 2), int(height / 2)

#     # Define ROI around the center
#     roi_width, roi_height = int(width / 3), int(height / 3)
#     x1, y1 = center_x - int(roi_width / 2), center_y - int(roi_height / 2)
#     x2, y2 = center_x + int(roi_width / 2), center_y + int(roi_height / 2)

#     # Crop the image
#     crop_image = blur_image[y1:y2, x1:x2]

#     # Initialize the radius list
#     radius_list = []

#     # Show the cropped image using matplotlib
#     fig, ax = plt.subplots(figsize=(8, 6))
#     ax.imshow(crop_image, cmap='gray')

#     # Mark the two points and calculate radius and draw circle
#     def onclick(event):
#         x, y = int(event.xdata), int(event.ydata)
#         ax.plot(x, y, 'ro', markersize=10)
#         fig.canvas.draw()

#         if len(ax.lines) == 2:
#             # Calculate radius and draw circle
#             x1, y1 = ax.lines[0].get_xdata()[0], ax.lines[0].get_ydata()[0]
#             x2, y2 = ax.lines[1].get_xdata()[0], ax.lines[1].get_ydata()[0]
#             x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2
#             radius = int(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
#             circle = plt.Circle((x3, y3), radius, color='r', fill=False)
#             ax.add_artist(circle)
#             fig.canvas.draw()

#             # Store radius value in the list and clear the lines
#             radius_list.append(radius)
#             # ax.lines.clear()

#             # Print radius on image
#             cv2.putText(crop_image, f"Radius: {radius}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#             ax.imshow(crop_image, cmap='gray')
#             fig.canvas.draw()

#             # Schedule the calculation of CDR after a short delay
#             root.after(100, calculate_cdr, os.path.basename(img_path))

#     fig.canvas.mpl_connect('button_press_event', onclick)
#     plt.show()

#     return radius_list

# # Function to calculate CDR and update data_list
# def calculate_cdr(img_file):
#     img_path = os.path.join(img_dir, img_file)
#     radius_list = process_image(img_path)
#     print(radius_list)

#     # Check if there are at least two elements in radius_list before calculating cdr
#     if len(radius_list) >= 2:
#         cdr = radius_list[0] / radius_list[1]
#         print(cdr)

#         if cdr < 0.5:
#             Status = "Normal"
#         else:
#             Status = "Glucomactic"

#         data_list.append({"Image": img_file,
#                           'CDR': cdr,
#                           "Glucomactic or not": Status })

#         df = pd.DataFrame(data_list)
#         filepath = "CDR Details.xlsx"
#         df.to_excel(filepath, sheet_name='Sheet1', index=False)
#     else:
#         print(" ")

# # Tkinter UI code
# def open_file_dialog():
#     filename = filedialog.askopenfilename(initialdir=img_dir, title="Select Image",
#                                           filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("all files", "*.*")))
#     entry.delete(0, tk.END)
#     entry.insert(0, os.path.basename(filename))
#     calculate_cdr(os.path.basename(filename))

# import subprocess
# def run_quadrant_script():
#     try:
#         # Call the Quadrant.py script using subprocess
#         subprocess.run(["python", "Quadrant.py"])
#     except Exception as e:
#         print(f"Error: {e}")

# def run_MiddlePoint_script():
#     try:
#         # Call the Quadrant.py script using subprocess
#         subprocess.run(["python", "dummies/MiddlePoint.py"])
#     except Exception as e:
#         print(f"Error: {e}")


# # Create Tkinter window
# root = tk.Tk()
# root.title("Retinal Blood Vessel Segmentation")

# # Create an entry widget for image filename input
# entry = tk.Entry(root, width=40)
# entry.pack(side=tk.TOP, pady=10)

# # Heading
# heading_label = tk.Label(root, text="Retinal Blood Vessel Segmentation", font=("Helvetica", 16))
# heading_label.pack(side=tk.TOP, pady=10)
# # Subheading
# subheading_label = tk.Label(root, text="Choose a feature", font=("Helvetica", 14))
# subheading_label.pack(side=tk.TOP, pady=10)

# # Button (Feature 1)
# choose_image_button = tk.Button(root, text="Calculate the Radius", command=open_file_dialog)
# choose_image_button.pack(side=tk.LEFT, pady=10)

# # Button to calculate feature 2
# feature2_button = tk.Button(root, text="See the Quadrants", command=run_quadrant_script)
# feature2_button.pack(side=tk.LEFT, padx=10)

# # Button to calculate feature 3
# feature3_button = tk.Button(root, text="See the Center", command=run_MiddlePoint_script)
# feature3_button.pack(side=tk.LEFT, padx=10)

# # Image label
# img_label = tk.Label(root)
# img_label.pack(side=tk.TOP, pady=10)

# # Run the Tkinter main loop
# root.mainloop()

import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Path to directory containing retinal images
img_dir = 'imageszip'
# Create a list of image filenames in the directory
img_files = os.listdir(img_dir)

# Create an empty list to store the CDR values
data_list = []

# Function to process image and calculate CDR
def process_image(img_path):
    image = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray)

    # Apply Gaussian blur for noise removal
    blur_image = cv2.GaussianBlur(clahe_image, (3, 3), 0)

    # Initialize the radius list
    radius_list = []

    # Show the image using matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(blur_image, cmap='gray')

    # # Mark the two points and calculate radius and draw circle
    # def onclick(event):
    #     x, y = int(event.xdata), int(event.ydata)
    #     ax.plot(x, y, 'ro', markersize=10)
    #     fig.canvas.draw()

    #     if len(ax.lines) == 2:
    #         # Calculate radius and draw circle
    #         x1, y1 = ax.lines[0].get_xdata()[0], ax.lines[0].get_ydata()[0]
    #         x2, y2 = ax.lines[1].get_xdata()[0], ax.lines[1].get_ydata()[0]
    #         x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2
    #         radius = int(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
    #         circle = plt.Circle((x3, y3), radius, color='r', fill=False)
    #         ax.add_artist(circle)
    #         fig.canvas.draw()

    #         # Store radius value in the list and clear the lines
    #         radius_list.append(radius)
    #         ax.lines.clear()  # Clear the lines drawn for marking points

    #         # Clear the entire axes
    #         ax.clear()

    #         # Print radius on image
    #         cv2.putText(blur_image, f"Radius: {radius}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    #         ax.imshow(blur_image, cmap='gray')
    #         fig.canvas.draw()

    #         # Schedule the calculation of CDR after a short delay
    #         root.after(100, calculate_cdr, os.path.basename(img_path), radius_list)

            # Mark the two points and calculate radius and draw circle
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

            # Store radius value in the list and clear the lines
            radius_list.append(radius)
            
            # Clear the lines drawn for marking points
            for line in ax.lines:
                line.remove()

            # Print radius on image
            text = f"Radius: {radius}"
            ax.text(10, 30, text, fontsize=12, color='black', bbox=dict(facecolor='white', alpha=0.7))
            fig.canvas.draw()

            # Schedule the calculation of CDR after a short delay
            root.after(100, calculate_cdr, os.path.basename(img_path), radius_list)



    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

def calculate_cdr(img_file, radius_list):
    img_path = os.path.join(img_dir, img_file)

    # Check if there are at least two elements in radius_list before calculating cdr
    if len(radius_list) >= 2:
        cdr = radius_list[0] / radius_list[1]
        print(cdr)

        if cdr < 0.5:
            Status = "Normal"
        else:
            Status = "Glucomactic"

        data_list.append({"Image": img_file,
                          'CDR': cdr,
                          "Glucomactic or not": Status })

        df = pd.DataFrame(data_list)
        filepath = "CDR Details.xlsx"
        df.to_excel(filepath, sheet_name='Sheet1', index=False)
    else:
        print(" ")

# Tkinter UI code
def open_file_dialog():
    filename = filedialog.askopenfilename(initialdir=img_dir, title="Select Image",
                                          filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("all files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, os.path.basename(filename))
    process_image(filename)

# Create Tkinter window
root = tk.Tk()
root.title("Retinal Blood Vessel Segmentation")

# Create an entry widget for image filename input
entry = tk.Entry(root, width=40)
entry.pack(side=tk.TOP, pady=10)

import subprocess
def run_quadrant_script():
    try:
        # Call the Quadrant.py script using subprocess
        subprocess.run(["python", "dummies/Quadrant.py"])
    except Exception as e:
        print(f"Error: {e}")

def run_MiddlePoint_script():
    try:
        # Call the Quadrant.py script using subprocess
        subprocess.run(["python", "dummies/MiddlePoint.py"])
    except Exception as e:
        print(f"Error: {e}")
def run_seg_script():
    try:
        # Call the Quadrant.py script using subprocess
        subprocess.run(["python", "dummies/segm.py"])
    except Exception as e:
        print(f"Error: {e}")


# Heading
heading_label = tk.Label(root, text="Retinal Blood Vessel Segmentation", font=("Helvetica", 16))
heading_label.pack(side=tk.TOP, pady=10)
# Subheading
subheading_label = tk.Label(root, text="Choose a feature", font=("Helvetica", 14))
subheading_label.pack(side=tk.TOP, pady=10)

# Button (Feature 1)
choose_image_button = tk.Button(root, text="Calculate the Radius", command=open_file_dialog)
choose_image_button.pack(side=tk.LEFT, pady=10)

# Button to calculate feature 2
feature2_button = tk.Button(root, text="See the Quadrants", command=run_quadrant_script)
feature2_button.pack(side=tk.LEFT, padx=10)

# Button to calculate feature 3
feature3_button = tk.Button(root, text="See the Center", command=run_MiddlePoint_script)
feature3_button.pack(side=tk.LEFT, padx=10)
feature4_button = tk.Button(root, text="segmentation", command=run_seg_script)
feature4_button.pack(side=tk.LEFT, padx=10)

# Image label
img_label = tk.Label(root)
img_label.pack(side=tk.TOP, pady=10)

# Run the Tkinter main loop
root.mainloop()
