import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,0]})
var["C"] =var["A"]+var["B"] 
var["D"] =var["A"]-var["B"] 
var["E"] =var["A"]*var["B"] 
var["F"] =var["A"]/var["B"] 
print(var)
# print(var["C"])


# Logical Arithmetic Operators in Python Pandas
var1 = pd.DataFrame({"A":[10,20,30,40],"B":[60,70,80,90]})
var1["Logical"] = var1["A"] <= 20
var1["Logical_1"] = var1["B"] >= 70
print(var1)