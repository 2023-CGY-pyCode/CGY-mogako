import sys
from collections import deque

N = int(sys.stdin.readline()) # 카드의 수

queue = deque()

for i in range(1, N + 1): # 1부터 N까지 카드
    queue.append(i)

for i in range(N - 1): # 첫번째 값을 빼고 다음 값을 끝에 더한다
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue.pop()) # 마지막으로 남은 값 출력
