N = int(input())

li = list(map(int, input().split()))

count = 0
DP = [0] * N
answer = 0

for i in range(len(li)):
    DP[i] = 1
    for j in range(i):
        if li[i] > li[j]:
            DP[i] = max(DP[i], DP[j]+1)
        
    answer = max(answer, DP[i])
    

target = answer
result = []

# print(DP)
for idx, item in enumerate(DP[::-1]):
    idx = N-idx-1
    if item == target:
        result.append(li[idx])
        target-=1
        
        
print(answer)
print(*result[::-1])
