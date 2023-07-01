dp = []
dp.append(0)
dp.append(1)
dp.append(2)
dp.append(4)

for i in range(4, 13):
    dp.append( dp[i-1] + dp[i-2] + dp[i-3] )
    
    
T = int(input())

for _ in range(T):
    n = int(input())
    
    print(dp[n])
