import pandas as pd
import numpy as np

def true_strength_indicator(data, ema1=25, ema2=13):
    # Calculate price changes
    price_change = data['close'].diff(1)
    
    # Calculate absolute price change
    abs_price_change = abs(price_change)
    
    # Calculate EMA1 and EMA2
    ema_price_change = price_change.ewm(span=ema1).mean()
    ema_abs_price_change = abs_price_change.ewm(span=ema2).mean()
    
    # Calculate TSI
    tsi = ema_price_change / ema_abs_price_change
    print(data)
    return tsi

# Example usage
if __name__ == "__main__":
    file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
    data = pd.read_csv(file_path)
    
    # Ensure the 'date' column is in datetime format and set as the index
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)
    
    # Reset index to start from 0
    data.reset_index(drop=True, inplace=True)
    
    # Calculate TSI using 'close' prices
    true_strength_series = true_strength_indicator(data)
    print("True Strength Indicator (TSI) Series:\n", true_strength_series)
