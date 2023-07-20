import sys
from collections import deque

T = int(sys.stdin.readline()) # 입력 데이터 수

stack = deque()

for i in range(T):
    X = list(sys.stdin.readline())
    
    stack.clear()
    num = 0
    
    for j in range(len(X)): # 스택에 괄호 문자열 하나씩 저장
        stack.appendleft(X[j]) # 계산하기 쉽게 왼쪽부터 저장

    for j in range(len(X)):
        p = stack.pop()

        if p == '(':
            num += 1
        elif p == ')':
            num -= 1
            
        if num == -1: # 닫을 괄호가 없으면 break
            break

    if num == 0:
        print("YES")
    else:
        print("NO")
