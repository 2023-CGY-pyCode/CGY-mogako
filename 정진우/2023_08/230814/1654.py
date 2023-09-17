N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
    

start , end = 1, max(arr)


while start <= end:
    mid = (end+start) // 2
    count = 0
    for i in range(N):
        count += arr[i] // mid
        
    
    if count >= K:
        start = mid + 1
    else:
        end = mid - 1
        
    # print(start, mid, end)
        

print(end)
        
    