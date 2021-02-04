############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###############################################################

import random
from replit import clear
from art import logo

#deal card funtion 
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  random_card = random.choice(cards)  
  return random_card 

#score calculator function
def calculate_score(input_card):
    
  if sum(input_card) == 21 and len(input_card) == 2:
      return 0; #blackjack
  
  if 11 in input_card and sum(input_card) > 21: #ace can act as 1 as well as 11 
    input_card.remove(11) #removes the element
    input_card.append(1) #adds the element

  return sum(input_card) #return the score

#compare function
def compare (user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You lose, opponent has a Blackjack"
  elif user_score == 0:
    return "You Win with a Blackjack"
  elif user_score > 21:
    return "You lose, you went over"
  elif computer_score > 21:
    return "You win, computer went over"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You lose"

#play game function ...... main logic part
def play_game():
  print(logo)

  is_game_over = False
#store the cards of user and computer as a list
  user_cards = []
  computer_cards = []
#add 2 deal cards to each of the player i.e. user and computer
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" computer first card: {computer_cards[0]}")

    if computer_score == 0 or user_score == 0 or user_score > 21: # ends the game if these conditions met
        is_game_over = True
    else: #game continues
      choice = input("do you want to draw another card? Type 'y' for yes and 'n' for no\t")

      if choice == "y": 
        user_cards.append(deal_card()) # add third card
      else:
        is_game_over = True #end game
# computer plays now
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards) #calculater score again
# print final hands
  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
#call compare()
  print(compare(user_score, computer_score))

#execution starts here
while input("Do you want to play a game of Black jack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


