# leble encoding use hote ha jo nominal data type pe 
# nominal data type wo data type hote ha wo repet na ho rahi ha jasy name  cat dog cow different ha 

import pandas as pd 
from pandasgui import show
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({
    "name":["Cat","Dog","Cow","Elephant","Loin"]
})

le = LabelEncoder()
df["en_name"] =le.fit_transform(df['name'])

print(df)

dataset = pd.read_csv("loan.csv")
print(dataset["Property_Area"].unique())
la = LabelEncoder()
dataset['Property_Area'] = la.fit_transform(dataset['Property_Area'])
print(dataset['Property_Area'])

