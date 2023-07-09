import sys

def knapsack(K, weights, values, N):
    P = [[0 for x in range(K+1)] for x in range(N+1)]
    # K[i][W]는 i개의 갯수만 사용했을때의 W인 무게한도의 최댓값
    for i in range(N+1):
        for w in range(K+1):
            if i == 0 or w == 0:
                P[i][w] = 0
            elif weights[i-1] > w: # 최대한도
                P[i][w] = P[i-1][w]
            else:
                P[i][w] = max(values[i-1]+P[i-1][w-weights[i-1]], P[i-1][w])
    return P[N][K]


N, K = tuple(map(int, input().split()))

weights = []
values = []
for _ in range(N):
    item = tuple(map(int, sys.stdin.readline().split()))
    weights.append(item[0])
    values.append(item[1])
    
print(knapsack(K, weights, values, N))
    




            
            
            