import sys

row, col = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().rstrip() for _ in range(row)]

cur_r, cur_c = 0, 0
result_list = []
while True:
    # W, B로 먼저 시작할 경우 각각 확인 (0 row = 0,짝수 , 1 row 홀수 ...)
    w_b_result = [0, 0] # w로 시작, b로 시작
    for i in range(cur_r, cur_r+8):
        for j in range(cur_c, cur_c+8):
            if (i - cur_r) % 2 == 0: # 짝수 row (0부터 시작)
                if (j - cur_c) % 2 == 0: # 짝수 col (0부터 시작)
                    if chess[i][j] != 'W': # B면 고쳐야 하므로 1 더함
                        w_b_result[0] += 1
                    elif chess[i][j] != 'B':
                        w_b_result[1] += 1
                else:
                    if chess[i][j] == 'W': # B면 고쳐야 하므로 1 더함
                        w_b_result[0] += 1
                    elif chess[i][j] == 'B':
                        w_b_result[1] += 1
            else: # 홀수 row
                if (j - cur_c) % 2 == 0: # 홀수 col
                    if chess[i][j] != 'B': # B면 고쳐야 하므로 1 더함
                        w_b_result[0] += 1
                    elif chess[i][j] != 'W':
                        w_b_result[1] += 1
                else:
                    if chess[i][j] == 'B': # B면 고쳐야 하므로 1 더함
                        w_b_result[0] += 1
                    elif chess[i][j] == 'W':
                        w_b_result[1] += 1

    result_list.append(min(w_b_result))
    cur_c += 1
    if cur_c+8 > col:
        if cur_r+9 > row:
            break
        else:
            cur_r += 1
            cur_c = 0

print(min(result_list))
