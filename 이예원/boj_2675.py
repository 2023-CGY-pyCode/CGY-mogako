import sys

n = int(sys.stdin.readline())

input_list = []
for _ in range(n):
    input_list.append(sys.stdin.readline().split())

for repeat, target in input_list:
    for _, c in enumerate(target):
        print(int(repeat) * c, end='')
    print('')