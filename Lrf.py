import pandas as pd
import numpy as np

def linear_regression_forecast(data, output="lrf", length=10):
    length = int(length)
    # Calculate Linear Regression Forecast (LRF)
    data['x'] = np.arange(len(data))  # Independent variable (time)
    data['y'] = data['close']  # Dependent variable (close price)
    
    # Calculate necessary sums and means for linear regression formula
    n = length
    sum_x = data['x'].rolling(window=n, min_periods=1).sum()
    sum_y = data['y'].rolling(window=n, min_periods=1).sum()
    sum_xy = (data['x'] * data['y']).rolling(window=n, min_periods=1).sum()
    sum_x_squared = (data['x'] ** 2).rolling(window=n, min_periods=1).sum()
    
    data['slope'] = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    data['intercept'] = (sum_y - data['slope'] * sum_x) / n
    
    # Forecast using the linear regression equation: y = intercept + slope * x
    data['lrf'] = data['intercept'] + data['slope'] * (len(data) - 1)
    
    if output == 'lrf':
        print(data)
        return data['lrf']

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate LRF using the 'close' column
lrf_series = linear_regression_forecast(data)

# Print the LRF series
print("Linear Regression Forecast (LRF) Series:\n", lrf_series)
