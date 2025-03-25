# M3 Mathworks Modelling Challenge

In 2025 Kirish and I participated in the M3 math modelling
challenge. The problem statements and data can be found
[here](https://m3challenge.siam.org/wp-content/uploads/M3-Challenge-PROBLEM_2025.pdf)

All of the code, LaTeX and the final report can be viewed here! Here's a brief summary:

Q1: Hot to Go
- Used multivariate polynomial regression of degree 3 to model indoor temperatures
- Incorporated global warming rate of 0.06°C per decade since 1850
- Fitted the model against M3 dataset and produced hourly temperature predictions with 1-2°C accuracy

Q2: Power Hungry
- Applied Holt-Winters Exponential smoothing model to predict energy consumption
- Created separate models for domestic and non-domestic energy consumption
- Used proportion factor (χ = 0.081) to estimate summer month consumption from annual data

Q3: Beat the Heat
- Implemented Heat Index (γ) as vulnerability score for neighborhoods
- Calculated Relative Humidity (ε) using dew point and temperature data
- Used these metrics to identify high-risk areas and suggest power allocation strategies during heat waves
