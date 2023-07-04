word = input()

while word:
    print(word[:10])
    if len(word) >= 10:
        word = word[10:]
    else:
        word = []