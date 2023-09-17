n = int(input())

arr = []

for i in range(n):

    li = list(map(int, input().split()))
    arr.append(li)
    
for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
            
# print(arr)
print(max(arr[n-1]))
        
    
    