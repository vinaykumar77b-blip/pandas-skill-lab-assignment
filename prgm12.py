
import pandas as pd
import numpy as np

# Create a list of text strings
words = ['python', 'pandas', 'machine learning', 'data science', 'programming']

# Select 5 random text strings
data = np.random.choice(words, size=5)

# Create a Pandas Series
series = pd.Series(data)

# Display the original Series
print("Original Series:")
print(series)

# Convert all strings to uppercase
result = series.str.upper()

# Display the updated Series
print("\nSeries After Converting to Uppercase:")
print(result)
