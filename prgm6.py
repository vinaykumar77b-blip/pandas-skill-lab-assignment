
import pandas as pd
import numpy as np

# Create a DataFrame with random data
data = {
    'Product': np.random.choice(
        ['Laptop', 'Mobile', 'Tablet', 'Headphones'], size=10
    ),
    'Category': np.random.choice(
        ['Electronics', 'Accessories', 'Gadgets'], size=10
    ),
    'Sales': np.random.randint(1000, 10000, size=10)
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Group by Category and calculate total sales
result = df.groupby('Category')['Sales'].sum()

# Display total sales
print("\nTotal Sales by Category:")
print(result)
