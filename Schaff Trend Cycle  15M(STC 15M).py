import pandas as pd
import numpy as np

def schaff_trend_cycle(data, period1=23, period2=50, signal_period=10):
    # Calculate EMA1 and EMA2
    ema1 = data['close'].ewm(span=period1, min_periods=period1).mean()
    ema2 = data['close'].ewm(span=period2, min_periods=period2).mean()
    
    # Calculate MACD Line
    macd_line = ema1 - ema2
    
    # Calculate Signal Line
    signal_line = macd_line.ewm(span=signal_period, min_periods=signal_period).mean()
    
    # Calculate STC
    high_macd = macd_line.rolling(window=period2).max()
    low_macd = macd_line.rolling(window=period2).min()
    stc = 100 * (macd_line - signal_line) / (high_macd - low_macd)
    print(data)
    return stc

# Example usage
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_15m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate STC using 'close' prices
stc_series = schaff_trend_cycle(data)
print("Schaff Trend Cycle (STC) Series:\n", stc_series)
