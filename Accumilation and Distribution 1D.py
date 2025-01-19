import pandas as pd
import numpy as np

def accumulation_distribution(data):
    # Calculate Money Flow Multiplier (MFM)
    mfm = ((data['close'] - data['low']) - (data['high'] - data['close'])) / (data['high'] - data['low'])
    
    # Calculate Money Flow Volume (MFV)
    data['mfv'] = mfm * data['volume']
    
    # Calculate Accumulation Distribution Line (ADL)
    data['adl'] = data['mfv'].cumsum()
    print(data)
    return data['adl']

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_day_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate ADL using 'close' prices and 'volume'
adl_series = accumulation_distribution(data)

# Print the ADL series
print("Accumulation Distribution Line (ADL) Series:\n", adl_series)
