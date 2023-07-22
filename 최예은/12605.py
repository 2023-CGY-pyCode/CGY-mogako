for i in range(int(input())):
    s = list(input().split())
    sen = ' '.join(s[::-1])
    print(f"Case #{i+1}: {sen}")