import pandas as pd
dataset = pd.read_csv(r"loan.csv") 
dataset.head(3)
perusntage = dataset.isnull().sum()/dataset.shape[0]
print(perusntage)