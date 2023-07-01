T = int(input())

for _ in range(T):
    p = str(input())
    n = int(input())
    arr = str(input())
    arr = list(arr.replace("[", "").replace("]", "").split(","))
    
    mask = [1] * n
    pointer = 0
    first_pointer = 0
    last_pointer = n-1
    reverse = False
    error = False
    for i in p:
        if i == 'R':
            reverse = not reverse
            pointer = last_pointer if reverse else first_pointer
        if i == 'D':
            if not len(mask):
                print("error")
                error= True
                break
            if mask[pointer] == 0 :
                print("error")
                error = True
                break
            mask[pointer] = 0
            if not reverse: #  순방향
                pointer = pointer + 1 if pointer + 1 <= n-1 else pointer
                first_pointer = pointer 
            if reverse: # 역방향
                pointer = pointer - 1 if pointer - 1 >= 0 else pointer
                last_pointer = pointer
    
    
    print_arr = list()
    
    if not reverse:
        for idx, i in enumerate(mask):
            if i == 1:
                print_arr.append(int(arr[idx]))
                
                
    if reverse:
        for idx in range(len(mask)-1, -1, -1):
            if mask[idx] == 1:
                print_arr.append(int(arr[idx]))
                
    if not error:
        print("[", end="")
        for idx, i in enumerate(print_arr):
            if idx != len(print_arr) -1:
                print(f'{i},', end="")
            else:
                print(i, end="")
        print("]")
    