# Step 1: Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score


# Personal Details and Social Media Links:
# Author: Muhammad Jawad Ahmad
# LinkedIn: https://www.linkedin.com/in/jawadahmadcs/
# Instagram: https://www.instagram.com/jawadahmadcs
# Facebook: https://www.facebook.com/JawadAhmadCS
# GitHub: https://github.com/JawadAhmadCS
# Blogs: https://jawadahmadcs.blogspot.com/

# Step 2: Load the Dataset
dataset = pd.read_csv('Social_Network_Ads.csv')  
X = dataset.iloc[:, :-1].values  # Features
y = dataset.iloc[:, -1].values   # Labels

# Step 3: Split the Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

# Step 4: Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test)        

# Step 5: Train the Logistic Regression Model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Step 6: Predict Test Set Results
y_pred = classifier.predict(X_test)

# Step 7: Evaluate Model Performance
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Metrics: Precision, Recall, F1-Score, Accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
print(f"Accuracy: {accuracy}")

# Step 8: Visualize the Confusion Matrix
cm_df = pd.DataFrame(cm, index=['0', '1'], columns=['0', '1']) 
plt.figure(figsize=(7, 4))
sns.heatmap(cm_df, cmap='Greens', annot=True)
plt.title('Confusion Matrix')
plt.ylabel('Actual Class')
plt.xlabel('Predicted Class')
plt.show()
