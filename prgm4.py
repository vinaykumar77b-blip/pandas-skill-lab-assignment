
import pandas as pd
import numpy as np

# Create a DataFrame with 4 columns and 6 rows
data = np.random.randint(1, 100, size=(6, 4))

df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Introduce NaN values
df.loc[1, 'A'] = np.nan
df.loc[3, 'C'] = np.nan
df.loc[4, 'B'] = np.nan

# Display DataFrame with NaN values
print("DataFrame with NaN values:")
print(df)

# Drop rows containing any NaN values
df = df.dropna()

# Display DataFrame after dropping rows
print("\nDataFrame after dropping rows with NaN:")
print(df)

