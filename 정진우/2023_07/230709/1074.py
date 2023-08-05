N, r, c = tuple(map(int, input().split()))

r_list = []
c_list = []

total = 0
while(r):
    r_list.append(r % 2) 
    r = r // 2
    
while(c):
    c_list.append(c % 2)
    c = c // 2

for i in range(len(r_list)):
    if r_list[i] == 1:
        total += 2 * ( 4 ** i)
    
for i in range(len(c_list)):
    if c_list[i] == 1:
        total += 4 ** i
    
print(total)
    

