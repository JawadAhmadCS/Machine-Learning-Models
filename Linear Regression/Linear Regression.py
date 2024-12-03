# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 2: Load the dataset
ds = pd.read_csv("sample.csv")

# Step 3: Select features (Frequency) and target variable (no of jobs)
x = ds[["Frequency"]]
y = ds[["no of jobs"]]

# Step 4: Split the dataset into training and testing sets
xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.3)

# Step 5: Create a Linear Regression model and train it on the training data
LR = LinearRegression()
LR.fit(xtr, ytr)

# Step 6: Create a test dataset for predictions
test = {
    "Frequency": [3.9, 3.2, 2.7, 3.7],
}
tds = pd.DataFrame(test)

# Step 7: Make predictions for the test dataset
a = LR.predict(tds)
print("\nPredicted No of Jobs/Sec for {3.9, 3.2, 2.7, 3.7}:\n\n", a)

# Step 8: Make predictions on the testing data and calculate the mean squared error
pred = LR.predict(xte)
mse = mean_squared_error(yte, pred)
print("Mean Square Error: ", mse)

# Step 9: Visualize the results
plt.scatter(xtr["Frequency"], ytr, color="red", label="Data Points")  # Plot the training data points
plt.plot(xte["Frequency"], pred, color="blue", label="Regression Line")  # Plot the regression line for the testing data
plt.title('Linear Regression on Full Dataset')  # Title of the plot
plt.xlabel('Frequency')  # X-axis label
plt.ylabel('No of Jobs')  # Y-axis label
plt.legend()  # Add a legend to the plot
plt.show()
