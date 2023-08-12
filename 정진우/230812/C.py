def score(level):
    if level >= 250:
        return 5
    if level >= 200:
        return 4
    if level >= 140:
        return 3
    if level >= 100:
        return 2
    if level >= 60:
        return 1
    else:
        return 0

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
    

li.sort(reverse=True)

levels, scores = 0 , 0 
for i in li[:42]:
    levels += i
    scores += score(i)
    
print(levels, scores)