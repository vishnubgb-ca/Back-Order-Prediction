
import pandas as pd

def preprocess_dataframe(df):
    # Remove rows with missing values
    df = df.dropna()

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df

# Example usage:
df = pd.read_csv("data.csv")
df = preprocess_dataframe(df)
df.to_csv("data.csv", index=False)
print(df)

