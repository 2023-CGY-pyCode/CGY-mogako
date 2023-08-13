import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())
state = False

def backtracking(N, depth, result):
    global state
    if state == True:
        return
    if depth == N: # 종료 조건
        if result % 7 == 0:
            state = True
        return  
    
    op1,v1 = arr[depth][0]
    op2,v2 = arr[depth][1]
    
    backtracking(N, depth+1, eval(f"{result}{op1}{v1}"))
    backtracking(N, depth+1, eval(f"{result}{op2}{v2}"))
    
    return 

for _ in range(T):
    N = int(input())
    K = 1
    state = False
    arr = []
    for i in range(N):
        op1, v1, op2, v2 = map(str, input().split())
        arr.append([(op1, v1), (op2, v2)]) # 두개 넣음
    
    
    backtracking(N, 0, K)

    if state == True:
        print("LUCKY\n")
    else:
        print("UNLUCKY\n")
        