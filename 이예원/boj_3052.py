import sys

num_list = [int(sys.stdin.readline()) for _ in range(10)]

div_list = []
for i in range(10):
    div = num_list[i] % 42
    if div not in div_list:
        div_list.append(div)

print(len(div_list))
