
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv("data.csv")  # replace "your_dataset.csv" with your actual file path
except Exception as e:
    print("Error occurred while loading the dataset: ", e)
    exit(1)

# Display basic information about the dataset
try:
    print("Basic information about the dataset:")
    print(df.info())
except Exception as e:
    print("Error occurred while displaying basic information: ", e)

# Check for missing values
try:
    print("\nChecking for missing values:")
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print("Missing values found:")
        print(missing_values)
    else:
        print("No missing values found.")
except Exception as e:
    print("Error occurred while checking for missing values: ", e)

# Print summary statistics
try:
    print("\nSummary statistics:")
    print(df.describe())
except Exception as e:
    print("Error occurred while printing summary statistics: ", e)

