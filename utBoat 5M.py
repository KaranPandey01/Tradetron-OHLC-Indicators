import pandas as pd
import numpy as np

def ut_boat(data, period=14):
    # Implement your custom UT Boat indicator here
    # This might involve proprietary calculations or a specific logic not publicly defined.
    # Below is a placeholder for demonstration.
    ut_boat = data['close'].rolling(window=period).mean()  # Placeholder logic
    print(data)
    return ut_boat

# Example usage
if __name__ == "__main__":
    file_path = r'c:\Users\Karan Pandey\Downloads\RELIANCE_5m_aws (1).csv'
    data = pd.read_csv(file_path)
    
    # Ensure the 'date' column is in datetime format and set as the index
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)
    
    # Reset index to start from 0
    data.reset_index(drop=True, inplace=True)
    
    # Calculate UT Boat using 'close' prices
    ut_boat_series = ut_boat(data)
    print("UT Boat Series:\n", ut_boat_series)
