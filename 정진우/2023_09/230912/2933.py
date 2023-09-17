from collections import deque

R, C = map(int, input().split())

dx = [1, 0, -1, 0] # 동남서북
dy = [0, 1, 0, -1]

def bfs(y, x, visited):
    is_ground = False
    dq = deque()
    dq.append((y, x))
    trace = []
    while dq:
        y, x = dq.popleft()
        
        if y == R-1: # 그라운드에 미네랄이 있다
            is_ground = True
            
        if visited[y][x] == 1:
            continue
                    
        visited[y][x] = 1 # 방문처리
        trace.append([y, x]) # 추적
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C: # 조건안에서
                if arr[ny][nx] == 'x': # 미네랄이면
                    dq.append((ny, nx)) # BFS
    
    if trace:
        return is_ground, trace
    
    else:
        return True, []
    
def process():
    visited = [[0] * C for _ in range(R)] # 방문배열
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'x':
                # [print(arr[i]) for i in range(R)]
                is_ground, trace = bfs(i, j, visited)
                # [print(arr[i]) for i in range(R)]
                # print(is_ground, trace)
                
                if is_ground == False: # 그라운드에 미네랄이 없다? 중력에 의해 떨어짐
                    # print("Event")
                    while is_ground == False:
                        for y, x in trace: 
                            arr[y][x] = '.' # 빈공간으로 만들고
                            
                        for y, x in trace: 
                            arr[y+1][x] = 'x' # 중력에 의해 떨어짐
                        
                        # [print(arr[i]) for i in range(R)]
                        # print()
                        trace = [[item[0]+1, item[1]] for item in trace] # trace 갱신
                        
                        for y, x in trace:
                            if y == R-1: # 땅인경우
                                is_ground = True
                                break
                            
                            if arr[y+1][x] == 'x' and [y+1, x] not in trace : # 바로 아래 이미 클러스터가 있을 경우, 중복이 아닌경우r
                                is_ground = True # 
                                break
                        # visited = [[0] * C for _ in range(R)] # 방문배열 초기화
                        # is_ground, trace = bfs(i+1, j, visited)
                
                    # [print(arr[i]) for i in range(R)]
                    return
                
                        
                        
                        
                        

def throw_stick(height, direction):
    a_h = R-height # arr상 실제 높이
    
    if direction == 0: # 왼쪽
        for i in range(C): # 0~C 
            if arr[a_h][i] == 'x':
                arr[a_h][i] = '.' # 파괴
                process() # 합치는 프로세스
                break
    
    elif direction == 1: # 오른쪽
        for i in range(C-1, -1, -1):#  C-1 ~ 0
            if arr[a_h][i] == 'x':
                arr[a_h][i] = '.' # 파괴
                process() # 합치는 프로세
                break

arr = []
for _ in range(R): # 환경구축
    st = list(input())
    arr.append(st) 
    
    
N = int(input()) # 막대기 던진 횟수
direction = 0 # 처음은 0

H_list = list(map(int, input().split())) # 막대 던진 높이
for h in H_list:
    # print("수행", h)
    throw_stick(h, direction)
    direction = 1 - direction
    # [print(arr[i]) for i in range(R)]

[print(''.join(arr[i])) for i in range(R)]
# print(direction)
    


    
    