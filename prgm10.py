
import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 5 rows
data = np.random.randint(1, 100, size=(5, 3))

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Apply a function to double all values
result = df.apply(lambda column: column * 2)

# Display the updated DataFrame
print("\nDataFrame After Doubling Values:")
print(result)
