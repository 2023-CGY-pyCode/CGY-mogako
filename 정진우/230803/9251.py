s1 = input()
s2 = input()

if len(s1) > len(s2):
    temp = s2
    s2 = s1
    s1 = temp
    
    
# print(s1, s2)
dp = [0] * (len(s1)+1)
for i in range(len(s1)-1, -1, -1):
    dp[i] = dp[i+1]
    for k in range(i, len(s1)):
        for j in range(len(s2)-1, i-1, -1):
            # print(k, j)
            if s1[k] == s2[j]:
                dp[k] = dp[k+1] + 1
    # print(dp)
            
            
            
print(max(dp))         
# print(dp)
        