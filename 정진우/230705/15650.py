def dfs(st, arr, depth, limit):
    if depth == limit:
        for i in st:
            print(i, end=" ")
        print()
        return
    
    for i in arr:
        if st[-1] < i:
            st.append(i)
            dfs(st, arr, depth+1, limit)
            st.pop(-1)
    
    
    
M, N = tuple(map(int, input().split()))

arr = range(M+1)[1:] # 1부터 오름차순

for i in arr:
    st = []
    st.append(i)
    dfs(st, arr, 1, N)
    
    


