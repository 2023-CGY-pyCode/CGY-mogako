from itertools import combinations

from collections import defaultdict, Counter

N, S = map(int, input().split())

arr = list(map(int, input().split()))

# print(arr)

start = 0
end = len(arr)
mid = len(arr) // 2 

def get_all_combinations(start, end):
    dd = defaultdict(int)
    for i in range(0, end-start+2): # 모든 부분수열의 합을 구할 조합, 0,1,2 - 3,4 # 공집합을 구해야, 한쪽집합에서만 정답이나오는 경우를 구할 수 있음
        li = combinations(arr[start:end+1], i) # 0인것은 없음
        for item in map(sum , li):
            dd[item] += 1
             
    return dd


left_dict = get_all_combinations(start, mid)
right_dict = get_all_combinations(mid+1, end)

# print(left_dict, right_dict)
count =0
for k, v in left_dict.items():
    if S-k in right_dict: # 오른쪽 dict에 잇다면
        count += v * right_dict[S-k]
        
if S == 0:
    count -= 1 # S가 0인경우, 공집합과 공집합인 경우를 더하므로

print(count) 