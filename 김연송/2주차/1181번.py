import sys
N = int(sys.stdin.readline()) # 단어 수 입력
a = [sys.stdin.readline() for _ in range(N)] # 문자열 입력

a = list(set(a)) # set을 사용하여 중복 제거
a.sort() # 1차 : 사전순 정렬
a.sort(key = len) # 2차 : 길이순 정렬


for i in range(len(a)):
    print(a[i], end = '')
