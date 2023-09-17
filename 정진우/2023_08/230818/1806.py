N, S = map(int, input().split())

arr = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    arr[i] += arr[i-1]  # prefix sum
    

start = end = 1
min_length = 1e8
# print(arr)
while start <= end:
    # print(start, end)
    # print(min_length)
    if end >= N+1: # end가 배열을 넘어가면 안됨
        break
    if start == end:
        if arr[start] - arr[start-1] >= S:
            min_length = 1
            break
        else:
            end += 1
        continue
    if arr[end] - arr[start-1] >= S: # 구간 누적합이 S보다크면
        min_length = min(end-start+1, min_length) # 구간 누적합 길이 갱신
        # print(min_length)
        start += 1 # 길이를 작게하고 한번더 갱신해봄
    else:
        end += 1 # end 길이를 해봄
    
if min_length >= 1e8:
    print(0)
else:
    print(min_length)
        
    
    