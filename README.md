# ☀️ Solar Panel Classification

A deep learning project for automated detection and classification of solar panel defects using EfficientNet. This project includes both a training pipeline and a web-based application for real-time defect detection.

## 📋 Overview

This project leverages convolutional neural networks (CNNs) to classify solar panels into different states, enabling automated quality assurance and maintenance monitoring across solar installations. The model can identify various panel conditions including defects from bird damage, dust accumulation, electrical issues, physical damage, snow coverage, and clean panels.

## 🎯 Features

- **6-Class Classification**: Accurately classifies solar panels into:
  - Bird-drop
  - Clean
  - Dusty
  - Electrical-damage
  - Physical-damage
  - Snow-Covered

- **EfficientNet Model**: Fine-tuned pre-trained model for optimal accuracy and performance
- **Streamlit Web Interface**: User-friendly interface for uploading and classifying panel images
- **Edge Deployment Ready**: Jetson Inference module for deploying on edge devices (NVIDIA Jetson)
- **Dashboard Integration**: API support for sending detection data to central monitoring systems

## 📁 Project Structure

```
├── app.py                              # Streamlit web application
├── jetson_inference.py                 # Edge device inference module
├── Solar_Panel_Classification.ipynb    # Training and development notebook
├── trained_effnet_finetune.h5         # Pre-trained EfficientNet model
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone or download the project**

   ```bash
   cd Solar_Panel_Classification
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Web Application

Launch the Streamlit app to classify solar panels interactively:

```bash
streamlit run app.py
```

The application will:

- Open in your default browser at `http://localhost:8501`
- Display the Solar Panel Defect Classifier interface
- Allow you to upload solar panel images (JPG, JPEG, PNG)
- Show predictions with confidence scores
- Display the classification result for the panel condition

### Training and Development

Open the Jupyter notebook to train the model or explore the dataset:

```bash
jupyter notebook Solar_Panel_Classification.ipynb
```

The notebook includes:

- Data loading from directory structure
- Dataset splitting (80% training, 20% validation)
- Image preprocessing and augmentation
- Model architecture definition
- Training pipeline
- Evaluation metrics
- Visualization of results

## 🔧 Configuration

### Image Specifications

- **Input Size**: 224×224 pixels
- **Batch Size**: 32 (configurable in notebook)
- **Data Format**: RGB images
- **Supported Formats**: JPG, JPEG, PNG

### Model Details

- **Base Architecture**: EfficientNet (pre-trained on ImageNet)
- **Output Classes**: 6 (multi-class classification)
- **Model File**: `trained_effnet_finetune.h5`
- **Framework**: TensorFlow/Keras

## 📡 Edge Deployment (Jetson)

For deployment on NVIDIA Jetson edge devices:

```python
from jetson_inference import send_alert_to_dashboard

# Send detection results to central monitoring dashboard
send_alert_to_dashboard(label="Dusty", confidence=0.92)
```

Configure the API endpoint in `jetson_inference.py`:

```python
API_ENDPOINT = "https://your-solar-dashboard.com/api/logs"
```

## 📊 Model Performance

The EfficientNet model provides:

- **High Accuracy**: Fine-tuned on solar panel defect dataset
- **Fast Inference**: Optimized for real-time predictions
- **Efficient Memory**: Suitable for edge device deployment

## 🔍 Usage Examples

### Via Web Application

1. Start the Streamlit app (`streamlit run app.py`)
2. Click "Upload a solar panel image"
3. Select a JPG, JPEG, or PNG image
4. View the classification result and confidence score

### Via Python Script

```python
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("trained_effnet_finetune.h5")

# Load and preprocess image
image = Image.open("solar_panel.jpg").convert('RGB')
img = image.resize((224, 224))
img_array = np.expand_dims(np.array(img), axis=0)

# Make prediction
predictions = model.predict(img_array)
class_idx = np.argmax(predictions[0])
confidence = predictions[0][class_idx]
```

## 📦 Dependencies

- tensorflow
- keras
- streamlit
- pillow
- numpy
- requests

See `requirements.txt` for specific versions.

## 🛠️ Troubleshooting

**Model not loading:**

- Ensure `trained_effnet_finetune.h5` is in the project directory
- Verify TensorFlow is properly installed

**Streamlit app not opening:**

- Check that port 8501 is available
- Try: `streamlit run app.py --logger.level=debug`

**Image upload issues:**

- Use supported formats: JPG, JPEG, PNG
- Ensure image is readable and not corrupted

## 📚 References

- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [TensorFlow Documentation](https://www.tensorflow.org/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [NVIDIA Jetson Documentation](https://developer.nvidia.com/jetson)

## 📝 License

This project is provided as-is for educational and research purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs or issues
- Suggest improvements
- Add new features or enhancements
- Improve documentation

---

**Developed for Solar Panel Defect Detection and Monitoring Systems**

For questions or support, refer to the project documentation or training notebook.
