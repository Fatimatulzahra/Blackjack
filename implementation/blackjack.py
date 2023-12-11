# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
user = draw_starting_hand("YOUR")
while user < 21:
  should_hit = input('You have ' + str(user) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    user += draw_card()
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user)

dealer = draw_starting_hand("DEALER")
while dealer < 17:
     print("Dealer has " + str(dealer) + ".")
     dealer += draw_card()
print_end_turn_status(dealer)
print_end_game_status(user, dealer)
