import pandas as pd
import numpy as np
from pandas import DataFrame
import re

def list_chunk(list, n):
    return [ list[i:i+n] for i in range(0, len(list), n)]

data_file = pd.read_fwf('C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\June_input_data\\Input.txt')
data_list = []
if data_file.shape[1] == 1:
    with open("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\June_input_data\\Input.txt", \
        'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip() # 양쪽 공백을 제거해준다.
            line = ' '.join(line.split())
            cols = re.split(r'[ ]', line, 5) 
            data_list.append(cols)
            data_file = pd.DataFrame(data_list)
            data_file = data_file.drop([0])

input_file = np.array(data_file)
print(input_file.shape)
input_file = input_file.astype(float)
print(input_file)

def digital(file):
    for i in range(file.shape[0]):
        for j in range(3):
            if -0.1 <= file[i][j+1] <= 0.1:
                file[i][j+1] = 0
            elif 0.9 <= file[i][j+1] <= 1.1:
                file[i][j+1] = 1
            else:
                file[i][j+1] = 'error'
    return file

print(digital(input_file))

df = pd.DataFrame(input_file)
df.to_csv("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\June_input_data\\June.csv", \
            header=['index', 'output_ml_2*1', 'output_ml_1*1', 'output_ml_3*1', 'temper', 'alter#'], index=False)
           