# drop a null value in csv file     

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"loan.csv") 
dataset.drop(columns="Credit_History",inplace=True)
dataset.dropna(inplace=True)
print(dataset.isnull().sum())
print(dataset.shape)
print(((614-523)/614)*100)
# sns.heatmap(dataset.isnull())
# plt.show()