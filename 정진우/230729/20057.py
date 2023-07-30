import sys
input = sys.stdin.readline

arr = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
out = 0
N = int(input())

for _ in range(N):
    li = list(map(int, input().split()))
    
    arr.append(li)
    
# 회오리 진행방향

def get_tornado_directions():
    directions = [2,1,0,3]
    count = 0
    idx = 1
    target_directions = []
    while count != N**2 - 1:
        for d in range(len(directions)):
            if d == 0 or d == 1:
                for _ in range(idx):
                    target_directions.append(directions[d])
                    count+=1    
                    if count == N**2 -1:
                        return target_directions
            else:
                for _ in range(idx+1):
                    target_directions.append(directions[d])
                    count+=1
                    if count == N**2 -1:
                        return target_directions
        idx+=2            

# 회오리 프로세스 
def get_dd(left, right, straight):
    dd_list = []
    dd_list.append((dy[left]+dy[left], dx[left]+dx[left], 2))
    dd_list.append((dy[right]+dy[right], dx[right]+dx[right], 2))
    dd_list.append((dy[left], dx[left], 7))
    dd_list.append((dy[right], dx[right], 7))
    dd_list.append((dy[left]+dy[straight], dx[left]+dx[straight], 10))
    dd_list.append((dy[right]+dy[straight], dx[right]+dx[straight], 10))
    dd_list.append((dy[straight]+dy[straight], dx[straight]+dx[straight], 5))
    dd_list.append((dy[left]-dy[straight], dx[left]-dx[straight], 1))
    dd_list.append((dy[right]-dy[straight], dx[right]-dx[straight], 1))
    
    return dd_list

def tornado_process(y, x, value, d):
    global out 
    left = d-1 if d-1 >= 0 else 3
    right = d+1 if d+1 <= 3 else 0
    dd_list = get_dd(left, right, d)
    result = 0
    for ddy, ddx, p in dd_list:
        r = value*p // 100
        
        if y+ddy >= 0 and y+ddy < N and x+ddx >= 0 and x+ddx < N:
            arr[y+ddy][x+ddx] += r
        else:
            out += r
        result += r
    
    if y+dy[d] >= 0 and y+dy[d] < N and x+dx[d] >= 0 and x+dx[d] < N:
        arr[y+dy[d]][x+dx[d]] += value-result # 남은거 저장
    else:
        out += value-result
        
    arr[y][x] = 0
    
    
def tornado(y, x, d):
    next_y, next_x = y+dy[d], x+dx[d]
    value = arr[next_y][next_x]
    tornado_process(next_y, next_x, value, d)
    return next_y, next_x
    
# 시작 회오리는 정가운데 N은 홀수. 
target_directions = get_tornado_directions()
target_y, target_x = N//2, N//2

for direction in target_directions:
    target_y, target_x = tornado(target_y, target_x, direction)

print(out)


