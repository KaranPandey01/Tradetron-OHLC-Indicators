import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def relative_volatility_index(data_series, stddev_length=10, ema_length=14):
    stddev_length = int(stddev_length)
    ema_length = int(ema_length)
    data = pd.DataFrame(data_series, columns=['close'])
    data["stddev"] = data_series.rolling(window=stddev_length).std()
    data["change"] = data_series.diff()
    data.dropna(inplace=True)
    data["upper_condition"] = np.where(data["change"] <= 0, 0, data["stddev"])
    data["lower_condition"] = np.where(data["change"] > 0, 0, data["stddev"])
    data["upper"] = data["upper_condition"].ewm(span=ema_length, adjust=False).mean()
    data["lower"] = data["lower_condition"].ewm(span=ema_length, adjust=False).mean()
    data["rvi"] = data["upper"] / (data["upper"] + data["lower"]) * 100
    print(data)
    return data["rvi"]

def moving_average(source, length, ma_type, bb_mult):
    if ma_type == "SMA":
        return source.rolling(window=length).mean(), None, None
    elif ma_type == "Bollinger Bands":
        middle = source.rolling(window=length).mean()
        std = source.rolling(window=length).std()
        upper = middle + (std * bb_mult)
        lower = middle - (std * bb_mult)
        return middle, upper, lower
    elif ma_type == "EMA":
        return source.ewm(span=length, adjust=False).mean(), None, None
    elif ma_type == "SMMA (RMA)":
        # Custom implementation of SMMA
        smma = source.copy()
        smma.iloc[length-1] = source.iloc[:length].mean()  # Initial value is a simple moving average
        for i in range(length, len(source)):
            smma.iloc[i] = (smma.iloc[i-1] * (length - 1) + source.iloc[i]) / length
        return smma, None, None
    elif ma_type == "WMA":
        weights = np.arange(1, length + 1)
        wma = source.rolling(window=length).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)
        return wma, None, None
    elif ma_type == "VWMA":
        vwap = (source * source).rolling(window=length).sum() / source.rolling(window=length).sum()  # VWAP approximation
        return vwap, None, None
    else:
        raise ValueError("Invalid MA Type")

# Load data
file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_5m_aws (1).csv'
data = pd.read_csv(file_path)

# Assuming the data has a date column for the index
if 'date' in data.columns:
    data.set_index('date', inplace=True)

# Parameters
length = 10
offset = 0
ma_type = "SMA"  # Options: "SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"
ma_length = 14
bb_mult = 2.0

# Calculate RVI
rvi_series = relative_volatility_index(data['close'], stddev_length=length, ema_length=ma_length)
data['rvi'] = rvi_series

# Calculate RVI-based MA and Bollinger Bands
data['rvi_ma'], data['bb_upper'], data['bb_lower'] = moving_average(data['rvi'], ma_length, ma_type, bb_mult)

# Plotting
plt.figure(figsize=(14, 7))

# Plot RVI and RVI-based MA
plt.plot(data.index, data['rvi'], label='RVI', color='#7E57C2')
plt.plot(data.index, data['rvi_ma'], label='RVI-based MA', color='yellow')

# Plot Bollinger Bands if selected
if ma_type == "Bollinger Bands":
    plt.plot(data.index, data['bb_upper'], label='Upper Bollinger Band', color='green')
    plt.plot(data.index, data['bb_lower'], label='Lower Bollinger Band', color='green')
    plt.fill_between(data.index, data['bb_upper'], data['bb_lower'], color='green', alpha=0.1)

# Plot Upper and Lower Bands
plt.axhline(80, color='#787B86', linestyle='--', label='Upper Band')
plt.axhline(50, color='#787B86', linestyle='--', alpha=0.5, label='Middle Band')
plt.axhline(20, color='#787B86', linestyle='--', label='Lower Band')
plt.fill_between(data.index, 20, 80, color='#7E57C2', alpha=0.1)

plt.title("Relative Volatility Index (RVI)")
plt.legend()
plt.show()

print("Last value of RVI:", rvi_series)
