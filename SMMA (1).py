import pandas as pd
import numpy as np

def smoothed_moving_average(data_series, length=10):
    length = int(length)
    smma = data_series.rolling(window=length).mean()
    print(data)
    return smma

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate SMMA using the 'close' column
smma_series = smoothed_moving_average(data['close'])

# Print the SMMA series
print("SMMA Series:\n", smma_series)
