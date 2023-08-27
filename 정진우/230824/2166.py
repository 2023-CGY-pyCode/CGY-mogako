N = int(input())

left = []
right = []

for _ in range(N):
    x , y = map(int, input().split())
    
    left.append(x)
    right.append(y)
    
left.append(left[0]), right.append(right[0])

orth1=orth2=0
for i in range(len(left) - 1):
    orth1 += left[i] * right[i+1]
    
for i in range(len(right) - 1):
    orth2 += right[i] * left[i+1]
    
result = round(abs(orth2 - orth1) / 2, 1)
print(result )



    
