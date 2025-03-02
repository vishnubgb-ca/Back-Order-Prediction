
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy import stats

def encode_categorical(df):
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])
    return df

def remove_outliers_IQR(df):
    for col in df.columns:
        if df[col].dtype != "object":
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]
    return df

def balance_data(df, target_col):
    # Separate majority and minority classes
    majority_class = df[df[target_col]==0]
    minority_class = df[df[target_col]==1]

    # Upsample minority class
    minority_upsampled = resample(minority_class, 
                                 replace=True,     # sample without replacement
                                 n_samples=len(majority_class),    # to match majority class
                                 random_state=42) # reproducible results

    # Combine majority class with upsampled minority class
    df_balanced = pd.concat([majority_class, minority_upsampled])

    return df_balanced

def remove_unwanted_features(df, unwanted_features):
    return df.drop(unwanted_features, axis=1)

# Assuming df is your dataframe, "target" is your target column and "unwanted" is a list of unwanted features
df = pd.read_csv("data.csv")
df = encode_categorical(df)
df = remove_outliers_IQR(df)
#df = balance_data(df, "went_on_backorder")
#df = remove_unwanted_features(df, "sku")
df.to_csv("cleaned_data.csv", index=False)
print("cleansed data:\n", df)


