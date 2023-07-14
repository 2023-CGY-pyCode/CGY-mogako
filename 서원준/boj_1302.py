n = int(input())

d = dict()
for _ in range(n):
    s = input()
    if s not in d:
        d[s] = 0
    d[s] +=1

sd = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(sd[0][0])