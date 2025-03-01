import math
import matplotlib.pyplot as plt

# Calculating Relative Humidity
def CalcHumidity(airTemp, dewPointTemp):
    top = math.exp( (17.625 * dewPointTemp) / (243.04 + dewPointTemp) )
    bottom = math.exp( (17.625 * airTemp) / (243.04 + airTemp) )
    newHumidity = (top / bottom) * 100
    return newHumidity

# Degree to Fareignheight for heat index formula
def CelToFah(airTemp):
    return(airTemp * 9/5) + 32

# Calculating corresponding Heat Index
def CalcHeatIndex(airTemp, newHumidity):
    airTemp = CelToFah(airTemp)
    calculatedIndex = -42.379 + 2.04901523 * airTemp + 10.14333127 * newHumidity - 0.22475541 * airTemp * newHumidity - 0.00683783 * (airTemp**2) - 0.05481717 * (newHumidity**2) + 0.00122874*(airTemp**2) * newHumidity + 0.00085282 * airTemp * (newHumidity**2) - 0.00000199 * (airTemp **2) * (newHumidity**2)
    return calculatedIndex

# Data given by M3
data = [
    {"Time": "0000", "Temp_C": 21.1, "DewPoint_C": 12.8},
    {"Time": "0100", "Temp_C": 18.9, "DewPoint_C": 12.8},
    {"Time": "0200", "Temp_C": 17.8, "DewPoint_C": 12.2},
    {"Time": "0300", "Temp_C": 17.2, "DewPoint_C": 12.2},
    {"Time": "0400", "Temp_C": 17.2, "DewPoint_C": 11.1},
    {"Time": "0500", "Temp_C": 16.1, "DewPoint_C": 11.1},
    {"Time": "0600", "Temp_C": 18.9, "DewPoint_C": 13.9},
    {"Time": "0700", "Temp_C": 25.0, "DewPoint_C": 12.2},
    {"Time": "0800", "Temp_C": 27.8, "DewPoint_C": 11.1},
    {"Time": "0900", "Temp_C": 32.2, "DewPoint_C": 11.1},
    {"Time": "1000", "Temp_C": 33.9, "DewPoint_C": 11.1},
    {"Time": "1100", "Temp_C": 36.1, "DewPoint_C": 12.2},
    {"Time": "1200", "Temp_C": 37.2, "DewPoint_C": 10.0},
    {"Time": "1300", "Temp_C": 37.2, "DewPoint_C": 11.1},
    {"Time": "1400", "Temp_C": 37.2, "DewPoint_C": 12.8},
    {"Time": "1500", "Temp_C": 35.0, "DewPoint_C": 13.9},
    {"Time": "1600", "Temp_C": 35.0, "DewPoint_C": 13.9},
    {"Time": "1700", "Temp_C": 32.8, "DewPoint_C": 12.8},
    {"Time": "1800", "Temp_C": 32.8, "DewPoint_C": 12.8},
    {"Time": "1900", "Temp_C": 32.2, "DewPoint_C": 12.8},
    {"Time": "2000", "Temp_C": 27.8, "DewPoint_C": 15.0},
    {"Time": "2100", "Temp_C": 27.8, "DewPoint_C": 15.0},
    {"Time": "2200", "Temp_C": 27.2, "DewPoint_C": 15.0},
    {"Time": "2300", "Temp_C": 26.1, "DewPoint_C": 16.1}
]

allTimes = []
HIValues = []
RelativeHumidityVals = []

for set in data:
    airTemp = set["Temp_C"]
    dewPointTemp = set["DewPoint_C"]
    eachTime = set["Time"]


    newHumidity = CalcHumidity(airTemp, dewPointTemp)

    newHeatIndex = CalcHeatIndex(airTemp, newHumidity)

    allTimes.append(eachTime)
    HIValues.append(newHeatIndex)
    RelativeHumidityVals.append(newHumidity)

plt.figure(figsize=(10,6))
plt.plot(allTimes, HIValues, marker ="x")
plt.xlabel("Time")
plt.ylabel("Heat Index (F)")
plt.show()
