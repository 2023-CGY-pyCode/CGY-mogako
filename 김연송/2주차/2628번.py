import sys
W, H =  map(int ,sys.stdin.readline().split()) # 종이 크기

n = int(sys.stdin.readline()) # 반복 수

wi = [] # 가로 값 저장
he = [] # 세로 값 저장

for i in range(n):
    wh, n = map(int, sys.stdin.readline().split())
    if wh == 0: # 가로로 자르기
        wi.append(n)
    else: # 세로로 자르기
        he.append(n)

wi.append(H) # 배열 원소끼리 뺼셈을 할 것이라서 가로 세로 총 길이릴 각각 배열에 추가해주기
he.append(W)
# 각각 가로 값이 세로를 자르고, 세로 값이 가로를 자르기 때문에
# 입력받은 종이의 크기를 반대되는 배열에 저장해준다.

wi.append(0) # 배열 원소끼리 뺄셈을 할 것이라서 0을 두 배열에 모두 추가해주기
he.append(0)

wi.sort()
he.sort() # 둘 다 정렬


max = 0
for i in range(len(wi) - 1):
    for j in range(len(he) - 1):
        if (wi[i + 1] - wi[i]) * (he[j + 1] - he[j]) > max:
            max = (wi[i + 1] - wi[i]) * (he[j + 1] - he[j])

print(max)
        
    # 10cm 가로를 2, 3자른 경우
    # 길이는 2 3 - 2, 10 - 3
    # 8cm 세로를 4 자른 경우
    # 길이는 4, 8 - 4
