import  pandas as pd

def data_analysis():
    data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    print(data.head())
    print(data.tail())
    print(data.describe())
    print(data.info())
    print ("Rows     : " ,data.shape[0])
    print ("Columns  : \n" ,data.shape[1])
    print ("Features : \n" ,data.columns.tolist())
    print ("Missing values\n\n",data.isnull().any(),sep='')
    print ("Unique values\n\n",data.nunique(),sep='')
    return data

data_analysis()
