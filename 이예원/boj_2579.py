import sys

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n)]

dp[0] = stair[0]
if len(stair) != 1:
    dp[1] = stair[0] + stair[1]
    if len(stair) > 2:
        dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
        for i in range(2, n):
            dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])