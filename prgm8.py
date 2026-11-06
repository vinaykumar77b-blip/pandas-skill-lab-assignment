
import pandas as pd

# Create a MultiIndex
index = pd.MultiIndex.from_tuples(
    [
        ('A', 'A1'),
        ('A', 'A2'),
        ('B', 'B1'),
        ('B', 'B2'),
        ('C', 'C1'),
        ('C', 'C2')
    ],
    names=['Category', 'SubCategory']
)

# Create a DataFrame
df = pd.DataFrame(
    {'Value': [10, 20, 30, 40, 50, 60]},
    index=index
)

# Display the original DataFrame
print("MultiIndex DataFrame:")
print(df)

# Select all rows belonging to Category A
print("\nIndexing - Category A:")
print(df.loc['A'])

# Select a specific row
print("\nIndexing - Category B, SubCategory B1:")
print(df.loc[('B', 'B1')])

# Slice the DataFrame from Category A to Category B
print("\nSlicing - Category A to Category B:")
idx = pd.IndexSlice
print(df.loc[idx['A':'B', :], :])
