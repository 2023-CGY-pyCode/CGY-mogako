curr = input()
y,m,s = map(int, curr.split('-'))

N = int(input())

count = 0
for _ in range(N):
    dy, dm, ds = map(int, input().split('-'))
    if dy < y:
        continue
    if dm < m and dy == y:
        continue
    if ds < s and dy == y and dm == m :
        continue
    
    count += 1
    
print(count)