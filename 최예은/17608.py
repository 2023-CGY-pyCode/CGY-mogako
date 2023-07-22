import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    stack.append(int(sys.stdin.readline()))
    
count = 0
max = 0
for x in reversed(stack):
    if max < x:
        max = x
        count += 1
        
print(count)