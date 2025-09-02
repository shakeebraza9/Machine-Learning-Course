# Pandas Functions
import pandas as pd
import numpy as np
csv_1 = pd.read_csv('D:\\shakeeb\\Machine Learning FULL Course\\code\\Pandas\\test_pandas.csv')
# print(csv_1.index)
# print(csv_1.columns)
# print(csv_1.describe())
# print(csv_1.head(2))
# print(csv_1.tail(2))
# print(csv_1[6:11])
# print(csv_1[6:11])
# print(csv_1.index.array)
# print(csv_1.to_numpy())

# v1= np.asarray(csv_1)
# print(v1)

# print(csv_1.sort_index(axis=0,ascending=False))

# show an warning in terminal not a best way to write 
# csv_1['Security'][0] = "sky orbit"
# print(csv_1)


csv_1.loc[0,'Security'] = "Sky orbit"

# print(csv_1.loc[[0,1,2,3],['Security','Symbol']])
# print(csv_1.loc[[0,1,2,3],:])
# print(csv_1.iloc[0,1])
# print(csv_1.drop('Security',axis=1))
print(csv_1.drop(0,axis=0))