# 👁️ Retinal Vessel Segmentation 🔍

This project brings 💡 deep learning to medical imaging by accurately segmenting retinal vessels from fundus images, enabling precise 👌 diagnosis and monitoring of eye diseases. Get ready for an awesome 🚀 user experience with two GUI options!

## 🌟 Features

- **💻 Tkinter GUI:** Simple and intuitive interface for uploading and visualizing segmentation results.
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
3. Run the GUI:
    - **Tkinter:**
        ```bash
        cd MP_RetinalVesselAnalysis\MP_RetinalVesselAnalysis
        python cd.py
        ```
    - **Streamlit:**
        ```bash
        cd Model training
        streamlit run app.py
        ```

## 📂 Dataset

Trained on the DRIVE dataset of fundus images with manual labels. 📈

## 🔭 Future Aspects

- 📥 Integrate new deep learning architectures.
- 🌐 Web-based deployment for wider accessibility.
- 📡 Support for other medical imaging modalities.

## 🤝 Contributing

Found an issue or have a cool idea? Open an issue or submit a pull request! 🎉

## 📄 License

MIT License

## 🙏 Acknowledgments

- **Dataset Source:** [DRIVE Dataset](https://drive.grand-challenge.org/)
- **Deep Learning Library Used:** [TensorFlow](https://www.tensorflow.org/) / [PyTorch](https://pytorch.org/)
- **GUI Framework(s) Used:** [Tkinter](https://docs.python.org/3/library/tkinter.html) / [Streamlit](https://streamlit.io/)

Let's revolutionize 💥 medical imaging together! 🚀
