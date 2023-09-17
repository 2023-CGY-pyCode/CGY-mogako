N = int(input())

original = list(map(int, input().split()))
target = list(map(int, input().split()))


minus = 0
plus = 0
for x, y in zip(original, target):
    if x - y < 0 :
        minus += x - y
    else:
        plus += x - y
        
if minus == -plus:
    print(plus)

        
    
