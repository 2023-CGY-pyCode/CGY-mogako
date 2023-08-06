import sys
input =sys.stdin.readline

N = int(input())

sticks = [0] * 100001
li = list(map(int, input().split()))
multi = [2] * 100001
multi[1] = 1
for i in li:
    sticks[i] = 1
    
def sniff():
    for i in range(2, int(100001 ** 0.5)+1):
        if multi[i] == 0:
            continue
        for j in range(i+i, 100001, i):
            multi[j] = 0
            

M = int(input())

to_sticks = list(map(int, input().split()))

def multiplier(number):
    if sticks[number] == 0:
        return 0
    return multi[number]

def cal_multiplier(to_stick):
    li = []
    if multi[to_stick] == 2:
        return 2
    for i in range(2, int(to_stick**0.5) + 1):
        if to_stick % i == 0:
            li.append(i)
            if i != to_stick // i:
                li.append(to_stick//i)
    
    result = 0
    # li.append(to_stick)
    if to_stick == 1:
        return 1
    for i in li:
        # print(i)
        result += multiplier(i)
        
    if sticks[1] != 0:
        result += 1
    if sticks[to_stick] != 0:
        result += 1
        
    return result
        
sniff()
for i in range(1, 50001):
    count = 0
    if multi[i] == 2:
        continue
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j != i // j:
                count += 1
            count+=1

    multi[i] = count
    
    
for to_stick in to_sticks:
    print(cal_multiplier(to_stick), end=" ")
    
