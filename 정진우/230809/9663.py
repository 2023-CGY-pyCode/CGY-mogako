
import sys
N = int(sys.stdin.readline().rstrip())
output = sys.stdout.write
# N*N으로 초기화

ans = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
         
    return True
    

def n_queens(x):
    global ans
    if x == N:
        ans += 1
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
                
n_queens(0)
print(str(ans))