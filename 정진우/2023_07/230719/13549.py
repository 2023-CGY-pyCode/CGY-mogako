import sys
from collections import deque
sys.setrecursionlimit(10**5)

N, K = tuple(map(int, input().split()))

q = deque()
q.append((N, 0))

visited = [0] * 300002
level = 1


def bfs():
    if N < K:
            
        while q:
            state, count = q.popleft()
            print(state)
            if state < 0 or visited[state]:
                continue
            visited[state] = 1
            if state == K:
                return count
            
            
            if state < K:
                if not visited[2*state]:
                    q.appendleft((2*state, count))
            if not visited[state+1]:
                q.append((state+1, count+1))
            if not visited[state-1]:
                q.append((state-1, count+1))
    else:
        return (N-K)
        
    
print(bfs())

    
    
        
    
    

    