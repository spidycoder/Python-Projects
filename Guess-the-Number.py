
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
# selecting a random number from 1 to 100
from random import randint
#function to check user's guess against answer
def check_answer(guess,answer,turn):
    if guess>answer:
        print("Too High")
        return turn-1
    elif guess<answer:
        print("Too Low")
        return turn-1
    else:
        print(f"you got it!😎,the answer is {answer}")
#Making a function to set difficulty
def set_difficulty():
    level=input("choose a diffuclty level:Easy or Hard? ")
    if level=="Easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
#making a game function
def game():
    #chosing a random number from 1 to 100
    print("Welcome to the Guess-Number Game.")
    print("Guess the number between 1 to 100 👍")
    answer = randint(1,100)
    turn=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turn} attempts remaning to guess the number ")
        #Let's guess the number
        guess=int(input("Make a guess: "))
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print("You have run out of attempts 😫")
            return
        elif guess!=answer:
            print("Guess Again 😒")
        

game()