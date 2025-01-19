import pandas as pd
import numpy as np

def calculate_demark_pivots(data):
    def demark_pivot(row):
        if row['close'] < row['open']:
            X = row['high'] + (2 * row['low']) + row['close']
        elif row['close'] > row['open']:
            X = (2 * row['high']) + row['low'] + row['close']
        else:
            X = row['high'] + row['low'] + (2 * row['close'])
        
        PP = X / 4
        R1 = X / 2 - row['low']
        S1 = X / 2 - row['high']
        
        return pd.Series([PP, R1, S1])

    pivots = data.apply(demark_pivot, axis=1)
    pivots.columns = ['PP', 'R1', 'S1']
    print(data)
    return data.join(pivots)

file_path = 'C:/Users/Karan Pandey/Downloads/RELIANCE_1m_aws (1).csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format and set as the index
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

# Reset index to start from 0
data.reset_index(drop=True, inplace=True)

# Calculate DeMark pivot points using 'open', 'high', 'low', 'close' prices
demark_pivots_data = calculate_demark_pivots(data)

# Print the DeMark pivot points series
print("DeMark Pivot Points Data:\n", demark_pivots_data[['PP', 'R1', 'S1']])
