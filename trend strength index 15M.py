import pandas as pd
import numpy as np

def trend_strength_index(data, r1=25, r2=13):
    # Calculate price changes
    price_change = data['close'].diff(1)
    
    # Calculate absolute price change
    abs_price_change = abs(price_change)
    
    # Calculate SMA1 and SMA2
    sma1 = price_change.rolling(window=r1).mean()
    sma2 = abs_price_change.rolling(window=r2).mean()
    
    # Calculate TSI
    tsi = 100 * (sma1 / sma2)
    print(data)
    return tsi

# Example usage
if __name__ == "__main__":
    file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_15m_aws (1).csv'
    data = pd.read_csv(file_path)
    
    # Ensure the 'date' column is in datetime format and set as the index
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)
    
    # Reset index to start from 0
    data.reset_index(drop=True, inplace=True)
    
    # Calculate TSI using 'close' prices
    tsi_series = trend_strength_index(data)
    print("Trend Strength Index (TSI) Series:\n", tsi_series)
