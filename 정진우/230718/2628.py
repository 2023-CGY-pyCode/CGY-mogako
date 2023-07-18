x, y = tuple(map(int, input().split()))
             
n = int(input())

horizontal = [0]
vertical = [0]

for i in range(n):
    h, v = tuple(map(int, input().split()))
    if h == 0:
        horizontal.append(v)
    else:
        vertical.append(v)

horizontal.sort()    
vertical.sort()
horizontal.append(y)
vertical.append(x)

result = 0
for h_idx in range(len(horizontal)-1):
    for v_idx in range(len(vertical)-1):
        # print((horizontal[h_idx+1] - horizontal[h_idx]),(vertical[v_idx+1] - vertical[v_idx]) )
        result = max((horizontal[h_idx+1] - horizontal[h_idx]) * (vertical[v_idx+1] - vertical[v_idx]), result)
print(result)

    