N = input()
      
while N: #N이 사라질 때 까지
    if len(N) > 10: #N의 길이 10보다 큰경우
        print(N[:10]) # 10개 출력
        N = N[10:] # 앞의 내용은 이미 출력하였기 때문에 삭제해준다.
    else:
        print(N) #10보다 작은 경우 N을 출력하고 WHILE문 탈출
        N = False
