import sys
a = [int(sys.stdin.readline()) for _ in range(8)] # 숫자 여러 줄 입력받는 방법

b = a[:] # 리스트 복제할 때 등호로 복제하지 않기 !주의!
b.sort() # 복제해서 정렬하기
A = b[3:8] # 정렬한 값 중 큰 값만 저장


print(sum(A))# 가장 높은 점수 5개 합


for i in range(len(a)):
    for j in range(len(A)):
        if a[i] == A[j]:
            print(i + 1, end = " ") # 5개의 값 위치 출력
            break
