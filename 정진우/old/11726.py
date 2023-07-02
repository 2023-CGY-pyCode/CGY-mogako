arr = []
arr.append(0) #0
arr.append(1) # 1
arr.append(2) # 2
arr.append(3) # 3

n = int(input())

for i in range(4, 1001):
    arr.append((arr[i-1] + arr[i-2])%10007)
    
print(arr[n])
