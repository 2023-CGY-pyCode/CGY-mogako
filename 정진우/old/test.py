def soulution1(arr):
    if arr[0] >= arr[1] and arr[0] >= arr[2] and arr[0] >= arr[3]:
        return arr[0]
    if arr[1] >= arr[0] and arr[1] >= arr[2] and arr[1] >= arr[3]:
        return arr[1]
    if arr[2] >= arr[0] and arr[2] >= arr[1] and arr[2] >= arr[3]:
        return arr[2]
    return arr[3]

def solution2(arr):
    mx = arr[0]
    for i in range(mx):
        if arr[i] > mx: 
            mx = arr[i]
        
    return mx

def solution3(arr):
    return max(arr)