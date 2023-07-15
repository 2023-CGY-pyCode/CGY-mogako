import sys

N, L = map(int, sys.stdin.readline().split()) #과일 수, 초기 길이

a = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in range(len(a)): # 과일 수만큼 반복
    if L >= a[i]:
        L += 1

print(L)
