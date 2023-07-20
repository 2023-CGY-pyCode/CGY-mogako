import sys
from collections import deque

N = int(sys.stdin.readline()) # 막대기 개수
stack = deque()

for i in range(N):
    stack.append(int(sys.stdin.readline())) # 막대기를 스택에 추가

x = stack.pop() # 제일 앞에 있는 값을 x에 저장

num = 1; # 보이는 막대기의 수

for i in range(N - 1):
    y = stack.pop() # 앞에 있는 막대기보다 크면 num + 1
    if x < y:
        x = y
        num += 1
print(num)
