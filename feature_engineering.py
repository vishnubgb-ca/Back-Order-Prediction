from sklearn.preprocessing import LabelEncoder
# from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd

def feature_engg():
    
    data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    data = data.drop(columns=["sku","lead_time"],axis=1)
    data = data.dropna(axis=0, how='any')
    data = data.replace(to_replace = -99, value = np.nan)
    data["perf_6_month_avg"] = data["perf_6_month_avg"].fillna(data["perf_6_month_avg"].median())
    data["perf_12_month_avg"] = data["perf_12_month_avg"].fillna(data["perf_12_month_avg"].median())
    print ("Missing values after removal of rows with empty values\n\n",data.isnull().any(),sep='')
    print(data)
    #Outlier removal
    print("Old Shape: ", data.shape)

    def remove_outliers(data,par):
        print(par)
        print(data.info())
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data.drop(index=i,inplace=True)
            
        #for i in b[0]:
            #if i in data.index:
                #data.drop(index=i,inplace=True)

    for j in ["national_inv",   "in_transit_qty",   "forecast_3_month", "forecast_6_month"  ,"forecast_9_month" ,"sales_1_month", "sales_3_month", "sales_6_month", "sales_9_month", "min_bank", "pieces_past_due", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]: 
        remove_outliers(data,j)
    
    le=LabelEncoder()
    
    data['potential_issue']=le.fit_transform(data['potential_issue'])
    data['deck_risk']=le.fit_transform(data['deck_risk'])
    data['oe_constraint']=le.fit_transform(data['oe_constraint'])
    data['ppap_risk']=le.fit_transform(data['ppap_risk'])
    data['stop_auto_buy']=le.fit_transform(data['stop_auto_buy'])
    data['rev_stop']=le.fit_transform(data['rev_stop'])
    data['went_on_backorder']=le.fit_transform(data['went_on_backorder'])
    print(data.head())

    X=data.drop(columns="went_on_backorder")
    y=data['went_on_backorder']
    target = le.fit_transform(np.ravel(y))
    
    sm = SMOTE()
    X_upd, y_upd = sm.fit_resample(X, target.ravel())

    data_new=X_upd
    data_new['went_on_backorder']=y_upd 
    data_new.to_csv("cleaned_data.csv",index=False)

    return data_new

feature_engg()
