# 🤖 Deep Learning Mini Projects – Real-Time Inference Applications

> **A compact collection of 5 deep learning projects built using CNNs and RNNs, showcasing real-world applications in image classification, facial analysis, and natural language processing. Some include web interfaces for interactive user experience.**

---

## 🚀 Projects Overview

### 🧑‍🦱 1. Age and Gender Detection
- **🔍 Description**: Predicts the age and gender of a person from an image using a high-density convolutional neural network (CNN).
- **📦 Model**: Trained on annotated facial image datasets to learn fine-grained features for demographic classification.
- **⚙️ Features**:
  - Accurate estimation of age group and gender.
  - Robust to lighting and facial orientation variations.
- **UI**: No interface; intended for backend/CLI or integration.

---

### 🐾 2. Cat vs Dog Classifier
- **🔍 Description**: A binary image classifier that distinguishes between cat and dog images using deep learning.
- **📦 Model**: CNN trained on thousands of labeled pet images.
- **⚙️ Features**:
  - Efficient image preprocessing pipeline.
  - High classification accuracy.
- **UI**: No user interface; tested via script input or notebook.

---

### 🔤 3. Next Word Prediction
- **🔍 Description**: Predicts the next word in a sentence using a Recurrent Neural Network (RNN) architecture.
- **📦 Model**: Trained using LSTM layers on English text corpora.
- **⚙️ Features**:
  - Works with short input text.
  - Demonstrates basic language modeling.
- **Limitations**: Not designed for bulk file prediction.
- **UI**: No frontend; interactive via command line or notebook cell.

---

### 🌿 4. Plant Disease Prediction
- **🔍 Description**: Identifies plant leaf diseases from uploaded images using a CNN-based classification model.
- **📦 Model**: Trained on plant leaf images for crops like tomato, potato, and more.
- **⚙️ Features**:
  - Detects diseases such as early blight, late blight, etc.
  - Offers disease name as output for supported categories.
- **UI**: Implemented using **Streamlit** for a lightweight, browser-based user experience.

- This project is  about building an Image classifier CNN with Python on Plant Disease Prediction.
- Kaggle Dataset Link: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

---

### 🧑‍💻 5. Real vs Fake Face Detection
- **🔍 Description**: Determines whether a given human face image is real or AI-generated (deepfake) using a CNN classifier.
- **📦 Model**: Trained on real and synthetic face datasets to capture subtle differences in texture and symmetry.
- **⚙️ Features**:
  - Upload interface for image input.
  - Instant prediction (Real or Fake) with high accuracy.
- **UI**: Built using **Flask**, providing a responsive web interface for users.

---

## 🛠️ Technologies Used

| Project                      | Framework | Model Type | Interface  |
|-----------------------------|-----------|------------|------------|
| Age and Gender Detection     | Python    | CNN        | None       |
| Cat vs Dog Classifier        | Python    | CNN        | None       |
| Next Word Prediction         | Python    | RNN (LSTM) | None       |
| Plant Disease Prediction     | Streamlit | CNN        | Yes        |
| Real vs Fake Face Detection  | Flask     | CNN        | Yes        |

---

## ✅ Summary

These projects demonstrate the application of deep learning across various domains:
- 🎯 **Image-based prediction** using CNNs for classification and detection.
- 🧠 **Text prediction** using RNNs for simple natural language processing.
- 🖥️ **Web-based deployment** through Flask and Streamlit for real-time interaction.

Each project reflects a focused implementation of ML concepts, designed to be modular, educational, and production-ready with minimal customization.
