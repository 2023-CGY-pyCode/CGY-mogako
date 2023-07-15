import sys

N, L = map(int, sys.stdin.readline().split()) # 과일 수 & 초기 길이

x = list(map(int, sys.stdin.readline().split())) # 과일들

while L >= min(x): # 배열 중 가장 작은 값보다 작으면 탈출
    L += 1
    x.remove(min(x)) # 먹어서 삭제
    if len(x) == 0: # 배열 값 없으면 종료
        break
    
print(L)
