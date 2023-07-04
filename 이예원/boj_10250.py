import sys

n = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for h, w, n in input_list:
    floor = h if n % h == 0 else n % h
    room_num = n // h if n % h == 0 else n // h + 1
    print(floor * 100 + room_num)