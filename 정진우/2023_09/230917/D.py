N = int(input())

arr = [1] * (5000)
arr[1] = 0
def function(): # 에라토스테네스의 체
    for i in range(2, int(N**0.5)+1):
        if arr[i] == 0:
            continue
        for j in range(2*i, N+1, i):
            arr[j] = 0
            
function()  

# arr이 0이면 소수가 아닌거 1이면 소수
checked = [0 for _ in range(N+1)]
def select_number(number, N):
    for i in range(1, N+1): # 소수가 아닌게 있으면
        if arr[i] == 0 and not checked[i]:
            checked[i] = 1 # check
            return i
        
    for i in range(1, N+1):
        if not checked[i] and arr[i+number] == 0:
            checked[i] = 1
            return i
        
    return 0
        
track = []
number = select_number(0, N)
while True:
    i = select_number(number, N)
    if i == 0:
        print("NO")
        break
    else:
        number += i
        track.append(i)

print("YES")
print(track)
    
    