t = int(input())

for _ in range(t):
    a = input()
    ans=0
    b=0
    for i in range(len(a)):
        if a[i]=='O':
            b+=1
            ans += b
        else:
            b=0
    print(ans)
