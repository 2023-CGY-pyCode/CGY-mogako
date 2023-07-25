N = int(input())

cur_number = 1
for i in range(1, N+1):
    multiply = (i%10000) if i % 10000 else int(str(i)[0])
    cur_number = str(cur_number * multiply)
    for i in cur_number[::-1]:
        if i != '0':
            cur_number = int(i)
            break
    # print(cur_number)
        
print(cur_number)
        