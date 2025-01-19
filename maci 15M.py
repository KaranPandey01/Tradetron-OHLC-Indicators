import pandas as pd
import numpy as np

def calculate_maci(data, length=20):
    data['ma'] = data['close'].rolling(window=length).mean()
    data['upper_channel'] = data['ma'] + 2 * data['close'].rolling(window=length).std()
    data['lower_channel'] = data['ma'] - 2 * data['close'].rolling(window=length).std()
    print(data)
    return data[['ma', 'upper_channel', 'lower_channel']]

def relative_vigor_index(data, output="maci", length=10):
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
    
    data["maci"] = data["numerator"].rolling(window=length).mean() / data["denominator"].rolling(window=length).mean()
    
    data["i"] = data["maci"].shift(1)
    data["j"] = data["maci"].shift(2)
    data["k"] = data["maci"].shift(3)
    
    data["maci_signal"] = (data["maci"] + (2 * data["i"]) + (2 * data["j"]) + data["k"]) / 6
    
    if output == 'maci':
        return calculate_maci(data)
    elif output == 'signal':
        return data['maci_signal']

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_15m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate MACI using the 'close' column
maci_data = relative_vigor_index(data, output='maci')

# Print the MACI data
print("MACI Data:\n", maci_data)

# Calculate MACI signal
maci_signal = relative_vigor_index(data, output='signal')

# Print the MACI signal
print("MACI Signal:\n", maci_signal)
