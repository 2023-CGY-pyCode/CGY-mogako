import sys

s = sys.stdin.readline().rstrip()
result = [-1 for _ in range(26)]
for i, c in enumerate(s):
    current = ord(c.lower()) - 97
    if result[current] == -1:
        result[current] = i

print(' '.join(map(str, result)))