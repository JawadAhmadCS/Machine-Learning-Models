# Overview

This repository contains a Python implementation of a simple **Linear Regression Model** to predict the number of jobs/sec based on frequency data. The program is designed to demonstrate basic machine learning concepts such as data preprocessing, training a model, and visualizing the results.

---
## Dataset
The dataset used in this program is stored in `sample.csv` and consists of the following columns:
- **Frequency**: Input feature representing the frequency.
- **No of Jobs**: Target variable representing the number of jobs/sec.
---
## Steps Performed
1. **Import Libraries**:
   - Used `pandas` for data manipulation.
   - Used `matplotlib` for data visualization.
   - Used `scikit-learn` for implementing the Linear Regression model and calculating error metrics.

2. **Load the Dataset**:
   - The dataset is read from `sample.csv`.

3. **Data Splitting**:
   - The dataset is split into training (70%) and testing (30%) subsets.

4. **Train the Linear Regression Model**:
   - The training data is used to fit the Linear Regression model.

5. **Make Predictions**:
   - Predictions are made for custom frequency values: `[3.9, 3.2, 2.7, 3.7]`.
   - Predictions are also made for the test data to calculate the model's performance.

6. **Model Evaluation**:
   - The **Mean Squared Error (MSE)** is calculated to measure the prediction error on the test data.

7. **Visualization**:
   - A scatter plot visualizes the training data points.
   - The regression line is plotted to demonstrate the model's predictions.
---
## Prerequisites
- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - scikit-learn

You can install the required libraries using:
```bash
pip install pandas matplotlib scikit-learn
```
---
## Installation and Requirements
### **1. Clone the Repository**
```bash
git clone https://github.com/JawadAhmadCS/Machine-Learning-Models.git
cd Machine-Learning-Models/Linear\ Regression
```
### **2. Dataset**
Ensure you have the `sample.csv` file in the project directory. This file contains the input data required for training and testing the model.
### **3. Prepare the Environment**

Ensure you have the following libraries installed:
```bash
pip install pandas matplotlib scikit-learn
```
### **4. Run the Code**
Open the file `Linear Regression.py` in any Python IDE or editor, or use Jupyter Notebook to execute the code step by step.

### **5. Output Results**
- **Predictions:** Predicted number of jobs/sec for given frequency values.
- **Model Performance:** The Mean Squared Error (MSE) of the model.
- **Visualization:** A scatter plot with the regression line.

***Example Prediction Results:***
```
`Predicted No of Jobs/Sec for {3.9, 3.2, 2.7, 3.7}:
 [[176.3876652 ]
 [135.22026432]
 [105.81497797]
 [164.62555066]]
Mean Square Error:  15.553377709639491`
```
![image](https://github.com/user-attachments/assets/23155e2d-8ec6-4de2-8e01-5fcc60907f60)

---

## License

> **This Model is open-source and available under the MIT License. You are free to use and modify it for educational purposes.**
