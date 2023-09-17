N, M, y, x, K = tuple(map(int, input().split()))

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    
operations = list(map(int, input().split()))

state = [0, 0, 0, 0, 0, 0, 0] # 1,2,3,4,5,6 만 사용
cur_position = [y, x]
dx = [0, 1, -1, 0, 0] # 동서북남
dy = [0, 0, 0, -1, 1]
def roll(d):
    
    if d == 1: # 동쪽 #3->6->4->1
        temp = state[3]
        state[3] = state[1]
        state[1] = state[4]
        state[4] = state[6]
        state[6] = temp
        
    elif d == 2:
        temp = state[1]
        state[1] = state[3]
        state[3] = state[6]
        state[6] = state[4]
        state[4] = temp
                
    elif d == 4: # 남쪽
        temp = state[5]
        state[5] = state[1]
        state[1] = state[2]
        state[2] = state[6]
        state[6] = temp
        
    elif d == 3: # 북쪽
        temp = state[1]
        state[1] = state[5]
        state[5] = state[6]
        state[6] = state[2]
        state[2] = temp
    
    if board[cur_position[0]][cur_position[1]] == 0:
        board[cur_position[0]][cur_position[1]] = state[6]
    else:
        state[6] = board[cur_position[0]][cur_position[1]]
        board[cur_position[0]][cur_position[1]] = 0
    
for operation in operations:
    y, x = cur_position
    ddy = y + dy[operation]
    ddx = x + dx[operation]
    if 0 <= ddx < M and 0 <= ddy < N:
        cur_position[0] = ddy
        cur_position[1] = ddx
        roll(operation)
        # print(board)
        # print(state)
        print(state[1])
        
    
    
    

    

        