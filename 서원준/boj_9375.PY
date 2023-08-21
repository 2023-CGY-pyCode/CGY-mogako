t = int(input())

for _ in range(t):
    n = int(input())
    d = dict()
    for _ in range(n):
        c1, c2 = input().split()
        if c2 in d:
            d[c2] += 1
        else:
            d[c2] = 1

    result = 1
    for key in d:
        result *= (d[key] + 1)
    print(result - 1)
