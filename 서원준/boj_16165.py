
n, m = map(int, input().split())

d = dict()
for _ in range(n):
    t_name = input()
    t_num = int(input())
    t_lst = []
    for _ in range(t_num):
        t_lst.append(input())
    t_lst.sort()
    d[t_name] = t_lst

for _ in range(m):
    a = input()
    b = int(input())

    if b==0:
        for i in d[a]:
            print(i)    # 팀 멤버
    else:
        for team, mem in d.items():
            if a in mem:
                print(team) # 팀 이름
                break



