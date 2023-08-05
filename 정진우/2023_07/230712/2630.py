import sys
from collections import deque
sys.setrecursionlimit(10000)

N = int(input())
arr = []
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    arr.append(li)
    
dq = deque()
count = 0
def calc(blue, red):
    global count 
    count += 1
    if blue == 4 and red == 0:
        blue = 1
    elif red == 4 and blue == 0:
        red = 1
    dq.appendleft((blue, red))
    if count == 4:
        blue_sum = 0
        red_sum = 0
        while count:
            blue, red = dq.popleft()
            blue_sum += blue
            red_sum += red
            count = count - 1
        if blue_sum == 4 and red_sum == 0:
            blue_sum = 1
        elif blue_sum == 0 and red_sum == 4:
            red_sum = 1
        print(blue_sum, red_sum)
        dq.append((blue_sum, red_sum))
        count = 0
        
def calc2():
    while(dq):
        blue_sum = 0
        red_sum = 0
        if len(dq) >= 4:
            for _ in range(4):
                blue, red = dq.popleft()
                blue_sum += blue
                red_sum += red
            if blue_sum == 4 and red_sum == 0:
                blue_sum = 1
            elif blue_sum == 0 and red_sum == 4:
                red_sum = 1
            dq.append((blue_sum, red_sum))
            
        else:
            blue_sum, red_sum = dq.pop()
            dq.clear()
    return blue_sum, red_sum
            
    
def function1(start_pt_x, start_pt_y, k):
    if k==1:
        sum = 0
        sum += arr[start_pt_x][start_pt_y]
        sum += arr[start_pt_x][start_pt_y+1]
        sum += arr[start_pt_x+1][start_pt_y]
        sum += arr[start_pt_x+1][start_pt_y+1]
        print(sum, 4-sum, start_pt_x, start_pt_y)
        calc(sum, 4-sum)
    elif k == 2:
        function1(0, 0, k//2)
        function1(start_pt_x//2+ k //2, 0, k//2)
        function1(0, start_pt_y//2+ k//2, k//2)
        function1(start_pt_x//2+ k//2, start_pt_y//2+ k//2, k//2)
    else:
        function1(0, 0, k//2)
        function1(start_pt_x//2, 0, k//2)
        function1(0, start_pt_y//2, k//2)
        function1(start_pt_x//2, start_pt_y//2, k//2)
        
function1(N,N,N)
blue, red = calc2()
print(red)
print(blue)

        
    