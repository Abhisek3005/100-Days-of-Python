from random import randint
EAY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#function to check user's guess against actual number
turns = 0
def check_answer(guess,user_choice,turns):
    """check answer against guess.Returns the number of turns remain"""
    if user_choice > guess:
         print("Too high")
         return turns-1
    elif user_choice < guess:
        print("Too low")
        return turns-1
    else:
        print(f"You got the right number {guess}")

#make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
       return  EAY_LEVEL_TURNS
    else:
       return   HARD_LEVEL_TURNS

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    guess = randint(1,100)
    turns = set_difficulty()
    user_choice = 0
    while user_choice != guess:
        print(f"you have {turns} attemps remaining to guess the number")
        user_choice = int(input("make a guess"))
        turns = check_answer(guess,user_choice,turns)
        if turns == 0:
            print("You have run out of guesses,you loose")
            return
game()