from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([5], draw_card), 5)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([12], draw_card), 10)

  def test_print_header(self):
    expected_output1 = "-----------\nDEALER TURN\n-----------\n"
    expected_output2 = "-----------\nuser turn\n-----------\n"
    expected_output3 = "-----------\njak1 TURN\n-----------\n"
    self.assertEqual(get_print(print_header, "DEALER TURN"), expected_output1)
    self.assertEqual(get_print(print_header, "user turn"), expected_output2)
    self.assertEqual(get_print(print_header, "jak1 TURN"), expected_output3)

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([4,1], draw_starting_hand, "USER"), 15)
    self.assertEqual(mock_random([2,5], draw_starting_hand, "USER"), 7)
    self.assertEqual(mock_random([12,6], draw_starting_hand, "DEALER"), 16)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 17), 'Final hand: 17.\n')
    self.assertEqual(get_print(print_end_turn_status, 21), 'Final hand: 21.\nBLACKJACK!\n')
    self.assertEqual(get_print(print_end_turn_status, 23), 'Final hand: 23.\nBUST.\n')

  def test_print_end_game_status(self):
    output1 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    output2 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    output3 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 20,18), output1)
    self.assertEqual(get_print(print_end_game_status, 20,21), output2)
    self.assertEqual(get_print(print_end_game_status, 17,17), output3)

if __name__ == '__main__':
    unittest.main()
