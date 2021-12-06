# for 변수 in range(시작값, 끝값+1, 증가값):
i = 0
hap = 0
for i in range(1, 11, 1):
    hap = hap + i
    print(hap)

''' for 변수1 in range(시작값, 끝값+1, 증가값):
        for 변수2 in range(시작값, 끝값+1, 증가값): '''
i, j = 0, 0
for i in range(1, 11, 1):
    for j in range(1, 11, 2):
        print(i+i*j)


# 리스트 생성하기
A = [1, 2, 3, 4, 5]
print(A[0]) # 1
print(A[3]) # 4
i = 0
for i in range(0, 5, 1):
    print(A[i])

B=[]
B.append(1)
B.append(2)
print(B) # B=[1, 2]

C=[]
i = 0
for i in range(0, 4, 1):
    for j in range(0, 3, 2):
        C.append(i+j)
        print(C) # C=[0, 2, 1, 3, 2, 4, 3, 5]
for k in range(0, 5, 1):
    C[k] = k+1
    print(C) # C=[1, 2, 3, 4, 5, 4, 3, 5]