from enum import Enum

class Color(Enum):
    R = 0
    B = 1
    Y = 2
    G = 3

card_color = [0, 0, 0, 0] # 0 : R, 1: B, 2: Y, 3: G
card_number = [0] * 10 # 0번째 인덱스는 안쓰임

score = 0
for _ in range(5):
    color, number = tuple(map(str, input().split(" ")))
    card_number[int(number)] += 1
    card_color[Color[color].value] += 1
    
if max(card_color) == 5: # 모두 같은색 4번조건
    straight = 0 # 연속 체크
    for idx, i in enumerate(card_number):
        if idx == 0:
            continue
        if i == 1:
            straight += 1
            if straight == 5:
                score = idx + 900  # 1번 조건
                break
            else:
                score = idx + 600  # 4번 조건
        if i == 0:
            straight = 0
            
if max(card_number) == 4 and not score:
    for idx, i in enumerate(card_number):
        if idx == 0:
            continue
        if i == 4:
            score = idx + 800 # 2번
            
if max(card_number) == 3 and not score:
    three_same_idx = 0
    two_same_idx = 0
    for idx, i in enumerate(card_number):
        if idx == 0:
            continue
        if i == 3:
            three_same_idx = idx
            # score = three_same_idx+400 # 6번
        if i == 2:
            two_same_idx = idx
            # score = three_same_idx*10 + idx + 700 #3번
    if three_same_idx and two_same_idx:
        score = three_same_idx*10 + two_same_idx + 700 #3번
    if three_same_idx and not two_same_idx:
        score = three_same_idx+400 # 6번

if not score:
    straight = 0            
    for idx, i in enumerate(card_number):
        if i == 1:
            straight += 1
            if straight == 5:
                score = idx + 500 # 5번
        elif i == 0:
            straight = 0
        
if max(card_number) == 2 and not score:
    two_same_count = 0
    two_same_idx = []
    for idx, i in enumerate(card_number):
        if i == 2:
            two_same_count +=1
            two_same_idx.append(idx)
        
    if two_same_count == 1:
        score = two_same_idx[0] + 200 # 8번
    if two_same_count == 2:
        score = two_same_idx[1] * 10 + two_same_idx[0] + 300 # 7번

if not score:
    for idx, i in enumerate(card_number):
        if i == 1:
            score = idx + 100 # 9번
            
print(score)
    