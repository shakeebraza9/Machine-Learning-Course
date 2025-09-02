import pandas as pd
# csv_1 = pd.read_csv('test_pandas.csv')
# print(csv_1)

# csv_2 = pd.read_csv('test_pandas.csv',nrows=3)
# csv_2 = pd.read_csv('test_pandas.csv',usecols=["Security","Chnage"])
# csv_2 = pd.read_csv('test_pandas.csv',usecols=[0,3],index_col=0)
# csv_2 = pd.read_csv('test_pandas.csv',skiprows=[0,9])
# csv_2 = pd.read_csv('test_pandas.csv',header=2)
# csv_2 = pd.read_csv('test_pandas.csv',names=['id','names','total price',"AVG price","is chnage"])
csv_2 = pd.read_csv('test_pandas.csv',dtype={"Total_valoume":"int"})


print(csv_2)
# csv_2 = pd.read_csv('test_pandas.csv',header=None)
# csv_2.columns = [f"col{i}" for i in range(len(csv_2.columns))]
# print(csv_2.head())
print(type(csv_2))