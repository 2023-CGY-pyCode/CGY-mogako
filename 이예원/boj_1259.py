import sys

while True:
    s = sys.stdin.readline().rstrip()
    isTrue = True
    if s == '0':
        break

    for i, c in enumerate(s):
        rev = -1 * (i + 1)
        if s[i] != s[rev]:
            print('no')
            isTrue = False
            break

    if isTrue:
        print('yes')
