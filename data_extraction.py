import  pandas as pd
#import pymysql
import os

def loading_data():
    data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    return data

loading_data()
