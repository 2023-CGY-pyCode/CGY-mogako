import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
li = list(map(int, input().split()))

li = list(set(li))
# print(li)

li.sort()

range_arr = []
for i in range(1, len(li)):
    range_arr.append(li[i] - li[i-1])
    
range_arr.sort(reverse=True)
print(sum(range_arr[K-1::]))



        
        
        
    
    
    
    