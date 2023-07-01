import sys

num_list = list(map(int, sys.stdin.readline().split()))
max_num = max(num_list)
min_num = min(num_list)

if max_num == min_num:
    print(10000 + max_num * 1000)
else:
    max_count = num_list.count(max_num)
    min_count = num_list.count(min_num)
    if max_count == 1 and min_count == 1:
        print(max_num * 100)
    elif max_count == 2:
        print(1000 + max_num * 100)
    elif min_count == 2:
        print(1000 + min_num * 100)