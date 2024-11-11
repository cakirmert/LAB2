import pandas as pd

# Load the data, making sure we interpret commas as decimal points
data = pd.read_csv('mosfet_simulation_data.csv', delimiter=';', decimal=',')

# Save back to a new CSV file with proper decimal points for Python and MATLAB
data.to_csv('mosfet_simulation_data_converted.csv', index=False)
