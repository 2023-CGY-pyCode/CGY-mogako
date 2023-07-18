import sys

n = int(sys.stdin.readline())

word_list = []
check_repeat = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in check_repeat:
        word_list.append([len(word), word])
        check_repeat.append(word)

word_list.sort()
for _, word in word_list:
    print(word)


