N = int(input())

li = list(map(int, input().split()))

count = 0
DP = [0] * 1001
answer = 0

for i in range(len(li)):
    DP[i] = 1
    for j in range(i):
        if li[i] > li[j]:
            DP[i] = max(DP[i], DP[j]+1)
        
    answer = max(answer, DP[i])
        
print(answer)
    
        