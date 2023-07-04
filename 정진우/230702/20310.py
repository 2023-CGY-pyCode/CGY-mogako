S = list(str(input()))

zero_arr = []
one_arr = []

for i in S:
    if i == '0':
        zero_arr.append(0)
    elif i == '1':
        one_arr.append(1)

for i in range(len(zero_arr) // 2): # 반절
    for j in range(len(S)-1, -1, -1):# 뒤에서 부터 
        if S[j] == '0':
            S.pop(j)
            break

for i in range(len(one_arr) // 2): # 반절
    for j in range(0, len(S), 1):# 앞에서 부터 
        if S[j] == '1':
            S.pop(j)
            break

for i in S:
    print(i, end="")
    