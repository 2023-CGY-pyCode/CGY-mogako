from collections import deque
M,N,K = tuple(map(int, input().split()))

arr = [[0] * (N+1) for _ in range(M+1)] # [0~N,0], [0, 0~M] 안씀 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# for a in arr:
#     print(a)

for _ in range(K): # M = y, N = x
    x1,y1,x2,y2 = tuple(map(int, input().split()))
    
    '''
    0 2 4 4
    1 3
    1 4
    2 3
    2 4
    3 3
    3 4
    4 3
    4 4
    '''
    for y in range(y1+1, y2+1):
        for x in range(x1+1, x2+1):
            arr[y][x] = 1
            
checked = [[0] * (N+1) for _ in range(M+1)] # [0~N,0], [0, 0~M] 안씀 
count = []
def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    count_square = 0
    while dq:
        i, j = dq.pop()
        # print(i,j)
        if checked[i][j] == 0:
            checked[i][j] = 1
            count_square += 1
        else:
            continue
        for d in range(4):
            if i + dy[d] >= 1 and i + dy[d] < M+1 and j + dx[d] >= 1 and j + dx[d] < N+1:
                # print(i+dy[d], j+dx[d])
                if arr[i+dy[d]][j+dx[d]] == 0:
                    dq.append((i+dy[d], j+dx[d]))
                
    return count_square
                
        
    
for i in range(1, M+1):
    for j in range(1, N+1):
        if checked[i][j] == 0 and arr[i][j] == 0:
            count.append(bfs(i, j))
        

count.sort()
           
print(len(count))
for i in count:
    print(i, end=" ")
# for a in arr:
#     print(a)
