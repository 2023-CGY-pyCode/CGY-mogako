import sys
from collections import deque
M, N = tuple(map(int, input().split()))

# arr = [[] * M for _ in range(N)] # M*N 2d array
arr = []
bfs_list = deque()
zero_count = 0
zero_list = []
bfs_li = deque()
iter_count = 0
for i in range(N):
    li = list(map(int,sys.stdin.readline().split()))

    arr.append(li)
        
        

zero_count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs_li.append((i, j, 0)) # 1인 (i,j) 저장
        # if arr[i][j] == 0:
        #     zero_count += 1               
# zero_list.append(zero_count) # 이게 0이면 종료, 

# if len(zero_list) == 1:
#     if zero_list[-1] == 0:
#         iter_count = 0
# if len(zero_list) >= 2:
#     if zero_list[-1] == zero_list[-2] and zero_list[-1] != 0:
#         iter_count = -1
#     elif zero_list[-1] == 0:
#         iter_count = iter_count
max_count = 0
while len(bfs_li):
    i, j, count = bfs_li.popleft()
    max_count = count if max_count < count else max_count
    if arr[i][j] == -1:
        continue
    arr[i][j] = -1 # 방문했음
    if i-1 >= 0: # 북
        if arr[i-1][j] != -1 and arr[i-1][j] != 1:
            arr[i-1][j] = 1
            bfs_li.append((i-1, j, count+1))
    if i+1 <= N-1: # 남
        if arr[i+1][j] != -1 and arr[i+1][j] != 1:
            arr[i+1][j] = 1
            bfs_li.append((i+1, j, count+1))
    if j-1 >= 0: # 서
        if arr[i][j-1] != -1 and arr[i][j-1] != 1:
            arr[i][j-1] = 1
            bfs_li.append((i, j-1, count+1))
    if j+1 <= M-1: # 동
        if arr[i][j+1] != -1 and arr[i][j+1] != 1:
            arr[i][j+1] = 1
            bfs_li.append((i, j+1, count+1))
        # bfs_li = deque(set(bfs_li))
    # if bfs_li:
    #     iter_count+=1   

for i in arr:
    if 0 in i:
        max_count = -1 
        break
            
              
        
print(max_count)