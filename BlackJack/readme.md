#################### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## 1. The deck is unlimited in size. 
## 2. There are no jokers. 
## 3. The Jack/Queen/King all count as 10.
## 4. The the Ace can count as 11 or 1.
## 5. Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## 6. The cards in the list have equal probability of being drawn.
## 7. Cards are not removed from the deck as they are drawn.
## 8. The computer is the dealer.


##################### Steps #####################

Steps 1: Create a deal_cards() function that uses the List below to return a random card.
---- 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Step 2: Deal the user and computer 2 cards each using deal_cards() and append() it to their respective lists.
- player_card = []
- dealer_card = []

Step 3: Create a function called calculate_score() that takes a List of cards as input and returns the sum of the elements in the list. 

Step 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

Step 5: Create a function check_ace() and check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. Use append() and remove().

Step 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

Step 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_cards() function to add another card to the player_card List. If no, then the game has ended.

Step 8: The score will need to be rechecked with every new card drawn and the checks in Step 4 and Step 5 needs to be repeated until the game ends.

Step 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

Step 10: Create a function called results() and pass in the player_total and computer_total. 
#-- If the computer and user both have the same score, then it's a draw. 
#-- If the computer has a blackjack (0), then the user loses. 
#-- If the user has a blackjack (0), then the user wins. 
#-- If the user_score is over 21, then the user loses. 
#-- If the computer_score is over 21, then the computer loses. 
#-- If none of the above, then the player with the highest score wins.

Step 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack.