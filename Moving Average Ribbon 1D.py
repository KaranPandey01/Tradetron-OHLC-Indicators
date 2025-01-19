import pandas as pd
import numpy as np

def calculate_moving_average_ribbon(data, ma_periods):
    for period in ma_periods:
        data[f'MA_{period}'] = data['close'].rolling(window=period).mean()
        print(data)
    return data

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Define periods for Moving Averages in the Ribbon
ma_periods = [10, 20, 30, 40, 50]  # Example periods, adjust as needed

# Calculate Moving Average Ribbon
data = calculate_moving_average_ribbon(data, ma_periods)

# Plotting Moving Average Ribbon using Pandas built-in plot function
data.plot(y=['close'] + [f'MA_{period}' for period in ma_periods], figsize=(14, 7), title='Moving Average Ribbon')
