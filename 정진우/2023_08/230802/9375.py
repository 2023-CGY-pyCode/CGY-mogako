from itertools import combinations

T = int(input())

for i in range(T):
    n = int(input())
    
    clothes = dict()
    for j in range(n):
        cloth, types = input().split()
        try:
            clothes[types].append(cloth)
        except KeyError:
            clothes[types] = []
            clothes[types].append(cloth)
            
        
    result = 0
    
    li = []
    for k, v in clothes.items():
        li.append(len(v))
        
    
    # for i in range(1, len(li)+1): # 1, 2, 3, 4/·/
    for count in li:
        result += len(list(combinations(range(count), 1)))
        print(list(combinations(range(count), i)))
            
    print(result)
        