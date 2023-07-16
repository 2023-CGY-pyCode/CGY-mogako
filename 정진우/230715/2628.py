c, r = tuple(map(int, input().split()))

m = int(input())

horizontal = []
vertical = []
for _ in range(m):
    a, b = tuple(map(int, input().split())) 
    
    if a == 1:
        vertical.append(b)
    elif a == 0:
        horizontal.append(b)
        

horizontal.append(0)
vertical.append(0)
vertical.sort()
horizontal.sort()

result = 0
for i in horizontal:
    for j in vertical:
        max(result, max(i*j, (r-i, c-j)))
        
print(result)

