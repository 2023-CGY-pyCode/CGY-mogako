N = input()

plastic_set = [0] * 10 # 0~9
for i in N:
    plastic_set[int(i)] += 1

plastic_set[9] = round((plastic_set[9] + plastic_set[6] + 0.001) / 2)
plastic_set[6] = 0

print(max(plastic_set))
