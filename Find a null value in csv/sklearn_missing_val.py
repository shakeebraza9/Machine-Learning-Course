import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from pandasgui import show
from sklearn.impute import SimpleImputer
dataset = pd.read_csv("loan.csv") 
dataset.isnull().sum()
# print(dataset.info())

mission_data = dataset.select_dtypes(include="float64").columns
# print(mission_data)
si =SimpleImputer(strategy="mean")
arr = si.fit_transform(dataset[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
       'Credit_History']])
missing_val_chk = pd.DataFrame(arr,columns=dataset.select_dtypes(include="float64").columns)
print(missing_val_chk.isnull().sum())
print(dataset['LoanAmount'].mean())
