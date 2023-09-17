import copy

N, M = map(int, input().split())

arr = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cctv_list = []
for i in range(N):
    arr.append(list(map(int, input().split()))) # 입력
    
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 or arr[i][j] == 6 or arr[i][j] == '#':
            continue
        elif arr[i][j] == 5: # 5는 회전할 필요없으니 전처리
            for c in range(4): 
                multiplier = 0
                while True:
                    multiplier += 1
                    nx = j + dx[c] * multiplier
                    ny = i + dy[c] * multiplier
                    if 0 <= nx < M and 0 <= ny < N: # 범위
                        if arr[ny][nx] == 6: # 벽이면 
                            break # 벽이여도 멈춤
                        elif arr[ny][nx] == 0:
                            arr[ny][nx] = '#'
                    else:
                        break # 넘어가면 멈춤
        else:
            cctv_list.append([i, j, arr[i][j]]) #동쪽 부터 시작
            

zero_count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_count += 1

min_square = zero_count
change_count = 0
def process(temp_arr, i, j, c, d):
    count = 0
    if c == 1: # 한 쪽만 볼 수 있음
        multiplier = 0
        while True:
            multiplier += 1
            nx = j + dx[d] * multiplier
            ny = i + dy[d] * multiplier
            if 0 <= nx < M and 0 <= ny < N: # 범위
                if temp_arr[ny][nx] == 6: # 벽이면 
                    break # 벽이여도 멈춤
                elif temp_arr[ny][nx] == 0:
                    temp_arr[ny][nx] = '#'
                    count += 1
            else:
                break # 넘어가면 멈춤
            
    if c == 2: # 앞 뒤
        for idx in [d, (d+2)%4]:
            multiplier = 0
            while True:
                multiplier += 1
                nx = j + dx[idx] * multiplier
                ny = i + dy[idx] * multiplier
                if 0 <= nx < M and 0 <= ny < N: # 범위
                    if temp_arr[ny][nx] == 6: # 벽이면 
                        break # 벽이여도 멈춤
                    elif temp_arr[ny][nx] == 0:
                        temp_arr[ny][nx] = '#'
                        count += 1
                else:
                    break # 넘어가면 멈춤
                
    if c == 3: # 앞, 오른쪽 ,(0,1), (1,2), (2,3), (3,0)
        for idx in [d, (d+1)%4]:
            multiplier = 0
            while True:
                multiplier += 1
                nx = j + dx[idx] * multiplier
                ny = i + dy[idx] * multiplier
                if 0 <= nx < M and 0 <= ny < N: # 범위
                    if temp_arr[ny][nx] == 6: # 벽이면 
                        break # 벽이여도 멈춤
                    elif temp_arr[ny][nx] == 0:
                        temp_arr[ny][nx] = '#'
                        count += 1
                else:
                    break # 넘어가면 멈춤
        
    if c == 4: # 앞, 왼쪽, 오른쪽 ,(0,1,3), (1,2,0), (2,3,1), (3,0,1)
        for idx in [d, (d+1)%4, (d+3)%4]:
            multiplier = 0
            while True:
                multiplier += 1
                nx = j + dx[idx] * multiplier
                ny = i + dy[idx] * multiplier
                if 0 <= nx < M and 0 <= ny < N: # 범위
                    if temp_arr[ny][nx] == 6: # 벽이면 
                        break # 벽이여도 멈춤
                    elif temp_arr[ny][nx] == 0:
                        temp_arr[ny][nx] = '#'
                        count += 1
                else:
                    break # 넘어가면 멈춤
                
    return temp_arr, count
        
def check(temp_arr, cur, change_count):
    global min_square
    if cur == len(cctv_list):
        min_square = min(min_square, zero_count-change_count)
        # [print(*temp_arr[i]) for i in range(len(temp_arr))]
        # print()
        return
                
    # for idx in range(cur, len(cctv_list)):
    i, j, c = cctv_list[cur]
    for d in range(4):
        temp_arrt = copy.deepcopy(temp_arr)        
        temp_arrt, count = process(temp_arrt, i, j, c, d)
        check(temp_arrt, cur+1, change_count+count)           
        
    
    
# debug
# [print(*arr[i]) for i in range(len(arr))]
# print(cctv_list)

check(arr, 0, 0)
print(min_square)
        
                        
            
                    
            
    