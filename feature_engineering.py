import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from scipy import stats

# Load data
df = pd.read_csv('data.csv')

# Mean Imputation
#imputer = SimpleImputer(strategy='mean')
#df['forecast_6_month'] = imputer.fit_transform(df['forecast_6_month'].values.reshape(-1, 1))

# Duplicate values
#df = df.drop_duplicates(subset=['true'])

# Label encoding
encoder = LabelEncoder()
categorical_columns = ['potential_issue', 'deck_risk', 'oe_constraint', 'ppap_risk', 'stop_auto_buy', 'went_on_backorder', 'rev_stop']
for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

# Feature deletion
df = df.drop(['sku', 'lead_time'], axis=1)

# Balancing data
#smote = SMOTE(sampling_strategy={'went_on_backorder': 1})
#X, y = df.drop('went_on_backorder', axis=1), #df['went_on_backorder']
#X, y = smote.fit_resample(X, y)

# Outliers
numerical_columns = ['national_inv', 'in_transit_qty', 'forecast_3_month', 'forecast_6_month', 'forecast_9_month', 'sales_1_month', 'sales_3_month', 'sales_6_month', 'sales_9_month', 'min_bank', 'pieces_past_due', 'local_bo_qty']
#for column in numerical_columns:
    #df = df[df[column] <= stats.zscore(df[column])]

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)

# Print top 5 rows
print(df.head())