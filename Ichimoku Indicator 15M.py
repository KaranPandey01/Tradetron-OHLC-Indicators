import pandas as pd

def calculate_ichimoku_cloud(data, tenkan_period=9, kijun_period=26, senkou_span_b_period=52):
    # Tenkan-sen (Conversion Line)
    data['tenkan_sen'] = (data['high'].rolling(window=tenkan_period).max() + data['low'].rolling(window=tenkan_period).min()) / 2

    # Kijun-sen (Base Line)
    data['kijun_sen'] = (data['high'].rolling(window=kijun_period).max() + data['low'].rolling(window=kijun_period).min()) / 2

    # Senkou Span A (Leading Span A)
    data['senkou_span_a'] = ((data['tenkan_sen'] + data['kijun_sen']) / 2).shift(kijun_period)

    # Senkou Span B (Leading Span B)
    data['senkou_span_b'] = ((data['high'].rolling(window=senkou_span_b_period).max() + data['low'].rolling(window=senkou_span_b_period).min()) / 2).shift(kijun_period)
    print(data)

    return data[['tenkan_sen', 'kijun_sen', 'senkou_span_a', 'senkou_span_b']]

# Example usage
file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_15m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Ichimoku Cloud using the 'high' and 'low' columns
ichimoku_cloud_data = calculate_ichimoku_cloud(data)

# Print the Ichimoku Cloud data
print("Ichimoku Cloud Data:\n", ichimoku_cloud_data)
