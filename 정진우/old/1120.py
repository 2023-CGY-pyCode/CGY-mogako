A, B = tuple(map(str, input().split()))


min_diff = len(A)
for i in range(len(B) - len(A) + 1):
    diff = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            diff += 1
    if min_diff > diff:
        min_diff = diff
    
        
print(min_diff)
        