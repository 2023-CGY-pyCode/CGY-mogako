import sys
input = sys.stdin.readline

N, C = tuple(map(int, input().split()))

arr = []
for i in range(N):
    number = int(input())
    arr.append(number)
    

arr.sort()

sarr = []
# sarr.append(arr[0])
# for i in range(1, N):
#     sarr.append(sarr[i-1]+arr[i])

print(arr)

