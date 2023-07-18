import sys
from collections import Counter # 배열의 요소 수 세기

N = int(sys.stdin.readline()) # 팔린 책 수

A = [sys.stdin.readline() for _ in range(N)] # 제목 저장

common = Counter(A).most_common()

best_seller = []

# Counter(변수) => Counter({문자 : 개수}) 딕셔너리 형태로 반환

# Counter(변수).most_common() => (문자, 개수) 리스트 속 튜플형태로 저장


for i in range(len(common)):
    if(common[0][1] == common[i][1]): # 가장 앞의 수 = 가장 큰 수 
        best_seller.append(common[i][0]) # 그러므로 앞의 수와 비교하여 같으면 베스트셀러

best_seller.sort() # 베스트셀러 정렬

print(best_seller[0]) # 가장 첫 번째 책 출
