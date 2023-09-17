N = int(input())


arr = [[0] * N for _ in range(N)]
cur_value = 1

cur_y = cur_x = 0

direction = 0 # 0, 1, 2, 3 동남서북

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr[0][0] = 1
while cur_value != N ** 2 :
    nx = dx[direction] + cur_x
    ny = dy[direction] + cur_y

    if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0:
        cur_value += 1
        cur_y = ny
        cur_x = nx
        arr[cur_y][cur_x] = cur_value
        
    else:
        direction = (direction + 1) % 4

    print(direction)
    print(arr)


[print(*arr[i]) for i in range(len(arr))]

    

