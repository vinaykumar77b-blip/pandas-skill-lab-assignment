
import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 5 rows
data = np.random.randint(1, 100, size=(5, 3))

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Add a new column containing the product of the first two columns
df['Product'] = df['A'] * df['B']

# Display the DataFrame
print("Original DataFrame with Product Column:")
print(df)
