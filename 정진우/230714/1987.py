R,C = tuple(map(int, input().split()))

board = []

dx = [1, 0, -1, 0] # 동남서북
dy = [0, 1, 0, -1]

visited = [[0] * C for _ in range(R)]
alphabet_list = [0] * (ord('a') - ord('A') + 1) # 0번째 인덱스가 A를 나타냄
def dfs(y, x, depth):
    alphabet = ord(board[y][x]) - ord('A')
    max_depth = 0
    if alphabet_list[alphabet] == 0:
        alphabet_list[alphabet] = 1
    else:
        return depth-1
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < C and y+dy[i] >= 0 and y+dy[i] < R:
            cur_depth = dfs(y+dy[i], x+dx[i], depth+1)
            # print(alphabet_list) 
            max_depth = max(cur_depth, max_depth)
    alphabet_list[alphabet] = 0
    return max_depth
    
for _ in range(R):
    row = str(input())
    board.append(row)
    
count= dfs(0, 0, 1)
print(count)
    
