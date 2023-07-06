import sys
A, B = sys.stdin.readline().split( )

dif = len(B) - len(A) + 1 # B와 A의 길이 차 + 1
loc = [] # 각각의 count를 저장할 배열 생성

for i in range(dif):
    count = 0
    for j in range(len(A)):            
        if(A[j] == B[j + i]): #A와 B값을 비교하여 같으면 +1
            count += 1
    loc.append(count)

print(len(A) - max(loc)) # A의 길이에서 loc의 max값을 빼준다.
