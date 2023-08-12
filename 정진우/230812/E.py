import sys
input = sys.stdin.readline

class Game():
    def __init__(self, n, S, W, G):
        self.n = n # 3 <= n <= 10 보드 크기
        self.player_money = S # 1 <= S <= 10^7 시작시 가지는 돈  S
        self.W = W # 1 <= W <= 10^7 시작시 받게되는 월급 W
        self.G = G # 1 <= G <= 4n-8 황금 열쇠 카드의 개수
        self.walfare = 0 # 현재 사회 복지지금 얼마?
        self.player_state = 0 # 현재 위치
        self.turn_count = 0 # 현재 움직일 수 없는 턴 0 = 가능, n = n만큼 움직이지 못함 ( 무인도 )
        self.jail = False # 감옥 여부
        self.space_trip = False # 우주여행 여부
        self.board = [] # 보드 (Index, State, Value, Checked)
        self.dice_rolls = []
        self.game = True
        
    def get_dice_rolls(self, dice_list):
        self.dice_rolls = dice_list[::-1] #역순
        
    def game_end(self, state):
        if state == 'WIN':
            for board in self.board:
                try: # 이게 도시칸인가?
                    style, value, checked = board
                    if checked == 0:
                        print('LOSE')
                        self.game = False
                        return
                except: # 황금 칸이라면
                    pass
            print('WIN') # 모두 구매했다면
           
        elif state == 'LOSE':
            print('LOSE')
        
        self.game = False
        
    def golden_card_info(self, golden_card_list: list):
        self.golden_card_list = golden_card_list[::-1] # tuple 역순으로 넣음 먼저 입력된게 먼저 뽑혀야함 queue
    
    def golden_card_action(self): # action can be 1~4, value ~ x or y
                
        action, value = self.golden_card_list.pop(-1)
        self.golden_card_list.insert(0, (action, value))
        
        if action == 1: # 은행에서 value원을 받는다
            self.player_money += value 
        if action == 2: # 은행에 value원을 준다 
            if self.player_money < value: # 돈이 없으면 패배
                self.game_end('LOSE')
            else:
                self.player_money -= value 
        if action == 3: # 사회복지기금에 value원 추가
            if self.player_money < value:
                self.game_end('LOSE')
            else:
                self.walfare += value
        if action == 4: # 앞으로 이동
            self.player_state += value
            self.after_action()
        
    def after_action(self):  # 액션을 한 후에
        # 보드는 정확히 4n-4이기 때문에 이를 넘을 수 없음 0부터 시작
        # 만약 19에서 1을 굴려서 20이 됬으면 4*self.n -4 = 20보다는 크거나 같음 즉 0으로 바꿔줘야함 
        # 0번째가 스타트 
        if self.player_state >= 4*self.n - 4:  # 독립적 # 액션을 한 후에 도착 or 지나갔다면  시작 칸 : 이 칸에 정확히 멈추거나 지나가게 되면, 월급을 받게 된다.
            self.player_state = self.player_state % (4*self.n - 4)
            self.player_money += self.W # 월급 추가
            
        elif self.player_state == 0: 
            self.player_money += self.W
        
        if self.player_state == self.n-1: # 무인도
            self.jail = True
            self.turn_count = 3 # 3턴동안 갇힘
            
        elif self.player_state == 2 * (self.n-1): # 사회복지기금
            self.player_money += self.walfare
            self.walfare = 0
            
        elif self.player_state == 3 * (self.n-1): # 우주여행
            self.space_trip = True
            self.turn_count = 0
            
        else: # 일반칸
            try: # 이게 도시칸인가?
                style, value, checked = self.board[self.player_state]
                if checked == 1 or self.player_money < value: #이미 구매했다면 혹은 현금이 부족한경우
                    
                    # print("구매실패", self.player_state, self.player_money, value) 
                    pass # 아무것도 못함
                else: # 반드시 구매
                    self.player_money -= value
                    self.board[self.player_state][2] = 1 # 구매 완료
                    # print(self.player_state, "구매")
            except: # 특별 칸이라면
                style = self.board[self.player_state]
                if style == 'G':
                    self.golden_card_action()
            
    
    def get_board_state(self, board_state: list):
        for idx, board in enumerate(board_state):
            if len(board) == 2: # 일반땅
                self.board.append([board[0], int(board[1]), 0]) # style , value, checked
            else: # 황금 카드 or special
                self.board.append(board[0]) # type 
        
        
    def action(self):        
        if self.space_trip == True:
            self.player_state = 0 # 시작칸으로 이동
            self.after_action() # 월급 받아야함
        if self.dice_rolls:
            dice_1, dice_2 = self.dice_rolls.pop(-1) # 주사위 roll
        else:
            self.game_end('WIN')
        
        if self.jail == True and self.turn_count >= 1 and self.game == True: # 감옥이고 갇혀있는 턴이 남아있다면
            if dice_1 == dice_2: # 탈출
                self.jail = False
                self.turn_count = 0
                if self.dice_rolls:
                    dice_1, dice_2 = self.dice_rolls.pop(-1) # 한번더 주사위 roll (이전 주사위 못씀)
                else:
                    self.game_end('WIN')
            else:
                self.turn_count -= 1
                if self.turn_count == 0: # 횟수 차감했는데 탈출 가능하다면
                    self.jail = False # 이제 감옥 탈출
                    
                return
        
        if self.game == True:
            self.player_state += dice_1 + dice_2 # 두 주사위의 눈만큼 이동
            self.after_action() # 이동한후 액션
      
# init
n, S, W, G = map(int, input().split())
game = Game(n, S, W, G)

golden_list = []
board_list = []
for _ in range(G):
    golden_list.append(tuple(map(int, input().split())))
    
for i in range(4*n-4):
    if i % (n-1) == 0:
        if i == (n-1)*0:
            board_list.append(['START'])
        elif i == (n-1)*1:
            board_list.append(['JAIL'])
        elif i == (n-1)*2:
            board_list.append(['WARFARE'])
        elif i == (n-1)*3:
            board_list.append(['SPACE_TRIP'])
            
    else:
        board_list.append(tuple(map(str, input().split())))
    
I = int(input().strip())
dice_rolls = []

for _ in range(I):
    dice_rolls.append(tuple(map(int, input().split())))

# state init 2    
game.golden_card_info(golden_list)
game.get_board_state(board_list)
game.get_dice_rolls(dice_rolls)

# for board in game.board:
    # print(board)
    
while game.game == True:
    game.action()
    
    
    
    



                
            
            

            
        
        
        
        
    
        
        
    
        
    
        
    