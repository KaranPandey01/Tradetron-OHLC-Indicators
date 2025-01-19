import pandas as pd
import numpy as np

def calculate_super_trend(data, period=7, multiplier=3):
    data['tr'] = np.max([data['high'] - data['low'], 
                         abs(data['high'] - data['close'].shift()), 
                         abs(data['low'] - data['close'].shift())], axis=0)
    
    data['atr'] = data['tr'].rolling(window=period).mean()
    
    data['upper_band'] = (data['high'] + data['low']) / 2 + multiplier * data['atr']
    data['lower_band'] = (data['high'] + data['low']) / 2 - multiplier * data['atr']
    
    data['in_uptrend'] = True
    for current in range(1, len(data)):
        previous = current - 1
        if data['close'][current] > data['upper_band'][previous]:
            data['in_uptrend'].iat[current] = True
        elif data['close'][current] < data['lower_band'][previous]:
            data['in_uptrend'].iat[current] = False
        else:
            data['in_uptrend'].iat[current] = data['in_uptrend'].iat[previous]
            if data['in_uptrend'].iat[current] and data['lower_band'][current] < data['lower_band'][previous]:
                data['lower_band'].iat[current] = data['lower_band'][previous]
            if not data['in_uptrend'].iat[current] and data['upper_band'][current] > data['upper_band'][previous]:
                data['upper_band'].iat[current] = data['upper_band'][previous]
    
    data['super_trend'] = np.where(data['in_uptrend'], data['lower_band'], data['upper_band'])
    print(data) 
    return data['super_trend']

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Super Trend using the 'close', 'high', 'low' columns
super_trend_series = calculate_super_trend(data)

# Print the Super Trend series
print("Super Trend Series:\n", super_trend_series)
