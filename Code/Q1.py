import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Degree of our polynomial
DEG = 3

# Data given by M3
data = {
    "Time": ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM",
             "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM",
             "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"],
    "Temperature (°C)": [21.1, 18.9, 17.8, 17.2, 17.2, 16.1, 18.9, 25.0, 27.8, 32.2, 33.9, 36.1, 37.2, 37.2, 37.2, 35.0,
                         35.0, 32.8, 32.8, 32.2, 27.8, 27.8, 27.2, 26.1],
    "Dew Point (°C)": [12.8, 12.8, 12.2, 12.2, 11.1, 11.1, 13.9, 12.2, 11.1, 11.1, 11.1, 12.2, 10.0, 11.1, 12.8, 13.9, 13.9,
                       12.8, 12.8, 12.8, 15.0, 15.0, 15.0, 16.1],
    "Humidity (%)": [60, 68, 72, 72, 72, 72, 73, 44, 37, 27, 24, 23, 19, 21, 24, 28, 28, 29, 32, 32, 45, 45, 45, 48]
}

df = pd.DataFrame(data)

# We want times to be seconds after 00:00
df["Time"] = pd.to_datetime(df["Time"], format="%I:%M %p")
df["Time"] = (df["Time"] - pd.Timestamp("00:00:00")).dt.total_seconds()
df["Time"] = df["Time"].astype(int)

# Humidity % values should be in the interval [0, 1]
df["Humidity (%)"] = df["Humidity (%)"] / 100

# Prepare features (X) and target (y)
# Here, we predict Temperature based on Time, Dew Point, and Humidity
X = df[["Time", "Dew Point (°C)", "Humidity (%)"]]
y = df["Temperature (°C)"]

# Create a pipeline that first transforms the features into polynomial features
# then fits a linear regression model
model = make_pipeline(PolynomialFeatures(degree=DEG, include_bias=False), LinearRegression())

# Fit the model
model.fit(X, y)

# To see the learned coefficients, we can extract them from the LinearRegression step
lin_reg = model.named_steps['linearregression']
print("Intercept:", lin_reg.intercept_)
print("Coefficients:", lin_reg.coef_)

def Predict_Temps(new_data, year):
    # Predict on the given new_data
    y_pred_all = model.predict(new_data)

    # Apply the year adjustment
    y_pred_all_adjusted = y_pred_all + (year - 2025) * (0.006)

    # Print the predicted temperatures
    print("Predicted Temperatures:", y_pred_all_adjusted)

    # Calculate residuals using the original y for comparison
    residuals = y - y_pred_all_adjusted

    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred_all_adjusted, residuals, color='blue', alpha=0.6)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel("Predicted Temperature (°C)")
    plt.ylabel("Residuals")
    plt.title("Residuals vs. Predicted Temperature")
    plt.show()

Predict_Temps(X, 2025)
