from itertools import combinations

def gauss(term):
    point1, point2, point3 = term
    x1,y1 = point1
    x2,y2 = point2
    x3,y3 = point3
    result =  0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
    return result
    
N = int(input())
li = []

for _ in range(N):
    t = tuple(map(int, input().split()))
    li.append(t)
    

a = list(combinations(li, 3))

print(a)
max_value = 0
for i in a:
    # print(i)
    max_value = max(gauss(i), max_value)
    
print(max_value)
    
    

    
