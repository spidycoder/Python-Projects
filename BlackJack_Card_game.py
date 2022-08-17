# Rules for playing this game
# visit this Link:https://bicyclecards.com/how-to-play/blackjack/#:~:text=If%20a%20player's%20first%20two,the%20amount%20of%20their%20bet.

# creating a function which will return a random card from the list: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Create a function called calculate_score() that takes a List of cards as input
# and returns the score
def calculate_score(cards):
    ''' Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove()
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 👌"
    elif computer_score==0:
        return "Lose,Opponent has the BlackJack 😒"
    elif user_score==0:
        return "Win with a BlackJack 😎"
    elif user_score>21:
        return "You went Over,You Lose😫"
    elif computer_score>21:
        return "Oponent went over,You won❤️"
    elif user_score>computer_score:
        return "You Win😘"
    else:
        return "You Lose😫"
def play_game():
    # creating two list of user_cards and computer_cards and dealing them using deal_card(),append() and finding the sum()
    user_cards = []
    computer_cards = []
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends
    while not is_game_over:
        #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        # showing the cards
        print(f"Your's card:{user_cards},user_score={user_score}")
        print(f"computer's first card:{computer_cards[0]}")
        if user_score==0 or computer_score ==0 or user_score>21:
            is_game_over=True
        #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended
        else:
            user_choice=input("Tpye 'y' for drawing another card or type 'n' for not drawing any card: ")
            if user_choice=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17
    while computer_score!=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print(compare(user_score,computer_score))

while input("Type 'y' to play game  and type 'n' to exit the game: "):
    play_game()