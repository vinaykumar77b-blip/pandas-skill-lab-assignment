
import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Vinay', 'Akhil', 'Sharan', 'Sanjay']
})

# Create the second DataFrame
df2 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Marks': [85, 90, 78, 88]
})

# Display the first DataFrame
print("First DataFrame:")
print(df1)

# Display the second DataFrame
print("\nSecond DataFrame:")
print(df2)

# Merge both DataFrames using the common column ID
merged_df = pd.merge(df1, df2, on='ID')

# Display the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)
