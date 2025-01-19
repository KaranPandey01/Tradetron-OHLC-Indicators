import pandas as pd
import numpy as np

def relative_volatility_index(data_series, stddev_length=10, ema_length=14):
    stddev_length = int(stddev_length)
    ema_length = int(ema_length)
    data = pd.DataFrame(data_series)
    data["stddev"] = data_series.rolling(window=stddev_length).std()
    data["change"] = data_series.diff()
    data.dropna(inplace=True)
    data["upper_condition"] = np.where(data["change"] <= 0, 0, data["stddev"])
    data["lower_condition"] = np.where(data["change"] > 0, 0, data["stddev"])
    data["upper"] = data["upper_condition"].ewm(span=ema_length, adjust=False).mean()
    data["lower"] = data["lower_condition"].ewm(span=ema_length, adjust=False).mean()
    data["rvi"] = data["upper"] / (data["upper"] + data["lower"]) * 100
    last_index = data.index[-1]
    print(data)
    return data["rvi"], last_index

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate RVI using the 'close' column
rvi_series, last_index = relative_volatility_index(data['close'])

# Get the timestamp of the last RVI value and format it to 1-minute format
if isinstance(last_index, int):
    timestamp = data.index[last_index].strftime('%Y-%m-%d %H:%M')

    # Print the last value of the RVI series and its timestamp in 1-minute format
    print(f"Last value of RVI: {rvi_series} at timestamp: {timestamp}")

