import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandasgui import show
dataset = pd.read_csv("loan.csv") 
# show(dataset)
# show(dataset.fillna(10))
# Sirf null values ka count
# print(dataset.isnull().sum())
# print(dataset.info())

# backword and forward filling filling
# dataset = dataset.fillna(method="ffill" ,axis=1)
# print(dataset)
# perusntage = (dataset.isnull().sum()/dataset.shape[0])*100
# print(perusntage)

# Mode filling is using most use data in colume use null colume
# dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)
# show(dataset)


# Using for loop to collect object type Data
for i in dataset.select_dtypes(include="object").columns:
    dataset[i].fillna(dataset[i].mode()[0],inplace=True)
perusntage = (dataset.isnull().sum()/dataset.shape[0])*100
print(perusntage)