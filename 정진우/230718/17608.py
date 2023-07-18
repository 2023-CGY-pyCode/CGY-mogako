import sys
from collections import deque
input = sys.stdin.readline



st = deque()

N = int(input())

for _ in range(N):
    num = int(input())
    st.append(num)
    
seen = 0
count = 0
while st:
    number = st.pop()
    if number > seen:
        count += 1
        seen = number
        
print(count)
        