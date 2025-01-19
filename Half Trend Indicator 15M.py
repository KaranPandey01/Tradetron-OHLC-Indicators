import pandas as pd
import numpy as np

def half_trend_indicator(data, length=10):
    data['high_price'] = data['high'].rolling(window=length).max()
    data['low_price'] = data['low'].rolling(window=length).min()
    data['half_trend'] = (data['high_price'] + data['low_price']) / 2
    data['half_trend_signal'] = np.where(data['close'] > data['half_trend'], 1, -1)
    print(data)
    return data['half_trend_signal']

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_15M_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Half Trend Indicator
half_trend_signal = half_trend_indicator(data)

# Print the Half Trend Indicator signal series
print("Half Trend Indicator Signal Series:\n", half_trend_signal)
