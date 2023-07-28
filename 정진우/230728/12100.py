import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())

def process(arr, direction): # 0123 동남서북
    
    pending_list = []
    if direction <= 0:
        
        for i in range(N):
            temp_list = deque()
            for j in range(N):
                if arr[i][j] == 0:
                    temp_list.appendleft(0)
                else:
                    temp_list.append(arr[i][j])
            arr[i] = copy.deepcopy(list(temp_list))
                    
        for i in range(N):
            j = N-1
            while j >= 0:
                if arr[i][j] == 0:
                    j = j-1
                    continue
                if j-1 < 0:
                    pending_list.append(arr[i][j])
                else:
                    if arr[i][j] == arr[i][j-1]:
                        pending_list.append(2*arr[i][j])
                        j = j-1 # 계산됬기 때문에 건너뜀
                    else:
                        pending_list.append(arr[i][j])
                j = j-1
            while len(pending_list) != N:
                pending_list.append(0)
            pending_list = pending_list[::-1]
            arr[i] = pending_list
            pending_list = []
        return arr
    elif direction == 1:
        for j in range(N): # 0 처리
            temp_list = deque()
            for i in range(N):
                if arr[i][j] == 0:
                    temp_list.appendleft(0)
                else:
                    temp_list.append(arr[i][j])
            temp_list = list(temp_list)
            for temp in range(len(temp_list)): # 남쪽이라 순방향 0
                arr[temp][j] = temp_list[temp]
        for j in range(N):
            i = N-1
            while i >= 0:
            
                if arr[i][j] == 0:
                    
                    i = i-1
                    continue
                
                if i-1 < 0:
                    pending_list.append(arr[i][j])
                else:
                    if arr[i][j] == arr[i-1][j]:
                        pending_list.append(2*arr[i][j])
                        i = i-1 # 계산됬기 때문에 건너뜀
                    else:
                        pending_list.append(arr[i][j])
                i = i-1
            while len(pending_list) != N:
                pending_list.append(0)
            
            pending_list = pending_list[::-1]            
            for pend in range(len(pending_list)):
                arr[pend][j] = pending_list[pend]
                    
            
            pending_list = []
            
        return arr

    if direction == 2:
        for i in range(N):
            temp_list = deque()
            for j in range(N-1, -1, -1):
                if arr[i][j] == 0:
                    temp_list.append(0)
                else:
                    temp_list.appendleft(arr[i][j])
            arr[i] = copy.deepcopy(list(temp_list))
        # print(arr)
        for i in range(N):
            j = 0
            while j <= N-1:
                if arr[i][j] == 0:
                    j = j + 1
                    continue 
                if j+1 > N-1:
                    pending_list.append(arr[i][j])
                else:
                    if arr[i][j] == arr[i][j+1]:
                        pending_list.append(2*arr[i][j])
                        j = j+1 # 계산됬기 때문에 건너뜀
                    else:
                        pending_list.append(arr[i][j])
                j = j+1
            while len(pending_list) != N:
                pending_list.append(0)
            # pending_list = pending_list[::-1]
            arr[i] = pending_list
            pending_list = []
        return arr

    elif direction == 3:
        for j in range(N): # 0 처리
            temp_list = deque()
            for i in range(N-1, -1, -1):
                if arr[i][j] == 0:
                    temp_list.append(0)
                else:
                    temp_list.appendleft(arr[i][j])
                
            temp_list = list(temp_list)
            for temp in range(len(temp_list)): # 북쪽이라 역방향 0
                arr[temp][j] = temp_list[temp]
                
        for j in range(N):
            i = 0
            while i <= N-1: 
                if arr[i][j] == 0:
                    i = i + 1
                    continue     
                if i+1 > N-1:
                    pending_list.append(arr[i][j])
                else:
                    if arr[i][j] == arr[i+1][j]:
                        pending_list.append(2*arr[i][j])
                        i = i+1 # 계산됬기 때문에 건너뜀
                    else:
                        pending_list.append(arr[i][j])
                i = i+1
            while len(pending_list) != N:
                pending_list.append(0)
            pending_list = pending_list            
            for pend in range(len(pending_list)):
                arr[pend][j] = pending_list[pend]
            
            pending_list = []
        return arr
                
        
max_value = 0
# arr_copy = []

max_list = []
def backtracking(p, K):
    t = copy.deepcopy(p)
    global max_value
    # arr_copy = copy.deepcopy(arr)
    if K == 0:
        max_list.append(max(list(map(max, t))))
        return 
    
    for i in range(4): # 상하좌우
        l = copy.deepcopy(t)
        arr_copy = copy.deepcopy(process(t, i))
        t = copy.deepcopy(l)
        max_list.append(max(list(map(max, arr_copy))))
        backtracking(arr_copy, K-1)
    
    # print(K)
    
    # print(max_value)
    max_list.append(max(list(map(max, t))))
    # print(t, K)
    return
            
def main():    
    
    arr = []
    for _ in range(N):
        li = list(map(int, input().split()))
        arr.append(li)
        
    
    # print(arr)
    p = copy.deepcopy(arr)
    backtracking(p, 5)
    print(max(max_list))
    # print(arr)
        
    # print(max_value)
    
    # arr = process(arr, 2)
    # arr = process(arr, 3)
    # arr = process(arr, 2)
    # arr = process(arr, 1)
    # arr = process(arr, 0)    
      
    # print(arr)
    # arr = process(arr, 3)
    # print(arr)
    
main()


    


 