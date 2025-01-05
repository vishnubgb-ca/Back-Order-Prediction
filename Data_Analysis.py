
import pandas as pd

def analyze_dataframe(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input should be a pandas DataFrame")

    # Descriptive statistics
    print("Descriptive Statistics:")
    print(df.describe(include="all").transpose())

    # Top 5 rows
    print("\nTop 5 rows:")
    print(df.head())

    # Bottom 5 rows
    print("\nBottom 5 rows:")
    print(df.tail())

    # Data type in each column
    print("\nData type in each column:")
    print(df.dtypes)

# Test the function
df = pd.read_csv("data.csv")

analyze_dataframe(df)

