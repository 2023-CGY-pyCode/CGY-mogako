import sys
a = list(map(int, sys.stdin.readline().split())) #세 수를 배열로 입력받기

a.sort() # 정렬하기

print(a[1]) # 두번째에 위치하는 a[1] 원소를 출력하기
