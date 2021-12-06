import pandas as pd
import numpy as np

csv_file = pd.read_csv("'C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\June_input_data\\June.csv")
input_file = np.array(csv_file)

A = int(input("정답은 무엇입니까?(0 OR 1) "))

def CountError(file):
    count_1 = 0
    for i in range(file.shape[0]):
        if file[i][2] != A:
            count_1 += 1
    print('에러율 = ', count_1 / input_file.shape[0] * 100)

CountError(input_file)

def frequency(file):
    count_1 = 0
    count_2 = 0
    for i in range(file.shape[0]):
        if file[i][2] !=A:
            count_1 += 1
        if file[i][1] == 0 and file[i][2] !=A and file[i][3] == 1:
            count_2 += 1
    print('수정에러율 = ', (count_1 - count_2) / input_file.shape[0] * 100)
    print('빈도율 = ', count_2 / input_file.shape[0] * 100)

frequency(input_file)