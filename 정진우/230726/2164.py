from collections import deque
# import sys
# input = sys.stdin.readline

dq = deque()
N = int(input())

for i in range(1, N+1):
    dq.append(i)
    
if len(dq) == 1:
    print(dq.pop())

while dq:
    _ = dq.popleft()
    number = dq.popleft()
    if dq:
        dq.append(number)
    else:
        print(number)
    

# dq1 = deque()
# dq2 = deque()

# N = int(input())

# for i in range(N, 0, -1):
#     dq1.append(i)

# while dq1 or dq2:
#     # print(dq1)
#     if len(dq1) == 1:
#         print(dq1.pop())
#         break
        
#     _ = dq1.pop()
#     num = dq1.pop()
#     while dq1:
#         number = dq1.pop()
#         dq2.append(number)
        
#     dq2.append(num)
#     while dq2:
#         number = dq2.pop()
#         dq1.append(number)

    
            
    
    
    