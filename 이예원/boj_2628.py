import sys

col, row = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
cut_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

row_cut_index, col_cut_index = [], []
for where2cut, i in cut_list:
    if where2cut == 0:
        row_cut_index.append(i)
    else:
        col_cut_index.append(i)

row_cut_index.sort()
col_cut_index.sort()

prev_row, prev_col = 0, 0
row_list, col_list = [], []
for i in range(len(row_cut_index)):
    r = row_cut_index[i]
    row_list.append(r - prev_row)
    prev_row = r

    if i == len(row_cut_index) - 1:
        row_list.append(row - prev_row)

for i in range(len(col_cut_index)):
    c = col_cut_index[i]
    col_list.append(c - prev_col)
    prev_col = c

    if i == len(col_cut_index) - 1:
        col_list.append(col - prev_col)

if len(row_list) == 0:
    row_list.append(row)
elif len(col_list) == 0:
    col_list.append(col)

print(max(row_list) * max(col_list))