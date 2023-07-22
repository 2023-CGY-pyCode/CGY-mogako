import sys
from collections import deque
# 파이썬에는 스택 라이브러리가 없어서 덱 라이브러리로 사용

K = int(sys.stdin.readline())
stack = deque()

for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        stack.pop() # 0을 입력받으면 이전 값 삭제
    else:
        stack.append(N) # 그 외는 값 입력


print(sum(stack)) # 스택 합 출력
