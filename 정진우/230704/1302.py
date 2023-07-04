N = int(input())

book_dict = dict()

for _ in range(N):
    book = input()
    if book_dict.get(book) == None:
        book_dict[book] = 1
    else:
        book_dict[book] += 1

max_v = 0
answer_tuple = ()
for k, v in book_dict.items():
    if v > max_v:
        answer_tuple = (k, v)
        max_v = v
    elif v == max_v and max_v != 0:
        if k <= answer_tuple[0]:
            answer_tuple = (k, v)
        else:
            pass
        
print(answer_tuple[0])