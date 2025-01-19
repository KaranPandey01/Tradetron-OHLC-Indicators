import pandas as pd
import numpy as np

def calculate_vwap_bands(data, length=14, num_sd=2):
    data['typical_price'] = (data['high'] + data['low'] + data['close']) / 3
    data['volume_price'] = data['typical_price'] * data['volume']
    data['cumulative_volume'] = data['volume'].cumsum()
    data['cumulative_volume_price'] = data['volume_price'].cumsum()
    data['vwap'] = data['cumulative_volume_price'] / data['cumulative_volume']
    
    data['vwap_upper'] = data['vwap'] + num_sd * data['close'].rolling(window=length).std()
    data['vwap_lower'] = data['vwap'] - num_sd * data['close'].rolling(window=length).std()
    
    return data[['vwap', 'vwap_upper', 'vwap_lower']]

def relative_vigor_index(data, output="vwap", length=14, num_sd=2):
    length = int(length)
    
    # Calculate VWAP Bands
    data['typical_price'] = (data['high'] + data['low'] + data['close']) / 3
    data['volume_price'] = data['typical_price'] * data['volume']
    data['cumulative_volume'] = data['volume'].cumsum()
    data['cumulative_volume_price'] = data['volume_price'].cumsum()
    data['vwap'] = data['cumulative_volume_price'] / data['cumulative_volume']
    
    data['vwap_upper'] = data['vwap'] + num_sd * data['close'].rolling(window=length).std()
    data['vwap_lower'] = data['vwap'] - num_sd * data['close'].rolling(window=length).std()
    
    if output == 'vwap':
        return data[['vwap', 'vwap_upper', 'vwap_lower']]
    elif output == 'signal':
        # Example: Calculate some signal based on VWAP Bands
        data['vwap_signal'] = data['vwap'] - data['vwap_lower']  # Just an example signal calculation
        print(data)
        return data['vwap_signal']

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate VWAP Bands
vwap_bands = relative_vigor_index(data)

# Print the VWAP Bands
print("VWAP Bands:\n", vwap_bands)

# Calculate and print some VWAP signal (example)
vwap_signal = relative_vigor_index(data, output='signal')
print("VWAP Signal:\n", vwap_signal)
