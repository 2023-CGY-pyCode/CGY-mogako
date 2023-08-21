n, m = map(int, input().split())

d = dict()

for _ in range(n):
    id, pw = input().split()

    d[id] = pw


for _ in range(m):
    id = input()
    print(d[id])


