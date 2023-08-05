import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    number = int(input())
    arr.append(number)
    

arr.sort()

count = []
if N >= 2:
    count.append(arr[0]+arr[1])
else:
    count.append(0)


i = 2
while i < N:
    if i+1 < N:
        if arr[i] == arr[i+1]:
            count.append(2*arr[i])
            count.append(count[-1]+count[-2])
            i = i + 2
            continue
    
    count.append(count[-1]+arr[i])
    i = i + 1
    
print(sum(count))