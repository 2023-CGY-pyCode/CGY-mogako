import bisect
N = int(input())

arr = []
arr_total = [] 
for idx, item in enumerate(map(int, input().split())):
    if not arr:
        arr.append(item)
        arr_total.append((item, 1))
    
    elif arr:
        if arr[-1] < item:
            arr.append(item)
            arr_total.append((item, len(arr)))
        else:
            idx = bisect.bisect_left(arr, item) # 어디들어갈 수 있는지 찾는다
            arr[idx] = item
            arr_total.append((item, idx+1))
        
print(len(arr))
max_len = len(arr)
arr2 = []
print(arr_total )
for item in arr_total[::-1]:
    value, idx = item
    if idx == max_len:
        max_len -= 1
        arr2.append(value)
        
print(*arr2[::-1])
        
    