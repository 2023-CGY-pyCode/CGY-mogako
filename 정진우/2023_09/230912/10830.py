N, B = map(int, input().split())

arr = []
for _ in range(N):
    li = list(map(int, input().split()))
    arr.append(li)
    
def matrix_mul(arr1, arr2):
    result =[[0] * N for _ in range(N)] # NxN zeros
    
    for row in range(N):
        for col in range(N):
            s = sum(arr1[row][i] * arr2[i][col] for i in range(N)) 
            result[row][col] = s % 1000
            
    return result


def power(n, arr):
    if n == 1:
        return arr # n이 1일때는 그대로 리턴
    
    if n % 2 == 0 : # n이 짝수 일때
        half = power(n//2, arr) # 반절씩 나눠서 곱셈 진행
        return matrix_mul(half, half)
    else:
        return matrix_mul(arr, power(n-1, arr)) # 홀수 일때는 짝수로 만든것과 계산
    

for row in power(B, arr):
    print(*[r % 1000 for r in row])
    