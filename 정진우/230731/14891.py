from collections import deque

four_t = []

for i in range(4):
    state = deque([int(i) for i in input()])
    four_t.append(state)

def rotate(s, d):
    # print(four_t[s], d)
    if d == -1:
        number = four_t[s].popleft()
        four_t[s].append(number)
    elif d == 1:
        number = four_t[s].pop()
        four_t[s].appendleft(number)
        
    # print(four_t[s], d)
    
def process(s, d):
    if not checked[s]:  
        checked[s] = True
        # print(s)
    else:
        # print("return")
        return
    
    if s == 0:
        if four_t[s+1][6] != four_t[s][2]:
            process(s+1, -d) # 반대
    elif s == 1 or s == 2:
        if four_t[s+1][6] != four_t[s][2]:
            process(s+1, -d)
        if four_t[s-1][2] != four_t[s][6]:
            process(s-1, -d)
    elif s == 3:
        if four_t[s-1][2] != four_t[s][6]:    
            process(s-1, -d)
    
    # print("rotate ", s, d)        
    rotate(s, d)
        
N = int(input())
checked = [False] * 4
for i in range(N):
    s,d = tuple(map(int, input().split()))
    checked = [False] * 4
    # print(four_t)
    process(s-1,d)
    # print("process", i, "종료")
    
result = 0
for i in range(len(four_t)):
    if four_t[i].popleft() == 1:
        result += 2 ** (i)
        
print(result)
    

    
    