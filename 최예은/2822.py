score = []

for i in range(8):
    score.append(int(input()))
sorted_score = sorted(score, reverse=True)

big5 = []
for i in range(5):
    big5.append(sorted_score[i])

a = []
total = 0
for i in big5:
    total += i
    a.append(score.index(i))

print(total)

a.sort()
for i in a:
    print(i + 1, end=' ')