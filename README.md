# Cat vs Dog CNN Classifier

A deep learning image classification project built using TensorFlow and Keras.  
This project trains a Convolutional Neural Network (CNN) model to classify cat and dog images.

---

## Project Overview

The model was trained on a dataset containing multiple cat and dog images organized into separate folders:

- `cats_set/`
- `dogs_set/`

The dataset contained around **1000 total images**.  
Since the dataset was large, the image files themselves were not uploaded to GitHub.

TensorFlow automatically loaded the dataset from the local folders during training.

---

## Technologies Used

- Python
- TensorFlow
- Keras
- CNN (Convolutional Neural Network)

---

## Features

- Image preprocessing
- CNN model creation
- Training and validation split
- Accuracy tracking
- Model saving using `.keras`

---

## Training Results

| Metric | Result |
|--------|--------|
| Training Accuracy | ~78% |
| Validation Accuracy | ~65% |
| Epochs | 5 |

---

## Dataset Structure

```plaintext
cat_dog_project/
│
├── cats_set/
├── dogs_set/
├── main.py
├── README.md
└── .gitignore
````

---

## Model Workflow

```plaintext
Dataset
   ↓
Image Preprocessing
   ↓
CNN Model
   ↓
Training
   ↓
Validation
   ↓
Saved Model
```

---

## Learning Outcomes

Through this project, I learned:

* TensorFlow and Keras basics
* CNN architecture
* Image preprocessing
* Model training and validation
* Overfitting concepts
* Environment setup and dependency handling
* GitHub project structuring

---

## Note

The dataset images were not uploaded to GitHub because of their large size.
Only the project code and configuration files are included in this repository.

```
```
