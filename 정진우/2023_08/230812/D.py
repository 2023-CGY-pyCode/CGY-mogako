N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
Q = int(input())

def rotate(arr):
    A = [[] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            A[i].append(arr[j][i])
        A[i] = A[i][::-1]
    
    # arr = A[:]
    # print(arr)
    return A
    
for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        y = query[1]-1
        for i in range(N-1, 0, -1):
            dx = (i-1)%N # 0 -> 1 , 1 -> 2, 2 -> 0
            arr[y][dx], arr[y][i] = arr[y][i], arr[y][dx]
    else:
        arr = rotate(arr)
        
            
    
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
    
    
    