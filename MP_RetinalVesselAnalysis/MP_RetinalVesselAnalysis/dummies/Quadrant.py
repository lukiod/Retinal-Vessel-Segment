import cv2
import matplotlib.pyplot as plt

# Load the retinal fundus image
image = cv2.imread("dummies/Retinal_Images/12.png")

# Define the center coordinates of the optic disc
optic_disc_center = (718,666) # Replace x and y with your actual coordinates

# Define the size of each quadrant based on the position of the center of the optic disc
h1 = optic_disc_center[1]
h2 = image.shape[0] - optic_disc_center[1]
w1 = optic_disc_center[0]
w2 = image.shape[1] - optic_disc_center[0]

# Extract the four quadrants of the retinal fundus image
quadrant1 = image[0:h1, 0:w1]
quadrant2 = image[0:h1, w1:image.shape[1]]
quadrant3 = image[h1:image.shape[0], 0:w1]
quadrant4 = image[h1:image.shape[0], w1:image.shape[1]]

# Display the four quadrants in separate windows
plt.figure(figsize=(8,8))
plt.subplot(2,2,1), plt.imshow(quadrant1)
plt.title("Quadrant 1"), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(quadrant2)
plt.title("Quadrant 2"), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(quadrant3)
plt.title("Quadrant 3"), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(quadrant4)
plt.title("Quadrant 4"), plt.xticks([]), plt.yticks([])
plt.show()
