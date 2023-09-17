import sys
from itertools import count
input =sys.stdin.readline

N = int(input())

sticks = [0] * 100001
li = list(map(int, input().split()))

M = int(input())

targets = list(map(int, input().split()))
MX = max(max(li), max(targets))

dp = [0] * (MX+1)
for a in li:
    dp[a] += 1
    
    
# ----------------------------------------------------------------------------------
# 약수를 구하고 그 약수로 늘린 막대의 갯수를 더해줌
# ----------------------------------------------------------------------------------  

# for i in range(2, MX+1): # 최대값 까지
#     for j in count(1):
#         if j * j > i: # j가 root i를 넘어간다면? , 약수가 될 수 없음
#             break
#         if i % j == 0 : # j가 i의 약수라면
#             dp[i] += dp[j] # j가 가지고 있는 값을 dp[i]에 넣어줌
#             if j * j != i and j != 1: # 만약 j가 루트값이 아니고 1이 아니라면 
#                 dp[i] += dp[i // j] # j로 나눠지는 값 ex) 6 = 2 * 3 (3)부분을 dp[i]에 넣어줌
                
# ----------------------------------------------------------------------------------
# 배수로 푸는 방법 i를 1부터 증가시켜주면서 i의 배수 j에 대하여 Dj에 Di를 더해주는 방향
# O(KlogK)
# ----------------------------------------------------------------------------------  

for i in range(1, MX+1): # 배수 base
    for j in range(2*i, MX+1, i): # 배수에 해당하는 값에 대하여 i로 늘린 막대의 갯수를 더해줌
        dp[j] += dp[i]
        
        
        
    # Case
    # 5
    # 1 2 3 4 5
    # 6
    # 1 2 3 4 5 6
    
    # dp array init
    # 1 1 1 1 1 0
    # 1 2 2 2 2 1 (i = 1)
    # 1 2 2 4 2 3 (i = 2)
    # 1 2 2 4 2 5 (i = 3) ANS
    # 1 2 2 4 2 5 (i = 4)
    # 1 2 3 4 2 5 (i = 5)
    # 1 2 3 4 2 5 (i = 6)
    
    
print(*(dp[i] for i in targets))
                
        
