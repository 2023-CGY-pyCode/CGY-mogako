A,B,C = tuple(map(int, input().split()))

def dq(number, m):
    if m == 1:
        return A % C
    else:
        tmp = dq(number, m//2)
        if m % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
        
print(dq(A, B))
    