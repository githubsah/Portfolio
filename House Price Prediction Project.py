# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 2: Load Your Excel File
excel_file_name = r"E:\CODE\RESEARCH\Project\house data.xlsx"
df = pd.read_excel(excel_file_name, header=1)  # Use second row as header
print(f"Loaded data from: {excel_file_name}\n")

# Optional: Rename columns for easier access
df.rename(columns={
    'Area (sqft)': 'Area',
    'Rooms': 'RM',
    'Price (Lakhs)': 'PRICE'
}, inplace=True)

# Optional: Drop unused columns
df.drop(columns=['S.No', 'Location', 'Near Metro', 'Age (years)'], inplace=True, errors='ignore')

# Display first few rows and summary statistics
print(df.head())
print(df.describe())
print("\nColumns in dataset:", df.columns)

# Create plots directory if it doesn't exist
plots_dir = os.path.join(os.path.dirname(excel_file_name), "plots")
os.makedirs(plots_dir, exist_ok=True)

# Step 3: Visualize Some Data

# Plot 1: RM vs PRICE
plt.figure(figsize=(10, 6))
plt.scatter(df['RM'], df['PRICE'], color='blue', label='Data Points')
plt.xlabel('Average Number of Rooms (RM)')
plt.ylabel('House Price (Lakhs)')
plt.title('Average Rooms vs House Price')
plt.legend()
plt.savefig(os.path.join(plots_dir, "rm_vs_price.png"))
plt.show()

# Plot 2: Area Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Area'], bins=30, color='green', edgecolor='black')
plt.title('Area Distribution')
plt.xlabel('Area (sqft)')
plt.ylabel('Frequency')
plt.savefig(os.path.join(plots_dir, "area_distribution.png"))
plt.show()

# Step 4: Prepare Data for Modeling
X = df[['RM']]  # Feature (Independent variable)
y = df['PRICE']  # Target (Dependent variable)

# Splitting into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Simple Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Print the predictions
print("\nPredictions:", y_pred)

# Step 7: Visualize Predictions
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, y_pred, color='red', label='Predicted Prices')
plt.xlabel('Average Number of Rooms (RM)')
plt.ylabel('House Price (Lakhs)')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.savefig(os.path.join(plots_dir, "actual_vs_predicted.png"))
plt.show()

# Step 8: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse}")
