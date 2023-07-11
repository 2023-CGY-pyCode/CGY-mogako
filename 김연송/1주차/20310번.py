S = list(map(int, input()))

count1 = 0
count0 = 0

for i in range(len(S)):
    if S[i] == 0:
        count0 += 1
    else:
        count1 += 1

count1 //= 2 # 지워야할 1의 개수
count0 //= 2 # 지워야할 0의 개수

# 1은 앞의 값부터, 0은 뒤의 값부터 삭제하기

i = 0
while count1 != 0:
    if S[i] == 1: # 배열의 i번째 값이 1이고 count1이 0이 아니면 해당 값 삭제   
        del S[i]
        count1 -= 1
        continue
    i += 1

i = len(S) - 1
while count0 != 0:
    if S[i] == 0: # 배열의 i번째 값이 0이고 count0이 0이 아니면 해당 값 삭제
        del S[i]
        count0 -= 1
    i -= 1
        

for i in range(len(S)):
    print(S[i], end='')
    
