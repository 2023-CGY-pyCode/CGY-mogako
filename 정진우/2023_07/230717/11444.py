import sys
sys.setrecursionlimit(10**6)
n = int(input())

MODE = 1000000007
fibo_dict = {0: 0, 1: 1}

def fibo(n):
    if n not in fibo_dict:
        if n % 2 == 0:
            a = n // 2
            b = n // 2 - 1
            fibo_dict[n] = (fibo(a) * (fibo(a) + 2*fibo(b))) % MODE
        else:
            a = n // 2 + 1
            b = n // 2
            fibo_dict[n] = (fibo(a) ** 2 + fibo(b) ** 2) % MODE
        
    return fibo_dict[n]


print(fibo(n))
    
    