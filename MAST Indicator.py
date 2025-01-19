import pandas as pd
import numpy as np

def calculate_mast_indicator(data, ma_length=10, slope_length=5):
    # Calculate Moving Average
    data['moving_average'] = data['close'].rolling(window=ma_length).mean()
    
    # Calculate Slope of Moving Average
    data['ma_slope'] = data['moving_average'].diff(slope_length) / slope_length
    
    # MAST Indicator: 1 if slope is positive, -1 if slope is negative
    data['mast_indicator'] = np.where(data['ma_slope'] > 0, 1, -1)
    print(data)
    return data['mast_indicator']

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate MAST Indicator
mast_indicator = calculate_mast_indicator(data)

# Print the MAST Indicator series
print("MAST Indicator:\n", mast_indicator)
