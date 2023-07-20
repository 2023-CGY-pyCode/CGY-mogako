import sys
from collections import deque

N = int(sys.stdin.readline()) # 전체 케이스의 수
A = []
x = 1
stack = deque()

for i in range(N):
    A = list(sys.stdin.readline().split())
    
    for j in range(len(A)): # 배열에 저장된 문자의 수만큼 스택에 따로 저장
        stack.append(A[j])
        
    print("Case #{0}:".format(x), end = ' ') 
    x += 1
    
    for j in range(len(A)): # stack.pop()를 사용하여 순서대로 출력
        print(stack.pop(), end = ' ')
    print()

# 1.각 입력 문자열을 띄어쓰기에 따라 나누어 배열에 저장하기
# 2.스택에 각 배열을 저장하기
# 3.스택에 저장된 값을 pop하여 출력하기
