import sys
input = sys.stdin.readline

N, M, Q = tuple(map(int, input().split()))

# matrix = [[0] * (M+1) for _ in range(N+1)]

rows = [0] * 500001
columns = [0] * 500001

for _ in range(Q):
    a, b, c = map(int, input().split())
    
    if a == 1:
        columns[b] += c
    elif a == 2:
        rows[b] += c
        
for i in range(1, N+1):
    for j in range(1, M+1):
        print(columns[i] + rows[j], end=" ")
    print()
            

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         print(matrix[i][j], end=" ")
#     print()
    
