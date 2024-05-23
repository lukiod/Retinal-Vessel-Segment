# # import cv2
# # import matplotlib.pyplot as plt

# # # Load the image
# # image = cv2.imread('Retinal_Images/37.png')

# # # Convert to grayscale
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for contrast enhancement
# # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# # clahe_image = clahe.apply(gray)

# # # Apply Gaussian blur for noise removal
# # blur_image = cv2.GaussianBlur(clahe_image, (3,3), 0)

# # # Find the center of the image
# # height, width = blur_image.shape
# # center_x, center_y = int(width/2), int(height/2)

# # # Define ROI around the center
# # roi_width, roi_height = int(width/3), int(height/3)
# # x1, y1 = center_x - int(roi_width/2), center_y - int(roi_height/2)
# # x2, y2 = center_x + int(roi_width/2), center_y + int(roi_height/2)

# # # Crop the image
# # crop_image = blur_image[y1:y2, x1:x2]

# # # Display the cropped image using matplotlib
# # plt.imshow(crop_image, cmap='gray')

# # # Get user input for two points
# # print("Click on two points to mark them, then press Enter")
# # points = plt.ginput(2)

# # # Calculate midpoint of the two points
# # x, y = (points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2

# # # Mark the midpoint with a red circle
# # plt.plot(x, y, 'ro', markersize=10)

# # # Show the marked image
# # plt.show()

# import cv2
# import matplotlib.pyplot as plt
# from tkinter import Tk, filedialog

# # Open a GUI to choose an image file
# root = Tk()
# root.withdraw()  # Hide the main window

# file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])

# # Check if a file was selected
# if file_path:
#     # Load the selected image
#     image = cv2.imread(file_path)

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

#     # Display the cropped image using matplotlib
#     plt.imshow(crop_image, cmap='gray')

#     # Get user input for two points
#     print("Click on two points to mark them, then press Enter")
#     points = plt.ginput(2)

#     # Calculate midpoint of the two points
#     x, y = (points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2

#     # Mark the midpoint with a red circle
#     plt.plot(x, y, 'ro', markersize=10)

#     # Show the marked image
#     plt.show()








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

    # Display the image using matplotlib
    plt.imshow(blur_image, cmap='gray')

    # Get user input for two points
    print("Click on two points to mark them, then press Enter")
    points = plt.ginput(2)

    # Calculate midpoint of the two points
    x, y = (points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2

    # Display and store the center value
    center_x, center_y = int(image.shape[1] / 2), int(image.shape[0] / 2)
    center_text = f"Center Coordinates (x, y): {center_x}, {center_y}"

    # Add text annotation for center coordinates
    plt.text(center_x, center_y, center_text, color='white', fontsize=10, ha='center', va='center', bbox=dict(facecolor='red', alpha=0.5))

    # Show the marked image with center coordinates
    plt.show()

    # Save the center coordinates along with the image
    center_coordinates_file_path = file_path.replace('.png', '_center_coordinates.txt')
    with open(center_coordinates_file_path, 'w') as file:
        file.write(f"Center Coordinates (x, y): {center_x}, {center_y}")
