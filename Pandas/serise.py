import pandas as pd
x= [3,4,2,5]
# serise = pd.Series(x)
# serise = pd.Series(x,index=['a','s',3,6])
serise = pd.Series(x,index=['a','s',3,6],dtype=float,name="Array")
print(serise)
print(type(serise))


dic = {
    "name":
    ["python","C","C++","PHP"],
    "por":
    [12,15,16,17],
    "Rank":
    [9,8,7,10]
    }

var1 = pd.Series(dic,dtype=object)
print(var1)

s= pd.Series(12,index=[1,2,3,4,5,6,7,8,9])
print(s)
print(type(s))

s1= pd.Series(12,index=[1,2,3,4,5,6,7,8,9])
s2= pd.Series(12,index=[1,2,3,4])

print(s1+s2)