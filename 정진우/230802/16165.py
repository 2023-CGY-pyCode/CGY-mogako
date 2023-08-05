team = dict()
member = dict()

N, M = tuple(map(int, input().split()))

for _ in range(N):
    team_name = input()
    unit_count = int(input())
    team_members = []
    for _ in range(unit_count):
        member_name = input()
        team_members.append(member_name)
        member[member_name] = team_name
        
    team[team_name] = sorted(team_members)
    
for _ in range(M):
    question = input()
    types = int(input())
    
    if types == 1:
        print(member[question])
    elif types == 0:
        for name in team[question]:
            print(name)
            
    
        
        
        
        