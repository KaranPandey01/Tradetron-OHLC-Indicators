import pandas as pd
import numpy as np

def calculate_rsi(series, period):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def updown(series):
    ud = np.zeros_like(series)
    for i in range(1, len(series)):
        if series[i] == series[i-1]:
            ud[i] = 0
        elif series[i] > series[i-1]:
            ud[i] = 1 if ud[i-1] <= 0 else ud[i-1] + 1
        else:
            ud[i] = -1 if ud[i-1] >= 0 else ud[i-1] - 1
    print(data)        
    return pd.Series(ud, index=series.index)

def percent_rank(series, period):
    rank = series.rolling(window=period).apply(lambda x: pd.Series(x).rank(pct=True).iloc[-1] * 100, raw=True)
    print(data)
    return rank

def connors_rsi(data, rsi_period=3, updown_length=2, len_roc=100):
    data['rsi'] = calculate_rsi(data['close'], rsi_period)
    data['updown'] = updown(data['close'])
    data['updown_rsi'] = calculate_rsi(data['updown'], updown_length)
    data['roc'] = data['close'].pct_change(periods=1) * 100
    data['percentrank'] = percent_rank(data['roc'], len_roc)
    
    data['crsi'] = (data['rsi'] + data['updown_rsi'] + data['percentrank']) / 3
    print(data)
    return data['crsi']

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Connors RSI using 'close' prices and length=10
crsi_series = connors_rsi(data, rsi_period=3, updown_length=2, len_roc=100)

# Print the Connors RSI series
print("Connors RSI Series:\n", crsi_series)
