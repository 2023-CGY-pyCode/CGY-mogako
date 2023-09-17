n = int(input())
m = int(input())

INF = 1e9
arr = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][i] = 0
        
for _ in range(m):
    a, b, c = tuple(map(int, input().split()))
    
    arr[a][b] = min(c, arr[a][b])


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == INF:
            print('0', end=" ")
        else:
            print(arr[i][j], end = " ")  
    print()