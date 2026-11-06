
import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 6 rows
data = np.random.randint(1, 100, size=(6, 3))

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Create a new column using a lambda function
df['Total'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)

# Display the updated DataFrame
print("\nDataFrame After Adding Total Column:")
print(df)
