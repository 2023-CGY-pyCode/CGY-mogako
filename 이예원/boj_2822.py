import sys

score_list = []
for i in range(8):
    score = int(sys.stdin.readline())
    score_list.append([score, i+1])

score_list.sort(reverse=True)
result_score = 0
result_number = []
for i in range(5):
    result_score += score_list[i][0]
    result_number.append(score_list[i][1])

print(result_score)
result_number.sort()
for n in result_number:
    print(n, end=' ')