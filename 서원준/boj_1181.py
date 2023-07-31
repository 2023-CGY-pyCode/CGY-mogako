

n = int(input())
s=set()
for _ in range(n):
    s.add(input())

lst=list(s)

lst.sort(key=lambda o:(len(o), o))

for i in range(len(lst)):
    print(lst[i])
