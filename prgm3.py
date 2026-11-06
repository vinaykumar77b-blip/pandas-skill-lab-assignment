
import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 5 rows
data = np.random.randint(1, 100, size=(5, 3))

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Introduce some NaN values
df.loc[1, 'A'] = np.nan
df.loc[3, 'B'] = np.nan
df.loc[2, 'C'] = np.nan

# Display DataFrame with missing values
print("DataFrame with NaN values:")
print(df)

# Fill NaN values with column means
df = df.fillna(df.mean())

# Display the updated DataFrame
print("\nDataFrame after filling NaN values:")
print(df)
