# outlear ya hota ha jab ek serious ma data chal raha ho or bech ma koie out value ajay us se ap ka model acha train nhi ho ga 
# how to detack outlear discribe ma akr check krna ha mean value kiya ha or max value dono ka difference kafi zada ho to is ma outlear hone k both chnace ha 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('loan.csv')
# print(dataset.info())
# print(dataset.describe())
# boxplot using to graph find the outlear value
# sns.boxplot(x="CoapplicantIncome",data=dataset)
# plt.show()

# sns.displot(dataset['ApplicantIncome'])
# plt.show() 

l = [5,6,7,8,9,2,100] #outlear is an 100
print(sum(l)/len(l))
