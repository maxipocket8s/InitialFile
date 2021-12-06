import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\Iris.csv")
csv_data = csv[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
csv_label = csv['variety']

X_train, X_test, y_train, y_test = train_test_split(csv_data, csv_label)

clf = svm.SVC()
clf.fit(X_train, y_train)
y_label = clf.predict(X_test)
acc_score = metrics.accuracy_score(y_test, y_label)
print('accuracy: ', acc_score*100, "%")