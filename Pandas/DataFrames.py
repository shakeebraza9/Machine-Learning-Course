import pandas as pd
l= [1,2,3,4,5,6,7]
var = pd.DataFrame(l)
print(var)
print(type(var))

# dic ma ap k pass len ki value same hon cheya hemsha 
dic = {
    "name":
    ["python","C","C++","PHP"],
    "por":
    [12,15,16,17],
    "Rank":
    [9,8,7,10],
    "System_Status":
    [0,0,1,0]
    }

# var1 = pd.DataFrame(dic,columns=["name","System_Status"],index=['a','b','c','d'])
var1 = pd.DataFrame(dic)
print(var1)

print(var1["name"][3])