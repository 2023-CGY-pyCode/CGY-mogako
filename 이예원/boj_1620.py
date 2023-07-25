import sys

n, m = map(int, sys.stdin.readline().split())
num = [str(i) for i in range(1, 10)]
d = dict()
for i in range(1, n+1):
    d[str(i)] = sys.stdin.readline().rstrip()

rev_d = dict(map(reversed, d.items()))

for _ in range(m):
    i = sys.stdin.readline().rstrip()
    if i[0] in d.keys():
        print(d[i])
    else:
        print(rev_d[i])