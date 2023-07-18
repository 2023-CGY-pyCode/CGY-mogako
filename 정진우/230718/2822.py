li = []
for i in range(1, 9):
    a = int(input())
    li.append((a, i))
    
li.sort(key=lambda x:x[0], reverse=True)

li = li[:5]
li.sort(key=lambda x:x[1])

result = 0
for i in li:
    x, y = i
    result += x
    
print(result)

for i in li:
    x, y = i
    print(y, end=" ")


