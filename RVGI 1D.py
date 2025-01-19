import pandas as pd
import numpy as np

def relative_vigor_index(data, output="rvgi", length=10):
    length = int(length)
    data["a"] = data["close"] - data["open"]
    data["b"] = data["close"].shift(1) - data["open"].shift(1)
    data["c"] = data["close"].shift(2) - data["open"].shift(2)
    data["d"] = data["close"].shift(3) - data["open"].shift(3)
    data["e"] = data["high"] - data["low"]
    data["f"] = data["high"].shift(1) - data["low"].shift(1)
    data["g"] = data["high"].shift(2) - data["low"].shift(2)
    data["h"] = data["high"].shift(3) - data["low"].shift(3)
    
    data["numerator"] = (data["a"] + (2 * data["b"]) + (2 * data["c"]) + data["d"]) / 6
    data["denominator"] = (data["e"] + (2 * data["f"]) + (2 * data["g"]) + data["h"]) / 6
    
    data["rvgi"] = data["numerator"].rolling(window=length).mean() / data["denominator"].rolling(window=length).mean()
    
    data["i"] = data["rvgi"].shift(1)
    data["j"] = data["rvgi"].shift(2)
    data["k"] = data["rvgi"].shift(3)
    
    data["rvgi_signal"] = (data["rvgi"] + (2 * data["i"]) + (2 * data["j"]) + data["k"]) / 6
    
    if output == 'rvgi':
        print(data)
        return data['rvgi']
    elif output == 'signal':
        print(data)
        return data['rvgi_signal']

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate RVGI using the 'close', 'open', 'high', 'low' columns
rvgi_series = relative_vigor_index(data)

# Print the RVGI series
print("RVGI Series:\n", rvgi_series)

# Calculate RVGI signal
rvgi_signal = relative_vigor_index(data, output='signal')

# Print the RVGI signal series
print("RVGI Signal Series:\n", rvgi_signal)
