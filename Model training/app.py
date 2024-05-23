import streamlit as st
import numpy as np
import cv2
from keras.models import model_from_json


def read_image(image_file):
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (512, 512))
    image = image / 255.0
    image = image.astype(np.float32)
    return image

with open("files/model.json", "r") as json_file:
    model_json = json_file.read()
model = model_from_json(model_json)


model.load_weights("files/model.h5")


st.title("Image Segmentation App")
uploaded_file = st.file_uploader("Upload an image for segmentation...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = read_image(uploaded_file)
    image = np.expand_dims(image, axis=0)

  
    y_pred = model.predict(image)[0]
    y_pred = y_pred > 0.5  
    y_pred = y_pred.astype(np.uint8) * 255

  
    st.image(uploaded_file, caption="Original Image")
    st.image(y_pred, caption="Predicted Segmentation Mask")