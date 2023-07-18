import sys
W, H =  map(int ,sys.stdin.readline().split()) # 종이 크기

n = int(sys.stdin.readline()) # 반복 수

wi = [] # 가장 큰 가로
he = [] # 가장 큰 세로

for i in range(n):
    wh, n = map(int, sys.stdin.readline().split())
    if wh == 0: # 가로로 자르기
        he.append(n)
    else: # 세로로 자르기
        wi.append(n)

wi.append(W)
he.append(H)

wi.append(0)
he.append(0)

wi.sort()
he.sort() # 둘 다 정렬


X = wi[0]
Y = he[0]

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
