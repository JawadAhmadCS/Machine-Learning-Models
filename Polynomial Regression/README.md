# Overview

This repository demonstrates the use of **Polynomial Regression** to predict heights based on age using the dataset `HeightVsWeight1.csv`. The project includes data visualization and prediction capabilities to analyze the relationship between age and height.

---

## Features
- **Polynomial Regression Model**: Predicts height using a cubic polynomial for more complex relationships.
- **Data Visualization**: Graphical representation of the dataset and regression curves.

---


### Prerequisites
Ensure you have Python installed along with the following libraries:
- `pandas`
- `scikit-learn`
- `matplotlib`

Install missing dependencies using:
```bash
pip install pandas scikit-learn matplotlib
```
## Installation and Requirements
### **1. Clone the Repository**
```bash
git clone https://github.com/JawadAhmadCS/Machine-Learning-Models.git
cd Machine-Learning-Models/Polynomial\ Regression
```
### **2. Dataset**
Ensure you have the `HeightVsWeight1.csv` file in the project directory. This file contains the input data required for training and testing the model.
### **3. Prepare the Environment**

Ensure you have the following libraries installed:
```bash
pip install pandas scikit-learn matplotlib
```
### **4. Run the Code**
Open the file `Polynomial Regression.py` in any Python IDE or editor, or use Jupyter Notebook to execute the code step by step.

### **5. Output Results**
**1. Linear Regression Predictions**
Predicts height based on a linear model.

**2. Polynomial Regression Predictions**
Provides improved predictions using a cubic polynomial.

***Example Prediction Results:***
```
Linear model prediction for Ages [10, 34, 66] is  [[136.74474474]
 [147.22814243]
 [161.20600601]]
Polynomial model prediction for Ages [10, 34, 66] is  [[137.65046018]
 [146.50901764]
 [183.67051214]]
```
**3. Graphical Output**
- Red dots: Original data points.
- Blue curve: Polynomial regression model.

![image](https://github.com/user-attachments/assets/63271300-400e-4f73-b05e-203d0074cca6)

---

## License

> **This Model is open-source and available under the MIT License. You are free to use and modify it for educational purposes.**
