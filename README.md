# 👁️ Retinal Vessel Segmentation 🔍

This project brings 💡 deep learning to medical imaging by accurately segmenting retinal vessels from fundus images, enabling precise 👌 diagnosis and monitoring of eye diseases. Get ready for an awesome 🚀 user experience with two GUI options!

## 🌟 Features

- **🌐 Streamlit GUI:** Interactive and modern GUI with real-time image processing.
- **🧠 Deep Learning Models:** State-of-the-art algorithms for accurate segmentation.
- **🤖 Ensemble Modeling:** Combining multiple models for improved performance.

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/lukiod/Retinal-Vessel-Segment.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Download model.h5 and model.json from HuggingFace ```https://huggingface.co/spaces/aiwaks/retinal``` and store it in files folder
4. Download the Drive Dataset from    ```https://paperswithcode.com/dataset/drive```
3. - **Streamlit:**
        ```bash
        streamlit run app.py
        ```
## 📂 Directory Structure

The project directory contains the following structure:

    Retinal-Vessel-Segment/
    ├── .git/
    ├── pycache/
    ├── app.py
    ├── data.py
    ├── eval.py
    ├── files/
    ├── metrics.py
    ├── model.py
    ├── new_data/
    ├── README.md
    ├── requirements.txt
    ├── results/
    └── train.py

### File Descriptions

- **.git/**: Directory containing the Git version control system files.
- **__pycache__/**: Directory containing the compiled Python files.
- **app.py**: Contains the application code to run the segmentation model, providing both Tkinter and Streamlit GUIs.
- **data.py**: Handles data loading and preprocessing, including functions for reading images and preparing them for model input.
- **eval.py**: Evaluates the trained model on the test dataset and generates performance metrics.
- **files/**: Directory to store the pre-trained model files (`model.h5` and `model.json`).
- **metrics.py**: Defines metrics for evaluating the model's performance, such as accuracy, precision, recall, and F1 score.
- **model.py**: Defines the neural network model architecture used for segmenting the retinal vessels.
- **new_data/**: Directory for storing new datasets or any additional data required for model training or evaluation.
- **README.md**: The file you are currently reading, which provides an overview and documentation for the project.
- **requirements.txt**: Lists all the Python dependencies required to run the project. Use this file to install all dependencies with `pip install -r requirements.txt`.
- **results/**: Directory where the results of the model’s evaluation, including segmented images and performance metrics, will be saved.
- **train.py**: Contains the training loop and logic, including functions for model training, validation, and saving the trained model.

## 📂 Dataset

Trained on the DRIVE dataset of fundus images with manual labels.The dataset is in *.tif format 📈

## 🔭 Future Aspects

- 📥 Integrate new deep learning architectures.
- 🌐 Web-based deployment for wider accessibility.
- 📡 Support for other medical imaging modalities.

## 🤝 Contributing

Found an issue or have a cool idea? Open an issue or submit a pull request! 🎉

## 📄 License


## 🙏 Acknowledgments

- **Dataset Source:** [DRIVE Dataset](https://drive.grand-challenge.org/)
- **Deep Learning Library Used:** [TensorFlow](https://www.tensorflow.org/) / [PyTorch](https://pytorch.org/)
- **GUI Framework(s) Used:** [Tkinter](https://docs.python.org/3/library/tkinter.html) / [Streamlit](https://streamlit.io/)

Let's revolutionize 💥 medical imaging together! 🚀
