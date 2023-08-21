N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()


max_diff = arr[-1] - arr[0]
start, end = 1, max_diff
answer = 0

while start <= end:
    mid = (end+start) //2
    curr = arr[0]
    count = 1
    diff = max_diff
    
    for i in range(1, N):
        if arr[i] - curr >= mid: # 간격이 기준보다 넓으면
            diff = min(diff, arr[i] - curr)
            count += 1
            curr = arr[i]
    
    if count >= C: # 공유기 모두 설치가능하면 start를 mid+ 1
        start = mid + 1
        answer = max(answer, diff)
    else:
        end = mid -1 
        
print(answer)