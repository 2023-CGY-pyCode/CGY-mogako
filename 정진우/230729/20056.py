import sys
input = sys.stdin.readline

N,M,K = tuple(map(int, input().split()))


# Input
arr = [[ [] for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    r,c,m,s,d = tuple(map(int, input().split()))
    arr[r][c].append((m,s,d))

# print(arr)
# fireball move
def get_target_xy(r, c, s, d):
    target_r, target_c = 0, 0
    control = s%N
    if d == 7 or d == 6 or d == 5:
        target_c = c-control 
        if target_c <= 0:
            target_c = N + target_c
    elif d == 1 or d == 2 or d == 3:
        target_c = c+control
        if target_c >= N+1:
            target_c = (c+control)%N
    else:
        target_c = c
        
    if d == 5 or d == 4 or d == 3:
        target_r = r+control
        if target_r >= N+1:
            target_r = (r+control)%N
    elif d == 7 or d == 0 or d == 1:
        target_r = r-control
        if target_r <= 0:
            target_r = N + target_r
    else:
        target_r = r 
        
    # print(r,c,s,d,"-> ",target_r,target_c)
    return target_r, target_c

def spreading(m_list, s_list, d_list):
    all_m = sum(m_list)//5
    all_s = sum(s_list)//len(m_list)
    all_d = [0, 2, 4, 6]
    
    odd = 0
    even = 0
    for r_d in d_list:
        if r_d % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0 or even == 0:
        all_d = [0, 2, 4, 6]  # 0 2 4 6
    else:
        all_d = [1, 3, 5, 7]  # 1 3 5 7
    
    return all_m, all_s, all_d
    
for _ in range(K):
    pending_list = [[ [] for _ in range(N+1)] for _ in range(N+1)]
    for r in range(1, N+1): # 1234 if N == 4
        for c in range(1, N+1):
            if len(arr[r][c]) >= 1: # 파이어볼이 하나라도 있을 경우
                for fireball in arr[r][c]:
                    m,s,d = fireball # 
                    target_r, target_c = get_target_xy(r,c,s,d)
                    pending_list[target_r][target_c].append((m,s,d)) # fireball이 이동
                # print(target_r, target_c)
    # 이동후 확산
    arr = [[ [] for _ in range(N+1)] for _ in range(N+1)] # 초기화
    # print(pending_list)
    for r in range(1, N+1): # 1234 if N == 4
        for c in range(1, N+1):
            # print(r, c, pending_list[r][c])
            if len(pending_list[r][c]) >= 2: # 합쳐지는 경우에만
                # print("합쳐지는경우")
                m_list, s_list, d_list = [], [], []
                for fireball in pending_list[r][c]:
                    m,s,d = fireball
                    m_list.append(m)
                    s_list.append(s)
                    d_list.append(d)
                
                all_m, all_s, all_d = spreading(m_list, s_list, d_list)
                # print(all_m, all_s, all_d)
                for d in all_d:
                    if all_m == 0: # 소멸
                        break
                    else:
                        arr[r][c].append((all_m, all_s, d)) # 방향에따른 4가지 파이어볼 추가
            elif len(pending_list[r][c]) == 1:
                fireball = pending_list[r][c][0]
                m,s,d = fireball
                arr[r][c].append((m,s,d))
            # elif len(pending_list[r][c]) == 1:
            #     fireball = pending_list[r][c][0]
            #     m,s,d = fireball
            #     arr[r][c]
                        
                        

# 남아있는 파이어볼 합 출력
fireball_sum = 0
for r in range(1, N+1): 
    for c in range(1, N+1):
        for fireball in arr[r][c]:
            m, _, _ = fireball
            fireball_sum += m
            
print(fireball_sum)
            
                
                
                

                
                