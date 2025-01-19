import pandas as pd
import numpy as np

def zigzag_indicator(data_series, threshold_percent=5):
    zigzag_highs = []
    zigzag_lows = []
    
    current_high = data_series.iloc[0]
    current_low = data_series.iloc[0]
    
    for i in range(1, len(data_series)):
        price = data_series.iloc[i]
        
        if price >= current_high * (1 + threshold_percent / 100):
            zigzag_highs.append((i, price))
            current_high = price
            current_low = price
        
        elif price <= current_low * (1 - threshold_percent / 100):
            zigzag_lows.append((i, price))
            current_low = price
            current_high = price
    print(data)
    return zigzag_highs, zigzag_lows

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_5m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Zigzag highs and lows using the 'close' column
zigzag_highs, zigzag_lows = zigzag_indicator(data['close'])

# Replace RVGI with Zigzag indicator (assuming you want to replace RVGI)
data['zigzag_highs'] = np.nan
data['zigzag_lows'] = np.nan

for idx, price in zigzag_highs:
    data.at[idx, 'zigzag_highs'] = price

for idx, price in zigzag_lows:
    data.at[idx, 'zigzag_lows'] = price

# Print the Zigzag highs and lows
print("Zigzag Highs:\n", data['zigzag_highs'].dropna())
print("\nZigzag Lows:\n", data['zigzag_lows'].dropna())
