import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0] # 동북서남
dy = [0, -1, 0, 1] # 0123

arr = []

R, C, T = tuple(map(int, input().split()))

for _ in range(R):
    li = list(map(int, input().split()))
    arr.append(li)
    
# 확산 phase # 공기청정기 데이터도 같이 모음ㅁㅁㄱe

def spreading_process():
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 4: # 5보다 커야 확산이 일어남
                spreading(i, j)
            elif arr[i][j] == -1:
                air_cleaner_list.append((i, j))
                

    for spread in spreading_pending_list:
        y, x, value = spread  
        arr[y][x] += value
    

def spreading(y, x):
    count = 0
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < C and y+dy[i] >= 0 and y+dy[i] < R: # 벽을 안넘으면 확산
            if arr[y+dy[i]][x+dx[i]] == -1: # 공기청정기로는 확산이 안됨
                continue 
            spreading_pending_list.append((y+dy[i], x+dx[i], arr[y][x]//5))
            count += 1
    arr[y][x] = arr[y][x] - (arr[y][x]//5)*count 
    
    
    
    
# 공기 청정기 phase
def air_cleaner():
    # print(pending_air_cleaner_list[::-1])
    # print(arr)
    for air_clean in pending_air_cleaner_list[::-1]: # 역으로 해야 순서가 안꼬임
        y, x, value, d = air_clean
        if arr[y+dy[d]][x+dx[d]] == -1:
            arr[y][x] = 0
        else:
            arr[y+dy[d]][x+dx[d]] = value
        # print(arr[0])
            
def air_cleaner_process():
    global pending_air_cleaner_list
    for idx in range(2):
        if idx == 0: # 위쪽 공기 청정기
            y, x = air_cleaner_list[idx]
            cur_y, cur_x = y, x+1 # 처음은 동쪽
            d = 0
            # arr[cur_y][cur_x] = d
            while arr[cur_y][cur_x] != -1:
                if cur_x+dx[d] >= 0 and cur_x+dx[d] < C and cur_y+dy[d] >= 0 and cur_y+dy[d] < R: # 벽아니면 방향 그대로
                    pending_air_cleaner_list.append((cur_y, cur_x, arr[cur_y][cur_x], d))
                    cur_y, cur_x = cur_y+dy[d], cur_x+dx[d]
                    # print(cur_y, cur_x)
                    #air_cleaner_matrix[cur_y+dy[d]][cur_x+dx[d]] = d # 방향만 가지고 있음
                else: # 벽이면 회전
                    d = (d+1)%4
            y, x = air_cleaner_list[idx]
            arr[y][x+1] = 0
        elif idx == 1: # 아래쪽 공기 청정기
            y, x = air_cleaner_list[idx]
            cur_y, cur_x = y, x+1 # 처음은 동쪽
            d = 0
            # arr[cur_y][cur_x] = d
            while arr[cur_y][cur_x] != -1:
                if cur_x+dx[d] >= 0 and cur_x+dx[d] < C and cur_y+dy[d] >= 0 and cur_y+dy[d] < R: # 벽아니면 방향 그대로
                    pending_air_cleaner_list.append((cur_y, cur_x, arr[cur_y][cur_x], d))
                    cur_y, cur_x = cur_y+dy[d], cur_x+dx[d]
                    #air_cleaner_matrix[cur_y+dy[d]][cur_x+dx[d]] = d # 방향만 가지고 있음
                else: # 벽이면 회전 -90도
                    d = (d-1)
                    if d < 0:
                        d = 3
            y, x = air_cleaner_list[idx]
            arr[y][x+1] = 0
                        
        air_cleaner()
        pending_air_cleaner_list = []
    

for _ in range(T):
    # reset
    spreading_pending_list = []
    air_cleaner_list = []
    pending_air_cleaner_list = []
    spreading_process()
    # print(air_cleaner_list)
    air_cleaner_process()
    
# print(arr)
print(sum([sum(i) for i in arr]) + 2)