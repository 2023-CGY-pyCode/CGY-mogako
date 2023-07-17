import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = a * b * c
result = [0 for _ in range(10)]
for n in str(num):
    result[int(n)] += 1

for i in range(10):
    print(result[i])