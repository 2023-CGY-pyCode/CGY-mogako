n = input()

while len(n)>10:
    print(n[:10])
    n = n[10:]
print(n)