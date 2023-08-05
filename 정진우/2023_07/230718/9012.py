from collections import deque
T = int(input())

def check(string, st):
    for i in string:
        if i == ")":
            if not st or st[-1] == ")":
                return "NO"
            else:
                if st[-1] == "(":
                    st.pop()
        else:
            st.append(i)  
            
    return "NO" if st else "YES"
    

for _ in range(T):
    a = str(input())
    st = deque()
    print(check(a, st))

        
        
        