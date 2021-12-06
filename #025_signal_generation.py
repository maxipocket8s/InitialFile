file = open("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\June_input_data\\input_sub.txt", 'w', encoding='utf-8')
N = int(input("EVAL: "))
M = int(input("MID(1X1): "))
U = int(input("UP(2X1): "))
D = int(input("DOWN(3X1): "))
file.write("**\n\n")
for i in range(N):
    file.write("vsl<{0}> sl<{0}> 0 PWL 0 0 1.09e-9 0 1.091e-9 1 TD=0\n".format(i))
for i in range(N):
    file.write("vslb<{0}> slb<{0}> 0 PWL 0 0 1.09e-9 0 1.091e-9 0 TD=0\n".format(i))
for i in range(N, 150):
    file.write("vsl<{0}> sl<149> 0 PWL 0 0 1.09e-9 0 1.091e-9 0 TD=0\n".format(i))
for i in range(N, 150):
    file.write("vslb<{0}> slb<149> 0 PWL 0 0 1.09e-9 0 1.091e-9 1 TD=0\n".format(i))
if N < M: # CASE A
    for i in range(N):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, M):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, M):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(M, 150):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(M, 150):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
elif N == M: # CASE B
    for i in range(N):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
else: # CASE C
    for i in range(M):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(M):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
    for i in range(M, N):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=0\n".format(i))
    for i in range(M, N):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_1x1<{0}> ref_w_1x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_1x1<{0}> ref_wb_1x1<{0}> 0 DC=0\n".format(i))
if N < U: # A CASE
    for i in range(N):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, U):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, U):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(U, 150):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(U, 150):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
elif N == U: # B CASE
    for i in range(N):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
else: # C CASE
    for i in range(U):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(U):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
    for i in range(U, N):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=0\n".format(i))
    for i in range(U, N):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_2x1<{0}> ref_w_2x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_2x1<{0}> ref_wb_2x1<{0}> 0 DC=0\n".format(i))
if N < D:
    for i in range(N):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, D):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, D):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(D, 150):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(D, 150):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
elif N == D:
    for i in range(N):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(N):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
else:
    for i in range(D):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(D):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
    for i in range(D, N):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=0\n".format(i))
    for i in range(D, N):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_w_3x1<{0}> ref_w_3x1<{0}> 0 DC=1\n".format(i))
    for i in range(N, 150):
        file.write("vref_wb_3x1<{0}> ref_wb_3x1<{0}> 0 DC=0\n".format(i))
for i in range(150):
    file.write("vbl<{0}> bl<{0}> 0 DC=0\n".format(i))
for i in range(150):
    file.write("vblb<{0}> blb<{0}> 0 DC=0\n".format(i))
file.close()