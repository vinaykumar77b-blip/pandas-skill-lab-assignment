
import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 4 rows
data = np.random.randint(1, 100, size=(4, 3))

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Calculate row-wise sum
print("\nRow-wise Sum:")
print(df.sum(axis=1))

# Calculate column-wise sum
print("\nColumn-wise Sum:")
print(df.sum(axis=0))
