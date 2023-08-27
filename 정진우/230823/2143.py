import bisect
T = int(input())

n = int(input())
A = list(map(int , input().split()))

m = int(input())
B = list(map(int, input().split()))

sumA, sumB = A, B

for i in range(n):
    for j in range(i+1, n):
        sumA.append(sum(A[i:j+1])) # 부분합 저장
        
for i in range(m):
    for j in range(i+1, m):
        sumB.append(sum(B[i:j+1])) # 부분합 저장
        
sumA.sort(), sumB.sort() # 부분합들을 오름차순 정렬

count = 0
for i in range(len(sumA)):
    right = bisect.bisect_right(sumB, T-sumA[i]) # upper bound
    left = bisect.bisect_left(sumB, T-sumA[i]) # lower bound 
    count += right-left # upper bound - lower bound = count
    
print(count)
    