
import random


class Game():

    

    def __init__(self) :
        self.cards = Cards()
        self.game_is_running = True
        total_points = 300
        starting_points = 300

    def start_game(self):
        while self.game_is_running == True:
            returned_cards = self.cards.pick_random_cards()
            print(f"The card is: {returned_cards[0]}")
            user_answer = self.ask_user()
            print(f"Next card was: {returned_cards[1]}")
            self.check_if_correct(user_answer, returned_cards)
            self.check_game_over()
            self.check_to_continue()
            print()
            print()

    def check_if_correct(self, user_answer, returned_cards):
        if user_answer == "l" and returned_cards[1] < returned_cards[0]:
            self.add_points()
        elif user_answer == "h" and returned_cards[1] > returned_cards[0]:
            self.add_points()
        else:
            self.subtract_points()

        
    def ask_user(self):
        response = input("Higher or lower? (h/l) ")
        return response

    def add_points(self):
        self.total_points += 100
        print(f"Your score is: {self.total_points}")
        
    def subtract_points(self):
        self.total_points -= 75
        print(f"Your score is: {self.total_points}")

    def check_to_continue(self):
        desire = input("Play again? (y/n) ")
        if desire == "n":
            self.game_is_running = False
       
    def end_game(self,desire):
        if desire == "n":
            self.game_is_running = False

    def check_game_over(self):
        if self.total_points <=0:
            self.game_is_running = False

class Cards():
    card_1 = 0
    card_2 = 0


    def __init__(self) :
        pass
        

    def pick_random_cards(self):

        card_1 = random.randint(1,13)
        card_2 = random.randint(1,13)
        while card_1 == card_2:
            card_2 = random.randint(1,13)
        return card_1, card_2


game = Game()
game.start_game()
