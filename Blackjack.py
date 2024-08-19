import random
import Blackjack_art

def blackjack_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
         return "You win!!"
    else:
        return "You lose!!"
    
def play_blackjack():
    print(Blackjack_art.logo)
    user_score = -1
    computer_score = -1
    user_cards = []
    computer_cards = []
    continue_or_not = True

    for i in range(2):
        user_cards.append(blackjack_cards())
        computer_cards.append(blackjack_cards())
    
    while continue_or_not:
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)

        print(f"Your cards: {user_cards}, Your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_or_not = False
        else:
            user_hit = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_hit == "y":
                user_cards.append(blackjack_cards())
            else:  
                continue_or_not = False
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(blackjack_cards())
        computer_score = calculate(computer_cards)

    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
    print(compare(user_score,computer_score))
    print("***************************************")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 100)
    play_blackjack()
