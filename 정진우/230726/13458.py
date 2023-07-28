import sys
input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))

B,C = tuple(map(int, input().split()))


count = 0

for r in range(len(li)):
    li[r] = li[r] - B
    count += 1
    
    
for r in li:
    if r <= 0:
        continue
    if C >= r:
        count += 1
        continue
    if r%C == 0: 
        count += r//C
    else:
        count += r//C + 1
        
        

print(count)
        
    




