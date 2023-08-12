N = int(input())

def check(num):
    if num < 250:
        return 4
    if num < 275:
        return 3
    if num < 300:
        return 2
    if num == 300:
        return 1
    
arr = list(map(int, input().split()))

for i in arr:
    print(check(i), end=" ")