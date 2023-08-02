import sys

num = sys.stdin.readline().rstrip()
plastic = [0] * 10

for n in num:
    plastic[int(n)] += 1

mid = round((plastic[6] + plastic[9]) / 2 + 0.00001)

plastic[6], plastic[9] = mid, mid

print(max(plastic))