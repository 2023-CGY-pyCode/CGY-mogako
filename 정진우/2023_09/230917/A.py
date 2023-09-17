A, B = map(int, input().split())

min_value = min(A,B)

if A>B:
    print(min_value * 2 + 1)
else:
    print(min_value * 2 - 1)