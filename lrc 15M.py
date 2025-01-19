import pandas as pd
import numpy as np

def calculate_lrc(data, period=14, num_sd=2):
    # Ensure data is a DataFrame with 'close' prices
    if 'close' not in data.columns:
        raise ValueError("Data must contain 'close' prices")

    lrl = []
    upper_channel = []
    lower_channel = []

    for i in range(len(data)):
        if i >= period - 1:
            y = data['close'][i-period+1:i+1]
            x = np.arange(period)
            
            # Calculate slope and intercept for the linear regression line
            x_mean = np.mean(x)
            y_mean = np.mean(y)
            slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
            intercept = y_mean - slope * x_mean
            lrl_value = intercept + slope * (period - 1)
            lrl.append(lrl_value)

            sd = np.std(y)
            upper_channel.append(lrl_value + num_sd * sd)
            lower_channel.append(lrl_value - num_sd * sd)
        else:
            lrl.append(np.nan)
            upper_channel.append(np.nan)
            lower_channel.append(np.nan)

    data['LRL'] = lrl
    data['Upper Channel'] = upper_channel
    data['Lower Channel'] = lower_channel
    print(data)
    return data

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_15m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate LRC using 'close' prices
lrc_data = calculate_lrc(data, period=14, num_sd=2)

# Print the LRC series
print("LRC Data:\n", lrc_data[['LRL', 'Upper Channel', 'Lower Channel']])
