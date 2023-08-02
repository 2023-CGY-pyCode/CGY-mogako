from itertools import combinations
import sys
from collections import deque
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
# 배열 

chicken_house = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: #치킨집
            chicken_house.append((i, j)) # 치킨집 i, j를 튜플로넣음
        elif arr[i][j] == 1: # 집
            house.append((i, j))  
            # print("치킨")
    

c_list = list(combinations(chicken_house, M))

def bfs(y, x, c):
    min_value = 1000000
    for p in c:
        target_y, target_x = p
        min_value = min((abs(target_y-y) + abs(target_x-x)), min_value)
    return min_value
                    
                        
                
# print(c_list)

min_result = 100000
for c in c_list:
    result = 0
    for h in house:
        y, x = h
        d = bfs(y, x, c)
        # print(arr)
        result += d

    min_result = min(result, min_result)
    
print(min_result)
        
                        
                    
            


