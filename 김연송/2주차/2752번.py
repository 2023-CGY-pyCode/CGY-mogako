import sys
a = list(map(int, sys.stdin.readline().split()))

a.sort();

print(*a)
