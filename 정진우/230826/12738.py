import bisect
N = int(input())

arr = []
for item in map(int, input().split()):
    if not arr:
        arr.append(item)
    
    elif arr:
        if arr[-1] < item:
            arr.append(item)
        else:
            idx = bisect.bisect_left(arr, item) # 어디들어갈 수 있는지 찾는다
            arr[idx] = item
        

print(len(arr))