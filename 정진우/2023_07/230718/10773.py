import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
st = deque()
for _ in range(K):
    num = int(input())
    st.append(num) if num != 0 else st.pop()
        
print(sum(st))