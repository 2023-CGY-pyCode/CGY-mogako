import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

arrival = []

p = [i for i in range(G+1)] 


for _ in range(P):
    arrival.append(int(input()))
    
    
count = 0

def find(node : int):
    if p[node] == node:
        return node
    
    p[node] = find(p[node])
    return p[node]

def union(a : int, b : int):  # a < b
    pa = find(a) 
    pb = find(b)
    
    p[pb] = pa 
def check():
    global count
    for idx in range(len(arrival)):
        airplane = arrival[idx]
        
        while True:
            if find(airplane) == 0:
                return
            if find(airplane) == airplane: # 자기자신에 도킹가능
                count += 1
                union(airplane-1, airplane) # 하나 뺸것과 유니온 해줌
                break
            
            else:
                airplane = find(airplane)
                
                
check()
print(count)
            
