def check(N, K):
    count = 0
    arr = [1] * (N+1) # 1이 소수 0이 소수 x
    arr[1] = 0
    # print(N**(0.5))
    for i in range(2, int(N)+1):
        for j in range(i, N+1, i):
            if arr[j] == 0:
                continue
            # print(i, j)
            arr[j] = 0
            count += 1
            # print(j)
            if count == K:
                return j
                
        

N, K = tuple(map(int, input().split()))

print(check(N, K))
