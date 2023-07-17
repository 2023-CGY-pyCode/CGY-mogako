N, M = tuple(map(int, input().split()))

known_list = [0] * (N+1)
party_list = []

li = list(map(int, input().split()))
known_number = li[0]
for i in li[1:]:
    known_list[i] = 1
    
for _ in range(M):
    party = list(map(int, input().split()))
    party_list.append(party[1:])
for _ in range(1, N+1):
    for known_person_idx in range(1, N+1):
        known_person = known_list[known_person_idx]
        if known_list[known_person_idx]:
            for party in party_list:
                if known_person_idx in party:
                    for p_idx in range(len(party)):
                        known_list[party[p_idx]] = 1
                    
# print(known_list)
    
not_known_list = [i for i in range(1, len(known_list)) if known_list[i] == 0]
# print(not_known_list)
def check_not_known_list(party):
    for p in party:
        if p not in not_known_list:
            return 0
    return 1

count = 0
for party in party_list:      
    count += check_not_known_list(party)
        
print(count)
        
    

