import sys
from collections import deque
 
X = int(sys.stdin.readline()) # 테스트 케이스 수

for i in range(X):
    N, M = map(int, sys.stdin.readline().split()) # 문서의 개수, 해당 문서가 놓인 순서

    count = 0 # 출력된 문서 개수 초기화
    
    queue = deque(list(map(int, sys.stdin.readline().split()))) # 문서의 중요도

    while(True):
        if queue[0] >= max(queue): # 가장 크면 pop으로 삭제
            count += 1
            if M == 0:
                break
            else:
                queue.popleft()
                M -= 1
        else:
            queue.append(queue.popleft()) # 가장 크지 않으면 뒤로 보내기 
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1 # 순서를 당기기
  
    print(count)
    queue.clear() # 큐 초기화
