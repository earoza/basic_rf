import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
digits = load_digits()

dir(digits)

['DESCR', 'data', 'images', 'target', 'target_names']

plt.gray()
#Show digits 0 to 3
# for i in range(4):
#     plt.matshow(digits.images[i])

#raw
print('RAW')
print(digits.data[:5])

#create Data Frame from digits data
df = pd.DataFrame(digits.data)

#Df format
print('DF FORMAT')
print(df.head())

#Append target collum to the df
df['target'] = digits.target
print('APPEND TARGET TO DF')
print(df.head())

from sklearn.model_selection import train_test_split

#Split 20% of the dataset for test
X_train, X_test, y_train, y_test = train_test_split(df.drop(['target'], axis='columns'), digits.target, test_size=0.2)

#Import classifier
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

#train classifier
model.fit(X_train, y_train)

#Makes pediction
score = model.score(X_test, y_test)
print('PREDICTION WITH DEFAULT VALUES')
print(score)

model_custom = RandomForestClassifier(n_estimators=50)

#train classifier
model_custom.fit(X_train, y_train)

#Makes pediction
score = model_custom.score(X_test, y_test)
print('PREDICTION WITH CUSTOM VALUES (n_estimators=50)')
print(score)

#BUILDING CONFUSION MATRIX
from sklearn.metrics import confusion_matrix

y_predicted = model.predict(X_test)

cm = confusion_matrix(y_test, y_predicted)

#Confusion matrix
print(cm)

#BETTER VISUALIZATION
import seaborn as sn

plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Answer')
plt.show()
