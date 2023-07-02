import sys
sys.setrecursionlimit(10000)

T = int(input()) # Test Case

def check_direction(i, j, arr, N, M):
    if arr[i][j] == 0:
        return arr
    else:
        arr[i][j] = 0
        if i+1 <= N-1: # 남
            arr = check_direction(i+1, j, arr, N, M)
        if i-1 >= 0: # 북
            arr = check_direction(i-1, j, arr, N, M)
        if j+1 <= M-1: # 동
            arr = check_direction(i, j+1, arr, N, M)
        if j-1 >= 0: # 서
            arr = check_direction(i, j-1, arr, N, M)
    return arr




for _ in range(T):
    N, M, K = tuple(map(int, input().split()))
    
    arr = [[0]* M for _ in range(N)] # arr N*M 배열 0으로 초기화
    warm_count = 0
    for _ in range(K):
        X, Y = tuple(map(int, input().split()))
        arr[X][Y] = 1
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            if arr[i][j] == 1:
                warm_count += 1
                arr = check_direction(i, j, arr, N, M)
    
    print(warm_count)

                
        

