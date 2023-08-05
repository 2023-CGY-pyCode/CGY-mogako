N = int(input())

arr = [1] * (N+1)
arr[1] = 0
def function(): # 에라토스테네스의 체
    for i in range(2, int(N**0.5)+1):
        if arr[i] == 0:
            continue
        for j in range(2*i, N+1, i):
            arr[j] = 0
function()            
# print(arr)
prime_list = [i for i in range(2, len(arr)) if arr[i] == 1 ] # O(n)
# print(prime_list)
first_pointer = 0
end_pointer = 1
count = 0 if arr[N] != 1 else 1
while True:
    target = sum(prime_list[first_pointer:end_pointer+1])
    if first_pointer == end_pointer or N <= 4:
        break
    if  target < N:
        end_pointer +=1
    elif target > N:
        first_pointer += 1
    else:
        count+=1
        first_pointer +=1
        end_pointer += 1
     
print(count)
        
    
    
        