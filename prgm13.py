
import pandas as pd
import numpy as np

# Create a list of text strings
words = ['python', 'pandas', 'machine', 'science', 'programming']

# Select 5 random text strings
data = np.random.choice(words, size=5)

# Create a Pandas Series
series = pd.Series(data)

# Display the original Series
print("Original Series:")
print(series)

# Extract the first three characters
result = series.str[:3]

# Display the updated Series
print("\nSeries After Extracting First Three Characters:")
print(result)

