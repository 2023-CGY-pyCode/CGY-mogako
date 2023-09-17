import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

INF = 1e8
dp = [1e8] * (k+1)
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
    # print(dp[1:16])
if dp[k] >= 1e8:
    print(-1)
else:
    print(dp[k])