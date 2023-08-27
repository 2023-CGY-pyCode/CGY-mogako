import sys
import bisect

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split()))) # A, B
    

arr.sort(key=lambda x:x[1]) # B를 기준으로 오름차순 정렬

lis = [0]
lis_total = [(0, 0)]
for item in arr: 
    a, b = item # b는 이미 오름차순되어있음 즉 a만 봐도됨 
    
    if lis[-1] < a: # 마지막에 있는 것보다 클경우 그냥 뒤에 붙임
        lis.append(a)
        lis_total.append((len(lis)-1, a)) # 역추적 하기 위한 배열 (idx, value)
    
    else: # 마지막에 있는 것보다 작을경우 bisect를 통해서 삽입할 위치를 지정 
        idx = bisect.bisect_left(lis, a) # a를 어디에 삽입하면 좋을까?
        lis[idx] = a #
        lis_total.append((idx, a)) # 역주적하기 위한 배열 idx와 value pair
        
max_len = len(lis)-1 # lis의 길이 0을 빼줘야함

# debug
# print(lis)
# print(lis_total)
results = []
for item in lis_total[::-1]:
    idx, value = item 
    if idx == max_len:
        max_len-=1
        
    else:
        results.append(value)
    

results.sort()
print(len(results))
for value in results:
    print(value)
    
    

        