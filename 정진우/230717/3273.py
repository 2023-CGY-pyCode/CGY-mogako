import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
x = int(input())

li.sort()
first_pointer = 0
end_pointer = len(li)-1
count = 0
while True:
    if first_pointer >= end_pointer:
        break
    result = li[first_pointer] + li[end_pointer]
    if result > x:
        end_pointer-=1
    elif result < x:
        first_pointer+=1
    else:
        count+=1
        first_pointer+=1
        end_pointer-=1
        
print(count)
    