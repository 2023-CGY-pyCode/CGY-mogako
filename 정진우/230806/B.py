li = []
N = int(input())
for i in range(N):
    string1 = str(input().strip())
    li.append(string1)

M = int(input())    
candidate = []
for j in range(M):
    string2 = str(input().strip())
    candidate.append(string2)
    
for i in range(len(li)):

    if len(li) == 1:
        print(candidate[0])
        break
    if li[i] == '?':
        if i == 0:
            start_char = li[i+1][0]
            for j in candidate:
                if j.endswith(start_char):
                    if j not in li:
                        print(j)
        elif i == len(li)-1:
            end_char = li[i-1][-1]
            for j in candidate:
                if j.startswith(end_char):
                    if j not in li:
                        print(j)               
        else:
            end_char = li[i-1][-1]
            start_char = li[i+1][0]
            for j in candidate:
                if j.startswith(end_char) and j.endswith(start_char):
                    if j not in li:
                        print(j)   
        

    



