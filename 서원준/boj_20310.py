n = input()

cnt0 = 0
cnt1 = 0
lst = [True] * len(n)

for i in range(len(n)):
    if n[i]=="0":
        cnt0 += 1
    else:
        cnt1 += 1

cnt0 /=2
cnt1 /=2


for i in range(len(n)):
    if n[i]=="1" and cnt1>0:
        lst[i] = False
        cnt1 -= 1
    if n[len(n)-i-1]=="0" and cnt0>0:
        lst[len(n)-i-1] = False
        cnt0 -= 1

# print(lst)
ans = ""
for i in range(len(n)):
    if lst[i]:
        ans += n[i]

print(ans)

