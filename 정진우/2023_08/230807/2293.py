import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
dp = [0 for i in range(k+1)]
dp[0] = 1 # 동전을 한개만 사용하는 경우


for _ in range(n):
    num = int(input())
    coins.append(num)


for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0: # 동전을 사용할 수 있는 경우
            dp[i] += dp[i-coin] 
            
print(dp[k])
            