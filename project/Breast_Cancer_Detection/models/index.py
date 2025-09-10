import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
breast = pd.read_csv('D:\\shakeeb\\Machine Learning FULL Course\code\\project\\Breast_Cancer_Detection\\models\\breast-cancer.csv')
# print(breast.head())
# print(breast['diagnosis'].value_counts())
# print(breast.shape)
# print(breast.isnull().sum())
# print(breast.info())
breast['diagnosis'] = breast['diagnosis'].map({'M':0, 'B':1})

# print(breast.corr())
# breast.drop('unnamed:32',axis=1,inplace=True)
# print(breast.describe())
# print(breast['diagnosis'].value_counts())

X = breast.drop('diagnosis',axis=1)
y = breast['diagnosis']
print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# print(X_train.shape)
# print(X_test.shape)
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
# print(X_test)

lg = LogisticRegression()
lg.fit(X_train,y_train)
y_pred =    lg.predict(X_test)
# print(y_pred)
# print(accuracy_score(y_test,y_pred))
print(X_train[10])
# input_test = ([-0.23712907, -1.39998202, -1.24962228, -1.34520926, -1.10978518, -1.33264483,
#                -0.30735463, -0.36555756, -0.69650228,  1.93033305,  0.95437877,  0.02752055,
#                 1.96305996, -0.12095781, -0.35077918,  0.57276579,  0.7394992,   0.32065553,
#                 0.58946222,  2.61504052,  0.71892779, -1.29528358, -1.04081128, -1.24522047,
#                -0.99971493, -1.43869328, -0.54856427, -0.64491059, -0.97023893,  0.59760192,
#                 0.0578942 ])

input_test = ([-0.23711093, -0.4976419,   0.61365274, -0.49813131, -0.53102815, -0.57694824,
               -0.17494424, -0.36215622, -0.284859,    0.43345165,  0.17818232, -0.36844966,
                0.55310406, -0.31671104, -0.40524636,  0.04025752, -0.03795529, -0.18043065,
                0.16478901, -0.12170969,  0.23079329, -0.50044002,  0.81940367, -0.46922838,
               -0.53308833, -0.04910117, -0.04160193, -0.14913653,  0.09681787,  0.10617647,
                0.49035329])

np_df =np.asarray(input_test)
prediction = lg.predict(np_df.reshape(1, -1))

if prediction == 1:
    print("Cancrous")
else:
    print("Not Cancrous") 



import pickle
pickle.dump(lg, open("model.pkl", "wb"))