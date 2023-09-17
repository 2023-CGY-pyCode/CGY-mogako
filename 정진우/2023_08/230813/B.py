A = input()
B = input()
C = input()

def function(number: int):
    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0 and number % 5 != 0:
        return 'Fizz'
    elif number % 3 != 0 and number % 5 == 0:
        return 'Buzz'
    else:
        return number
    

if A.isnumeric():
    B = int(A)+1
    C = int(A)+2
    
elif B.isnumeric():
    A = int(B)-1
    C = int(B)+1
    
elif C.isnumeric():
    A = int(C)-1
    B = int(C)-2
    
print(str(function(int(C)+1)))