# (dropna and fillna)
import pandas as pd
var = pd.read_csv('D:\\shakeeb\\Machine Learning FULL Course\\code\\Pandas\\loan.csv')
# print(var)

# print(var.dropna(axis=1)) #colume delete working is 1
# print(var.dropna(axis=0)) # row delete working is 0

# print(var.dropna(how="all"))
# print(var.dropna(subset=['Gender']))
# var.dropna(inplace=True)
# var.dropna(thresh=1)
# print(var)



# print(var.fillna("python"))
# print(var.fillna({"Loan_ID":"LAP001","Gender":"Male"}))
# print(var.fillna(method="ffill")) # forword data in current null feild
# print(var.fillna(method="bfill")) #backword data into current null feild
# print(var.fillna(method="ffill",axis=1))
# var.fillna(12,inplace=True)

print(var.fillna("Python",limit=5,axis=1)) 
