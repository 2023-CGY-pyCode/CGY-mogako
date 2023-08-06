li = [0] * 10
for i in range(5):
    a = int(input())
    li[a] += 1
    
for i in range(len(li)):
    li[i] %= 2
    
for i in range(len(li)):
    if li[i] == 1:
        print(i)

    
