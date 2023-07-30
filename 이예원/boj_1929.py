import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n):
    isTrue = True
    for j in range(2, i):
        if i % j == 0:
            isTrue = False
            break
    if isTrue:
        print(i)