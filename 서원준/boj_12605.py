from collections import deque

n = int(input())


for i in range(n):
    lst = input().split()
    s = deque()
    for j in range(len(lst)):
        s.append(lst[j])
    
    print(f"Case #%d:"%(i+1), end=' ')
    for j in range(len(s)):
        print(s.pop(), end=' ')

