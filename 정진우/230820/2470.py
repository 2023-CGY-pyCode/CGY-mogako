N = int(input())

arr = list(map(int, input().split()))

arr.sort()

start, end = 0, N-1

min_diff = 1e10
a, b = arr[0], arr[-1]

while start < end:
    sum = arr[start] + arr[end]
    if abs(sum) < min_diff: # 차이의 절댓값이 작을경우
        min_diff = abs(sum)
        a = arr[start]
        b = arr[end]
        
        if abs(sum) == 0:
            break
        
    if sum < 0:
        start += 1 # end를 감소
    else:
        end -= 1
    
print(a, b)
    
           
    