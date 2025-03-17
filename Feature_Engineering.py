
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
# Load the dataset
df = pd.read_csv("data.csv")

# Handle missing values
df = df.drop(columns=["sku","lead_time"],axis=1)
df = df.dropna(axis=0, how="any")
df = df.replace(to_replace = -99, value = np.nan)
df["perf_6_month_avg"] = df["perf_6_month_avg"].fillna(df["perf_6_month_avg"].median())
df["perf_12_month_avg"] = df["perf_12_month_avg"].fillna(df["perf_12_month_avg"].median())
print("Missing values after removal of rows with empty values\n\n",df.isnull().any(),sep="")
print(df)

# Remove outliers using Z-score
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
df = df[(z_scores < 3).all(axis=1)]

# Label encoding
le = LabelEncoder() 
for col in df.columns: 
   if df[col].dtype == "object": 
       df[col] = le.fit_transform(df[col])

# Balance the dataset using SMOTE
y = df["went_on_backorder"]
X = df.drop("went_on_backorder", axis=1)
smote = SMOTE()
X, y = smote.fit_resample(X, y)

# Save the cleaned dataset
df_cleaned = pd.concat([X, y], axis=1)
print(df_cleaned)
df_cleaned.to_csv("cleaned_data.csv", index=False)





