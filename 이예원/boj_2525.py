import sys

h, m = map(int, sys.stdin.readline().split())
plus_time = int(sys.stdin.readline())

plus_m = plus_time + m
plus_h = plus_m // 60
cur_m = plus_m % 60
cur_h = (h + plus_h) % 24

print(cur_h, cur_m)