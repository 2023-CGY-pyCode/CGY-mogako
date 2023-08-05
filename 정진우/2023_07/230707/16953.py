from collections import deque

arr = deque()

A, B = tuple(map(int, input().split()))

arr.append((A, 1))
while True:
    if not len(arr):
        print(-1)
        break
    
    number, depth = arr.popleft()
    # print(number, depth)
    if number > B:
        continue
    if number == B:
        print(depth)
        break
    arr.append((2*number, depth+1))
    arr.append((10*number+1, depth+1))

    
