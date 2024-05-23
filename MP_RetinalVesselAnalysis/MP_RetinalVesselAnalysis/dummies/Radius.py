# import cv2
# import matplotlib.pyplot as plt
# import os
# import pandas as pd



# # Path to directory containing retinal images
# img_dir = 'Retinal_Images'
# # Create a list of image filenames in the directory
# img_files = os.listdir(img_dir)

# # Create an empty list to store the R values

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



import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd

# Path to directory containing retinal images
img_dir = 'Retinal_Images'
# Create a list of image filenames in the directory
img_files = os.listdir(img_dir)

# Create an empty list to store the R values
data_list = []

# Loop through each image file
for img_file in img_files:
    # Load the image
    img_path = os.path.join(img_dir, img_file)
    image = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray)

    # Apply Gaussian blur for noise removal
    blur_image = cv2.GaussianBlur(clahe_image, (3, 3), 0)

    # Find the center of the image
    height, width = blur_image.shape
    center_x, center_y = int(width / 2), int(height / 2)

    # Initialize the radius list
    radius_list = []

    # Show the image using matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(blur_image, cmap='gray')

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
            ax.lines.clear()  # Clear the lines drawn for marking points

            # Clear the entire axes
            ax.clear()

            # Print radius on image
            cv2.putText(blur_image, f"Radius: {radius}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            ax.imshow(blur_image, cmap='gray')
            fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    print(radius_list)
