#Import the required modules

import random
from replit import clear
from logo import art


#Define the function deal_cards() which will randomly pick a card and return to the main function
def deal_cards():
    card = random.choice(cards)
    return card

#Define the function calculate_score() which will return the sum of the elements in the list.
def calculate_score(cards):
  total = sum(cards)
  #if the list has a 10 and 11, ie., a total of 21 (represents Blackjack in this game), then return 0.
  if (total == 21 and len(cards) == 2):
    return 0

  #Call the function check_ace() which will check for 11 in the list and replaces 1 if the sum is greater than 21.
  total = check_ace(cards, total)

  return total

#Define the function check_ace()
def check_ace(cards, total):
  if 11 in cards and total > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)   

#Define the function results() which will compare the totals of player_card and dealer_card and declares the winner.
def results(player, dealer):
  if player > 21 and dealer > 21:
    print("You Lose. You went over 21.")

  if player == dealer:
    print("It's a draw.")
  elif dealer == 21:
    print("You Lose. Dealer has Blackjack!")
  elif player == 21:
    print("Great!! You win with Blackjack!")  
  elif dealer > 21:
    print("You win. Dealer went over 21.")   
  elif player > dealer:
    print("Yay! You Win.")
  elif dealer > player:
    print("Oops.. You Lose.")
     
#Main function starts here

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_BlackJack():

  print(art)
  
  player_card = []
  dealer_card = []

  game_over = False

  #Call deal_cards() to choose two random cards for each list
  for card in range(2):
    player_card.append(deal_cards())
    dealer_card.append(deal_cards())

  while not game_over:
    #Calculate the totals
    player_total = calculate_score(player_card)
    computer_total = calculate_score(dealer_card)

    print(f"Your card {player_card}, Current score: {player_total}")
    print(f"Computer's card {dealer_card[0]}")

    if player_total == 0 or computer_total == 0 or player_total > 21:
      game_over = True
    else:
      #Ask the user if they wants to draw another card
      deal_user = input("Do you want to deal another card? Y or No - ").lower()
      if deal_user == 'y':
        player_card.append(deal_cards()) 
      else:
        game_over = True
  #Check if the computer's total is greater than 17. If not, draw cards.
  while computer_total != 0 and computer_total < 17:
    dealer_card.append(deal_cards())
    computer_total = calculate_score(dealer_card)

  #Display the results
  print(f"Your final cards: {player_card} and Your final score: {player_total}")
  print(f"Dealer's final cards: {dealer_card} and Dealer's final score: {computer_total}")
  results(player_total, computer_total)

#Loop the game until the player selects No.
game = True
while game:
  choice = input("Do you want to play a game of BlackJack? Y or N: ").lower()
  if choice == 'y':
    clear()
    play_BlackJack()
  elif choice == 'n':
    game = False
    print("Try whenever you are ready.")
  else:
    game = False
    print("Enter a valid choice.")

