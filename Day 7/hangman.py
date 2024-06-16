import random
from hangman_art import stages,logo
from hangman_words import word_list
print(logo)
choosen_word=random.choice(word_list)
lives=6
display=[]

for item in choosen_word:
    display+='_'
print(display)
end_of_game=False
while end_of_game==False:
    guess=input(f"Guess a word:").lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You loose")       
    print(display)
    if "_" not in display:
      end_of_game=True
      print("you won")    
    print(stages[lives])      