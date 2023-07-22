import sys

n = int(sys.stdin.readline())
for i in range(n):
    s_list = sys.stdin.readline().split()
    print('Case #{0}: '.format(i+1), end='')
    for i in range(1, len(s_list)+1):
        print(s_list[-i], end=' ')

    print('')