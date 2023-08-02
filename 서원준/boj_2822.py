lst = []
ans = []
for _ in range(8):
    t = int(input())
    lst.append(t)
    ans.append(t)

ans.sort()
ans = ans[3:]

print(sum(ans))

for i in range(len(lst)):
    for a in ans:
        if lst[i]==a:
            print(i+1,end=' ')
