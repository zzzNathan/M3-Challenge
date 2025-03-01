import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Create the DataFrame with the provided data
data = pd.DataFrame({
    "Year": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
    "Domestic Consumption": [1424117394, 1525486540, 1609229857, 1535046668, 1551441077,
                             1584877006, 1602218919, 1632646065, 1650323202, 1632305132, 1663571950],
    "Non-Domestic Consumption": [1896047335, 1893143269, 1805655202, 2124916982, 2172490874,
                                 2159883548, 2012774683, 1954766502, 1890155436, 1927600374, 1862786430]
})

# Constant of propotionality (refer to paper)
CHI = 0.081
data["Domestic Consumption"]     *= CHI
data["Non-Domestic Consumption"] *= CHI

# Sort the data by Year and set Year as index
data = data.sort_values("Year")
data.set_index("Year", inplace=True)

# Fit Holt-Winters models for each consumption type
domestic_model = ExponentialSmoothing(
    data["Domestic Consumption"],
    trend='add',      # Additive trend since the data is annual
    seasonal=None,    # No seasonal component for annual data
    initialization_method="estimated"
).fit()

nondomestic_model = ExponentialSmoothing(
    data["Non-Domestic Consumption"],
    trend='add',
    seasonal=None,
    initialization_method="estimated"
).fit()

# Compute the fitted values for each model and sum them to get the combined (total) fitted values
data["Total Fitted"] = domestic_model.fittedvalues + nondomestic_model.fittedvalues

# Also, calculate the actual total consumption for comparison
data["Total Actual"] = data["Domestic Consumption"] + data["Non-Domestic Consumption"]

# Forecast the next 20 years using both models and sum their forecasts
forecast_steps = 20
domestic_forecast = domestic_model.forecast(steps=forecast_steps)
nondomestic_forecast = nondomestic_model.forecast(steps=forecast_steps)
total_forecast = domestic_forecast + nondomestic_forecast

# Create a new index for the forecast years (assuming years continue consecutively)
forecast_years = list(range(data.index[-1] + 1, data.index[-1] + forecast_steps + 1))

# Plot the actual total consumption, the fitted total consumption, and the forecast
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Total Actual"], label="Actual Total Consumption", marker='o')
plt.plot(data.index, data["Total Fitted"], label="Fitted Total Consumption", linestyle="--")
plt.plot(forecast_years, total_forecast, label="Forecast Total Consumption", marker='o', linestyle="--")
plt.xlabel("Year")
plt.ylabel("Total Consumption")
plt.title("Total Consumption (Domestic + Non-Domestic) with Holt-Winters Forecast")
plt.legend()
plt.show()

# Print the forecast values
print("Forecast for Total Consumption for the next 20 years:")
print(total_forecast)
