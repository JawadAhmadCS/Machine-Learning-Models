# Overview

This project demonstrates the implementation of a **Logistic Regression model** and evaluates its performance using various metrics.

---

## What is Logistic Regression?

Logistic Regression is a machine learning model used for **classification problems**. It helps in predicting one of two categories, such as:
- "Yes" or "No"
- "1" or "0"

### How It Works:
- **Logistic Function:** The model predicts a **probability** between 0 and 1.  
  - If the probability > 0.5, the output is "1" (positive class).  
  - If the probability ≤ 0.5, the output is "0" (negative class).

---
## Implementation
1. The project follows these steps:
2. Import necessary libraries.
3. Load and preprocess the dataset.
4. Split the data into training and testing sets.
5. Standardize features using StandardScaler.
6. Train the logistic regression model using sklearn.
7. Evaluate model performance with metrics:
8. Confusion Matrix
9. Precision, Recall, F1-Score, Accuracy
10. Visualize results with a heatmap.

---
## How Does This Project Work?

We train the logistic regression model using a dataset. The process involves the following steps:

### 1. **Dataset**
- The dataset used here is `Social_Network_Ads.csv`, containing features (`X`) and a target variable (`y`).
  - Features: Information used for predictions.
  - Target Variable: The outcome we want to predict (e.g., "0" or "1").

### 2. **Splitting the Data**
The data is divided into:
- **Training Data:** Used to train the model.
- **Testing Data:** Used to test how well the model predicts unseen data.

### 3. **Feature Scaling**
- Normalizes the data to ensure all features have the same scale, improving the model's performance.

---
## Installation and Requirements
### **1. Clone the Repository**
```bash
git clone https://github.com/JawadAhmadCS/Machine-Learning-Models.git
cd Machine-Learning-Models/Linear\ Regression
```
### **2. Dataset**
Ensure you have the Social_Network_Ads.csv file in the project directory. This file contains the input data required for training and testing the model.
### **3. Prepare the Environment**

Ensure you have the following libraries installed:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
### **4. Run the Code**
Open the file logistic_regression.py in any Python IDE or editor, or use Jupyter Notebook to execute the code step by step.

### **5. Output Results**
After running the code:
The confusion matrix will be displayed visually.
The terminal will show precision, recall, F1-score, and accuracy.

---

## License

> **This Model is open-source and available under the MIT License. You are free to use and modify it for educational purposes.**
