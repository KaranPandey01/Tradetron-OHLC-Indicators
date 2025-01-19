import pandas as pd
import numpy as np

def momentum_indicator(data, length=14):
    data['close_shifted'] = data['close'].shift(length)
    data['momentum'] = data['close'] - data['close_shifted']
    data.drop(columns=['close_shifted'], inplace=True)
    print(data)
    return data['momentum']

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Momentum Indicator
momentum = momentum_indicator(data)

# Print the Momentum Indicator series
print("Momentum Indicator:\n", momentum)
