import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
input_li = list(map(int, input().split()))
operator_li = list(map(int, input().split()))

def check(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -1 * (-1 * num1 // num2)
        else:
            return num1 // num2
# max = 0
# min = 10000

def recursion(li, result, operator_li):
    if li:
        num2 = li.pop(0)
        for idx in range(len(operator_li)):
            if operator_li[idx] >= 1:
                result = check(result, num2, idx)
                # print(f'idx: {idx} 제거')
                operator_li[idx] -= 1
                recursion(li, result, operator_li)
                operator_li[idx] += 1
    if not li:
        print(result)
        return

for j in range(len(operator_li)):
    for p in range(4):
        i = j+p // 4
        temp_list = [o for o in input_li]
        print(temp_list)
        print(operator_li)
        result = temp_list.pop(0)
        recursion(temp_list, result, operator_li)
    
            
