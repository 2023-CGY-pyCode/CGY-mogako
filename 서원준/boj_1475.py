n = input()

lst = [i for i in range(10)]
cnt = [0]*10


for i in range(len(n)):
    cnt[int(n[i])] += 1

tmp = (cnt[6] + cnt[9]+1)//2
cnt[6] = tmp
cnt[9] = tmp


print(max(cnt))
