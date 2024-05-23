import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import tensorflow as tf

# Assuming you have a file named "metrics.py" with these functions
from metrics import dice_loss, dice_coef, iou 

# Function to read and preprocess the image
def read_and_preprocess_image(file_path):
    image = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (512, 512))  # Adjust size if needed
    image = image / 255.0
    image = image.astype(np.float32)
    return image

# Function to segment and display the image
def segment_and_display_image(file_path):
    if file_path:
        image = read_and_preprocess_image(file_path)
        image = np.expand_dims(image, axis=0)

        with tf.keras.utils.custom_object_scope({'dice_loss': dice_loss}):  
            y_pred = model.predict(image)[0]
        y_pred = y_pred > 0.5
        y_pred = np.squeeze(y_pred)

        mask_image = Image.fromarray(y_pred).convert('RGB')
        mask_image = ImageTk.PhotoImage(mask_image)
        mask_label.configure(image=mask_image)
        mask_label.image = mask_image

# Load the model
model_path = "dummies/files/model.h5"  # Replace with your actual path
with tf.keras.utils.custom_object_scope({'dice_loss': dice_loss, 'dice_coef': dice_coef, 'iou': iou}):
    model = tf.keras.models.load_model(model_path)

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window initially

# Ask for the file directly
file_path = filedialog.askopenfilename(title="Select an image file",
                                      filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

# Create the label to display the mask
mask_label = tk.Label(root)
mask_label.pack()

# Segment and display the image
segment_and_display_image(file_path)

root.deiconify() 
root.mainloop()