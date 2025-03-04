
import pandas as pd

# Load the dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error occurred while loading the data: {str(e)}")
        return None

# Display basic information about the dataset
def display_info(df):
    if df is not None:
        print(df.info())
    else:
        print("Data is not loaded correctly.")

# Check for missing values
def check_missing_values(df):
    if df is not None:
        print(df.isnull().sum())
    else:
        print("Data is not loaded correctly.")

# Print summary statistics
def print_summary_statistics(df):
    if df is not None:
        print(df.describe())
    else:
        print("Data is not loaded correctly.")

# Main function
def main():
    df = load_data("data.csv")
    display_info(df)
    check_missing_values(df)
    print_summary_statistics(df)

if __name__ == "__main__":
    main()




