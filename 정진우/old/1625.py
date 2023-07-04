N = int(input())
hotel = []
for i in range(N):
    li = input() # . or X
    hotel.append(li)
    

# 세로
row_can = 0

for i in range(N):
    row_check = 0
    for j in range(N):
        if hotel[j][i] == '.':
            row_check += 1
            if row_check == 2:
                row_can += 1
        elif hotel[j][i] == 'X':
            row_check = 0

# 가로
column_can = 0
for i in range(N):
    column_check = 0
    for j in range(N):
        if hotel[i][j] == '.':
            column_check += 1
            if column_check == 2:
                column_can += 1
        elif hotel[i][j] == 'X':
            column_check = 0
            
print(column_can, row_can) # 가로 세로
    
