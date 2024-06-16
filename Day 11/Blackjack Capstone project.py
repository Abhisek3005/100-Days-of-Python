import random
#function call
def deal_cards():
 cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
 card=random.choice(cards)
 return card
user_cards=[]
computer_cards = []
for _ in range(2):
 #new_card = deal_cards()
 user_cards.append(deal_cards())
 computer_cards.append(deal_cards())
is_game_over = False
def calculate_sccore(cards):
 return sum(cards)
 if sum(cards) == 21 and len(cards) == 2:
  return 0
 if 11 in cards and sum(cards) > 21:
  cards.remove(11)
  cards.append(1)
while not is_game_over:
    user_score = calculate_sccore(user_cards)
    computer_score = calculate_sccore(computer_cards)
    print(f"Your cards : {user_cards} , current score : {user_score}")

    print(f"computers first card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
     is_game_over = True
    else:
     user = input("Type 'Y' to get another card, type 'N' to pass \n" )
     if user == "Y" :
      user_cards.append(deal_cards())
     else:
      is_game_over = True 

while computer_score != 0 and computer_score < 17:
 computer_cards.append(deal_cards())
 computer_score = calculate_sccore(computer_cards)

def compare(user_score,computer_score):
 if user_score == computer_score:
  return "Draw"
 elif computer_score == 0:
  return "lose,opponent has blackjack"
 elif user_score == 0:
  return "win with a blackjack"
 elif user_score > 21:
  return "you went over.You loose"
 elif computer_score > 21:
  return "Opponent went over,You win"
 elif user_score > computer_score:
  return "You win"
 else:
  return "You loose"
compare(user_score,computer_score)





