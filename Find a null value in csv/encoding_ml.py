# category data ko numerical data ma convert krne k leya encoding use hote ha jyu k ml jo ha wo ha mathamatical pe banwa ha us pe category data work nhi krta ha 
# one hot encoding using same data repet 
import pandas as pd
from pandasgui import show
from sklearn.preprocessing import OneHotEncoder
dataset = pd.read_csv("loan.csv") 
# print(dataset.isnull().sum())

# sab se phely data ko fill krna ha abhi 2 row pe kam krna ha on hot encoding Gender Married
dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)
dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)
en_data = dataset[["Gender","Married"]]
# print(en_data)
# get_dummies using by pandas 

# show(pd.get_dummies(en_data)) # return value link True and False Not 0 or 1
# print(pd.get_dummies(en_data).info())

# sklearn OneHotEncoder return value into 0 or 1 
# ohe = OneHotEncoder()
# data = ohe.fit_transform(en_data).toarray()
# show(pd.DataFrame(data,columns=["Gender_Female","Gender_Male","Married_No","Married_Yes"]))

ohe = OneHotEncoder(drop="first") #drop first using to delete the first row 
data = ohe.fit_transform(en_data).toarray()
show(pd.DataFrame(data,columns=["Gender_Male","Married_Yes"]))
