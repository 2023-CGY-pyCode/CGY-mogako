import sys

input = sys.stdin.readline

N, M = map(int, input().split())

modulo_list = [0] * M

arr = list(map(int, input().split())) + [0]

for i in range(N):
    arr[i] += arr[i-1] 
    modulo_list[arr[i]%M] += 1

count = modulo_list[0]

print(modulo_list)
print(arr)
for i in modulo_list:
    count += (i * (i-1)) // 2
    
print(count)

