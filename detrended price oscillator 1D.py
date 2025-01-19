import pandas as pd
import numpy as np

def detrended_price_oscillator(data, output="dpo", period=20):
    data["sma"] = data["close"].rolling(window=period).mean()
    data["dpo"] = data["close"] - data["sma"].shift(int(period / 2) + 1)
    data.drop(columns=["sma"], inplace=True)
    
    if output == 'dpo':
        print(data)
        return data['dpo']

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate DPO using the 'close' column and a period of 20
dpo_series = detrended_price_oscillator(data)

# Print the DPO series
print("Detrended Price Oscillator (DPO) Series:\n", dpo_series)
