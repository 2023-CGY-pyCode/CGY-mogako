import sys
pocket_dict_str = {}
pocket_dict_num = {}

N, M = tuple(map(int, input().split()))

for i in range(N):
    pocketmon = str(sys.stdin.readline()).replace("\n", "")
    
    pocket_dict_str[pocketmon] = i+1
    
for k, v in pocket_dict_str.items():
    
    pocket_dict_num[v] = k


for i in range(M):
    pocketmon = str(sys.stdin.readline()).replace("\n", "")
    
    if pocketmon.isdigit():
        print(pocket_dict_num[int(pocketmon)])
    else:
        print(pocket_dict_str[pocketmon])