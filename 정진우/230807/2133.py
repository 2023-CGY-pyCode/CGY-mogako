N = int(input())

li = [1, 0, 3]
for i in range(3, 31):
    if i % 2 == 0:
        result = 0
        result += li[i-2] * 3 # 왼쪽만 처리
        for j in range(i-4, 0, -2): # 오른쪽 특수 처리
            result += 2 * li[j] 
            # print(result)
        li.append(result+2)
    else:
        li.append(0)
    
    # if i % 2 == 0:
    #     result = 0
    # else:
    #     li.append(0)
    
# print(li)
print(li[N])