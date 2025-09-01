import pandas as pd
# insert
var = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,0]})
var.insert(0,"Python",var["A"])
var.insert(1,"PHP",[1,2,3,4,9])
var.insert(2,"Slice",var["A"][:3])
print(var)

# Delete
var1 = pd.DataFrame({"A":[10,20,30,40],"B":[60,70,80,90],"C":[6,7,8,9]})
var2 = var1.pop("B") # this way both of them are same
del var1["A"] # this way both of them are same
print(var1)
print(var2)