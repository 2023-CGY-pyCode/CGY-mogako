import sys
input = sys.stdin.readline


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = tuple(map(int, input().split()))
def robot_passfind(r, c, d, check): # # 0 = 북, 1 = 동, 2 = 남, 3 = 서
    # current_direction = d
    # print(r,c,d,check)
    backward = 0
    if arr[r][c] == 0:
        arr[r][c] = 2 # 현재칸 청소
        
    count = 0 
    for i in range(4):
        #if r+dx[i] >= 0 and r+dx[i] < M and c+dy[i] >= 0 and c+dy[i] < N:
        if arr[r+dy[i]][c+dx[i]] == 0:
            count += 1
                
    
    # 후진
    if d == 0 or d == 2:
        backward = abs(2-d)
    elif d == 1 or d == 3:
        backward = abs(4-d) 
        
    # count == 0 모두 청소되거나 벽
    if count == 0: 
        ddy = dy[backward]
        ddx = dx[backward]
        if arr[r+ddy][c+ddx] == 1:
            return check
        elif arr[r+ddy][c+ddx] == 2: # 청소한곳
            return robot_passfind(r+ddy, c+ddx, d, check) # 방향은 그대로 후진

    # 하나라도 갈 곴이 있을경우
    else:
        backward = d-1 if d-1 >= 0 else 3
        ddy = dy[backward]
        ddx = dx[backward]
        if arr[r+ddy][c+ddx] == 0: # 갈곳이 있는경우
            return robot_passfind(r+ddy, c+ddx, backward, check+1) # 회전했기 때문에 backward
        else:
            return robot_passfind(r, c, backward, check)
        


r,c,d = tuple(map(int, input().split())) # 0 = 북, 1 = 동, 2 = 남, 3 = 서

arr = []
for _ in range(N):
    li = list(map(int, input().split()))
    arr.append(li)
    
    
result = robot_passfind(r, c, d, 1)
print(result)
    

