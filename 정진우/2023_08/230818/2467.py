N = int(input())

arr = list(map(int, input().split()))

start, end = 0, N-1

near_zero = 1e8
a, b = 0, 0


while start < end:
    if near_zero > abs(arr[end] + arr[start]):
        near_zero = abs(arr[end] + arr[start])
        a, b = arr[start], arr[end]
        end -= 1
    else:
        start += 1
        
print(a, b)