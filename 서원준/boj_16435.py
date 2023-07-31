n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(len(lst)):
    if m>=lst[i]:
        m+=1

print(m)

