import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

    
min_v, max_v = 0, 0
priority_queue = list()

def swap(a,b):
    temp = priority_queue[a]
    priority_queue[a] = priority_queue[b]
    priority_queue[b] = temp
    print("swap", priority_queue)
def balance(idx, reverse=False):
    swap(idx, 0)
    idx = 0
    
    parent = (idx-1) // 2 
    child_1 = parent * 2 + 1
    child_2 = parent * 2 + 2
    
    if len(priority_queue)-1 >= child_2:
        if priority_queue[parent] <= priority_queue[child_1] and \
            priority_queue[parent] <= priority_queue[child_2]:
                if priority_queue[child_1] <= priority_queue[child_2]:
                    swap(child_1, parent)
                    return balance(parent, reverse)
                else:
                    swap(child_2, parent)
                    return balance(parent, reverse)
        elif priority_queue[parent] >= priority_queue[child_1] and \
            priority_queue[parent] >= priority_queue[child_2]:
                if priority_queue[child_1] <= priority_queue[child_2]:
                    swap(child_2, parent)
                    return balance(parent, reverse)
                else:
                    swap(child_1, parent)
                    return balance(parent, reverse)
    
    elif len(priority_queue)-1 >= child_1:
        if priority_queue[parent] > priority_queue[child_1]:
            swap(child_1, parent)
            return balance(parent, reverse)
            
    else:
        return    
        
        
for i in range(N):
    num = int(input())
    priority_queue.append(num)
    balance(i, False)
    # print(priority_queue)
    print(priority_queue[0])


    
    