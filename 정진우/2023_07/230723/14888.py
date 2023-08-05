import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
input_li = list(map(int, input().split()))
operator_li = list(map(int, input().split()))

st = []
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

def recursion(li, result, j):
    if li:
        num2 = li.pop(0)
        result2 = check(result, num2, j)
        
        # print(result2)
        # print(f'idx: {idx} 제거')
        
        print(li, result2, operator_li)
        if not li:
            st.append(result2)
            return
        for i in range(len(operator_li)):
            if operator_li[i] >= 1:
                operator_li[i] -= 1
                recursion(li, result2, i)
                operator_li[i] += 1
                
    # if not li:
    #     print(result)
    #     st.append(result)
    #     return

for j in range(len(operator_li)):
    temp_list = [o for o in input_li]
    result = temp_list.pop(0)
    # print(temp_list, result, operator_li)
    if operator_li[j] >= 1:
        operator_li[j] -= 1
        recursion(temp_list, result, j)
        operator_li[j] += 1
    
print(st)
            
