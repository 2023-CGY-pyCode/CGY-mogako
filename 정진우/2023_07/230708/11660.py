import sys

N, M = tuple(map(int, input().split()))

arr = []
answer = []
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    
    arr.append(li)

for _ in range(M):
    li = list(map(int, sys.stdin.readline().split()))
    answer.append(li)
    
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            arr[i][j] += arr[i][j-1]
        elif j == 0:
            arr[i][j] += arr[i-1][j]
        else: 
            arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1] 
    
# print(arr)
for ans in answer:
    x1,y1,x2,y2 = tuple(ans)
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    
    if x1 == 0 and y1 == 0:
        a = arr[x2][y2]
    elif x1 == 0:
        a = arr[x2][y2] - arr[x2][y1-1]
    elif y1 == 0:
        a = arr[x2][y2] - arr[x1-1][y2]
    else:
        a = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
        
    print(a)


