from sklearn import svm, metrics
import random, re

csv = []

with open("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\Iris.csv", \
    'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip() # 양쪽 공백을 제거해준다.
        cols = line.split(',') # 쉼표로 columns 구분해준다.
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# 헤더 제거하기
del csv[0]

# 데이터 섞기
random.shuffle(csv)

# 훈련데이터와 테스트데이터 분리하기
total_len = len(csv)
train_len = int(total_len*2/3)

train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data, train_label)
y_label = clf.predict(test_data)
print(y_label)
acc_score = metrics.accuracy_score(test_label, y_label)
print('accuracy: ', acc_score * 100, '%')
