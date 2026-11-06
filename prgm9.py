
import pandas as pd
import numpy as np

# Create a MultiIndex
index = pd.MultiIndex.from_tuples(
    [
        ('A', 'A1'), ('A', 'A1'),
        ('A', 'A2'), ('A', 'A2'),
        ('B', 'B1'), ('B', 'B1'),
        ('B', 'B2'), ('B', 'B2'),
        ('C', 'C1'), ('C', 'C1'),
        ('C', 'C2'), ('C', 'C2')
    ],
    names=['Category', 'SubCategory']
)

# Create a DataFrame with random values
df = pd.DataFrame(
    {'Value': np.random.randint(10, 100, size=12)},
    index=index
)

# Display the original DataFrame
print("MultiIndex DataFrame:")
print(df)

# Calculate the sum for each Category and SubCategory
result = df.groupby(level=['Category', 'SubCategory']).sum()

# Display the result
print("\nSum of Values for Each Category and SubCategory:")
print(result)
