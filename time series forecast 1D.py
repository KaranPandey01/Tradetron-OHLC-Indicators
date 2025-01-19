import pandas as pd
import numpy as np

def time_series_forecast(data, output="tsf", forecast_period=5):
    # Create a new column for TSF values
    data['tsf'] = np.nan
    
    # Prepare data for linear regression
    n = len(data)
    sum_x = n * (n - 1) / 2
    sum_y = data['close'].sum()
    sum_xy = (data.index * data['close']).sum()
    sum_xx = (data.index * data.index).sum()
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n
    
    # Forecast using TSF
    for i in range(n, n + forecast_period):
        tsf_value = slope * i + intercept
        data.loc[i, 'tsf'] = tsf_value
    
    if output == 'tsf':
        return data['tsf']
    elif output == 'signal':
        # Example: Calculate some signal based on TSF (optional)
        data['tsf_signal'] = data['tsf'] - data['close']
        return data['tsf_signal']

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate TSF using the 'close' column
tsf_series = time_series_forecast(data)

# Print the TSF series
print("TSF Series:\n", tsf_series)

# Calculate and print some TSF signal (example)
tsf_signal = time_series_forecast(data, output='signal')
print("TSF Signal Series:\n", tsf_signal)
