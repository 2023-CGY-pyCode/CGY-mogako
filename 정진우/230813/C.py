import sys
import heapq
import math

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
min_heap = arr
max_heap = [-i for i in arr]
heapq.heapify(min_heap) # m
heapq.heapify(max_heap) # max_heap


# print(min_heap, max_heap)
T = N*30
result_arr = []
result_arr.append(-max_heap[0] - min_heap[0]) # cur_diff

for _ in range(T):
    min_number = heapq.heappop(min_heap) * 2 # 최솟값 하나 골라서 2 곱함 
    heapq.heappush(min_heap, min_number)
    heapq.heappush(max_heap, -min_number)
    cur_diff = -max_heap[0] - min_heap[0]
    min_diff = min(cur_diff, min_diff)
    
print(min_diff)
# print(result_arr)
    
    





