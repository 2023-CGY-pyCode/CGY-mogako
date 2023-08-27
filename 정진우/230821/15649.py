N, M = map(int, input().split())

visited = [0] * (N+1)

def recursive(number, count, arr : list):
    visited[number] = 1
    arr.append(number)
    
    if count == M:
        print(*arr)
        return 
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            recursive(i, count+1, arr)
            arr.pop(-1)
            visited[i] = 0
        
    
for i in range(1, N+1):
    visited = [0] * (N+1)
    recursive(i, 1, [])
    
    
    
