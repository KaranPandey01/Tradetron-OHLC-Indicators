import pandas as pd
import numpy as np

def chaikin_volatility(data, length=10):
    close_prices = data['close']
    high_prices = data['high']
    low_prices = data['low']
    
    # Calculate Money Flow Multiplier
    mf_multiplier = ((close_prices - low_prices) - (high_prices - close_prices)) / (high_prices - low_prices)
    
    # Calculate Money Flow Volume
    mf_volume = mf_multiplier * data['volume']
    
    # Calculate Chaikin Volatility
    data['chaikin_volatility'] = mf_volume.rolling(window=length).std() / mf_volume.rolling(window=length).mean()
    print(data)
    return data['chaikin_volatility']

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_5m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Chaikin Volatility
chaikin_volatility_series = chaikin_volatility(data)

# Print the Chaikin Volatility series
print("Chaikin Volatility Series:\n", chaikin_volatility_series)
