import random


class Player:
    def __init__(self):
        self.score = 0
        self.choice = ""


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def make_choice(self):
        valid_choices = ["r", "p", "s"]
        choice = input(f"Rock, paper or scissors [r/p/s]? ").lower()
        while choice not in valid_choices:
            print("Invalid choice. Please enter rock(r), paper(p), or scissors(s)")
            choice = input(f"Rock, paper or scissors [r/p/s]? ").lower()
        self.choice = choice


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def make_choice(self):
        self.choice = random.choice(["r", "p", "s"])
