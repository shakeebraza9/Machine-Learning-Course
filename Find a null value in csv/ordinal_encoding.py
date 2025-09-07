# ordinal encodin 2 tarah se perfume ki jaa sakte ha 
# 1st way ap sklearn ki help laa sakty ha 
# 2nd way ha ap map function ka use kr sakty ha 
import pandas as pd
from pandasgui import show
from sklearn.preprocessing import OrdinalEncoder
# df = pd.DataFrame({"Size":["s","m","l","xl","s","m","l","s","m","s","l","xl"]})
# ord_data = [["s","m","l","xl"]]
# oe = OrdinalEncoder(categories=ord_data)
# oe.fit(df[['Size']])              # encoder fit ho gaya
# df['size_en'] = oe.transform(df[['Size']])  # data transform hua
# df['size_en'] = df['size_en'].astype(int)
# print(df)


#  map function
# df2 = pd.DataFrame({"Size":["s","m","l","xl","s","m","l","s","m","s","l","xl"]})
# ord_data1 = {"s":5 , "m":7 , "l":6 , "xl":8}
# df2['size_en']=df2['Size'].map(ord_data1)
# print(df2)

dataset = pd.read_csv('loan.csv')
# print(dataset['Property_Area'].unique())
# dataset.fillna({'Property_Area': dataset['Property_Area'].mode()[0]}, inplace=True)
# en_data_loan = [["Rural","Urban","Semiurban" ]]
# ena = OrdinalEncoder(categories=en_data_loan)
# dataset['Property_Area'] = ena.fit_transform(dataset[['Property_Area']])
# print(dataset['Property_Area'] )


#  map function
dataset.fillna({'Property_Area': dataset['Property_Area'].mode()[0]}, inplace=True)
en_data_loan = {"Rural":0,"Urban":1,"Semiurban":2 }
dataset['Property_Area'] = dataset['Property_Area'].map(en_data_loan)
print(dataset['Property_Area'])