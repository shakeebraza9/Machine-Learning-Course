import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from pandasgui import show

# find out null data is this way
dataset = pd.read_csv(r"loan.csv") 
# dataset.head(3)
# show(dataset.shape) # show row and colume total value 
# print(dataset.isnull().sum().sum()) # check total null value in this file
perusntage = (dataset.isnull().sum()/dataset.shape[0])*100 # persunt each cell have null value in persunt
# print(perusntage)

find_avg_null_value_alldata = (dataset.isnull().sum().sum()/(dataset.shape[0] * dataset.shape[1] ))*100 # find Avg null value all data
# print(find_avg_null_value_alldata)

# find out not null mean fill data in this way 

# print(dataset.notnull().sum())

sns.heatmap(dataset.isnull())
plt.show()