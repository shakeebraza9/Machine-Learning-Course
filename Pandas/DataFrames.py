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


# same process as list 
list_1 = [[1,2,3,4,5],[2,3,4,5,7,8,1,0]]
var2 = pd.DataFrame(list_1)
print(var2)
print(type(var2))
# print(var2["name"][3])


sr={"s":pd.Series([1,2,3,4,5]),"r":pd.Series([9,8,7,6,5])}
var3 = pd.DataFrame(sr)
print(var3)
print(type(var3))