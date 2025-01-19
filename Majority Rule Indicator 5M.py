import pandas as pd
import numpy as np

def majority_rule_indicator(data, length=10):
    length = int(length)
    data['close_shifted'] = data['close'].shift(1)
    data['gain'] = np.where(data['close'] > data['close_shifted'], 1, 0)
    data['loss'] = np.where(data['close'] < data['close_shifted'], -1, 0)
    data['majority_rule'] = data['gain'].rolling(window=length).sum() / length - data['loss'].rolling(window=length).sum() / length
    print(data)
    return data['majority_rule']

file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_5m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate Majority Rule Indicator
majority_rule = majority_rule_indicator(data)

# Print the Majority Rule Indicator series
print("Majority Rule Indicator Series:\n", majority_rule)
