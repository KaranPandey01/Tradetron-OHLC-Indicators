import pandas as pd
import numpy as np

def williams_fractal(data, length=2):
    # Calculate Fractal Up
    data['fractal_up'] = np.where((data['high'] > data['high'].shift(length)) & 
                                  (data['high'] > data['high'].shift(length + 1)) &
                                  (data['high'] > data['high'].shift(length + 2)) &
                                  (data['high'] > data['high'].shift(length + 3)) &
                                  (data['high'] > data['high'].shift(length + 4)),
                                  data['high'], np.nan)
    
    # Calculate Fractal Down
    data['fractal_down'] = np.where((data['low'] < data['low'].shift(length)) & 
                                    (data['low'] < data['low'].shift(length + 1)) &
                                    (data['low'] < data['low'].shift(length + 2)) &
                                    (data['low'] < data['low'].shift(length + 3)) &
                                    (data['low'] < data['low'].shift(length + 4)),
                                    data['low'], np.nan)
    
    return data[['fractal_up', 'fractal_down']]

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
    
    if output == 'rvgi':
        return data['rvgi']
    elif output == 'signal':
        return data['rvgi']  # RVGI typically doesn't have a signal based on its own moving average

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
    
    # Calculate Williams Fractal Indicator
    fractal_data = williams_fractal(data)
    
    # Print the Williams Fractal Indicator data
    print("Williams Fractal Indicator:\n", fractal_data)
    
    # Calculate RVGI using the 'close', 'open', 'high', 'low' columns
    rvgi_series = relative_vigor_index(data)
    
    # Print the RVGI series
    print("\nRVGI Series:\n", rvgi_series)
    
    # Note: RVGI typically doesn't have a signal based on its own moving average
