
import pandas as pd
import numpy as np

# Create a DataFrame with random categories and values
data = {
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(10, 100, size=10)
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Group by Category and calculate sum and mean
result = df.groupby('Category')['Value'].agg(['sum', 'mean'])

# Display the result
print("\nSum and Mean of Each Category:")
print(result)
