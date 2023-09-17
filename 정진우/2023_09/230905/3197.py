import sys
from collections import deque
R, C = map(int, input().split())

arr = []
for _ in range(R):
    arr.append(list(input()))

if R == 1 and C == 1:
    print(0)
    exit()    
    
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
flag = 1
# print(arr)
def bfs(i, j, flag):
    dq = deque()
    dq.append((i,j))
    
    arr[i][j] = flag

    
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C: # 조건 안이면서
                if arr[ny][nx] == '.': # 백조 근처에 있는 것이 물일경우
                    arr[ny][nx] = flag
                    dq.append((ny, nx))

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L': # BFS를 통해 자기자신 포함한 집합을 구성
            bfs(i, j, flag)
            flag += 1
            
days = 0

one_step = []
two_step = []
zero_step = []
                
for i in range(R):
    for j in range(C):
        if arr[i][j] == 1: # 한쪽
            one_step.append((i, j))
        
        elif arr[i][j] == 2: # 다른쪽
            two_step.append((i, j))
    
        elif arr[i][j] == '.':
            zero_step.append((i, j ))

while True:
    # [print(arr[i]) for i in range(len(arr))]

    tmp_one_step = []
    tmp_two_step = []
    tmp_zero_step = []
    
    for step in zero_step:

        y, x = step
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C: # 조건 안이면서
                if arr[ny][nx] == 1 or arr[ny][nx] == 2: # 1일경우
                    continue # 아무것도 안함
                else:
                    arr[ny][nx] = '.' # X일경우 혹은 . 인데 속하지 않은경우 1로 초기화
                    
                    tmp_zero_step.append((ny, nx))
                    
    zero_step = tmp_zero_step
    for step in one_step:

        y, x = step
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C: # 조건 안이면서
                if arr[ny][nx] == 1: # 1일경우
                    continue # 아무것도 안함
                elif arr[ny][nx] == 2: # 2일경우 and 1과 2가 아직 만나지 않으면서 서로 붙어있는 경우
                    # [print(arr[i]) for i in range(len(arr))]
                    print(days) # 오리가 만남
                    exit()
                elif arr[ny][nx] == '.':
                    arr[ny][nx] = 1 # X일경우 혹은 . 인데 속하지 않은경우 1로 초기화
                    bfs(ny, nx, 1)
                    
                elif arr[ny][nx] == 'X':
                    arr[ny][nx] = 1
                    tmp_one_step.append((ny, nx))
                    
    one_step = tmp_one_step
                    
    for step in two_step:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        y, x = step
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C: # 조건 안이면서
                if arr[ny][nx] == 2: # 1일경우
                    continue # 아무것도 안함
                elif arr[ny][nx] == 1: # 2일경우 
                    days+=1
                    print(days) # 오리가 만남
                    exit()
                elif arr[ny][nx] == '.':
                    arr[ny][nx] = 2 # 빙판일경우 혹은 . 인데 속하지 않은경우 1로 초기화
                    bfs(ny, nx, 2)
                else:
                    arr[ny][nx] = 2
                    tmp_two_step.append((ny, nx))
                    
    two_step = tmp_two_step
                    
    days += 1
        
    
    
    
            
