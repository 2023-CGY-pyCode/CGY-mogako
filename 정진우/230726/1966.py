from collections import deque

dq = deque()

N = int(input())

count = 0
# cur_point = 0

def check(cur_point, count):        
    # print(dq)
    critical = dq.popleft()
    
    # print(cur_point)
    for item in list(dq):
        if critical < item:
            dq.append(critical)
            if cur_point == 0:
                cur_point = len(dq)-1
            else:
                cur_point -= 1
            return check(cur_point, count)

    count += 1
    if cur_point == 0:
        return count
    else:
        return check(cur_point-1, count)
        
for i in range(N):
    N, M = tuple(map(int, input().split()))
    
    li = list(map(int, input().split()))
    dq = deque(li)
    print(check(M, 0))

    
    
    
        