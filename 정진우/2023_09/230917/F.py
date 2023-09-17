import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())

li = []
for _ in range(N):
    p, q = map(int, input().split())
    li.append((p, q, p-q))

# p-q기준 오름차순 정렬
li.sort(key=lambda x:(x[2]))


min_a = 0
for p, q, d in li[:A]:
    min_a += p
for p, q, d in li[A:]:
    min_a += q
    
print(min_a)
    
    
# li.sort(key=lambda x:(x[1], -x[0]))
# min_b = 0
# for p, q in li[:B]:
#     min_b += q
# for p, q in li[B:]:
#     min_b += p
    
# # print(min_b)
# print(min(min_a, min_b))