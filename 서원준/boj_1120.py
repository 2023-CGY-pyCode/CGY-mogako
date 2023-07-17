# A < B
import sys
A, B = input().split()

ans = float('inf')

for i in range((len(B)-len(A)+1)):
    tmp = 0
    for j in range(len(A)):
        if B[i+j]!=A[j]:
            tmp += 1
    if ans>tmp:
        ans = tmp

print(ans)
