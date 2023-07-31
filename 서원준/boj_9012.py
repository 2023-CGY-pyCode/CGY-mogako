import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    s = deque()
    n = input()
    flag = True
    
    for i in range(len(n)):
        if n[i]=='(':
            s.append('(')
        else: # ')'
            if len(s)==0:
                flag=False
                break
            else:
                s.pop()
    
    if len(s)!=0:
        flag=False
    
    if flag==True:
        print("YES")
    else:
        print("NO")
