import random

class Player():
    def __init__(self):
        self.score = 0
        self.choice = ""


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def make_choice(self):
        valid_choices = ['r', 'p', 's']
        choice = input(f"Rock, paper or scissors [r/p/s]? ").lower()
        while choice not in valid_choices:
            print("Invalid choice. Please enter rock(r), paper(p), or scissors(s)")
            choice = input(f"Rock, paper or scissors [r/p/s]? ").lower()
        self.choice = choice


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def make_choice(self):
        self.choice = random.choice(['r', 'p', 's'])


class Game():
    def __init__(self, rounds=3):
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()
        self.rounds = rounds

    def play(self):
        for r in range(self.rounds):
            print(f"\nRound {r + 1}")
            self.human.make_choice()
            self.computer.make_choice()
            print(f"You: {self.human.choice} | Computer: {self.computer.choice}")
            result = self.get_result()
            if result == "won":
                self.human.score += 1
                print("You won this round!")
            elif result == "lost":
                self.computer.score += 1
                print("You lost this round!")
            else:
                print("This round is a tie!")

    def get_result(self):
        if self.human.choice == self.computer.choice:
            return "tie"
        elif (self.human.choice == 'r' and self.computer.choice == 's') or \
             (self.human.choice == 'p' and self.computer.choice == 'r') or \
             (self.human.choice == 's' and self.computer.choice == 'p'):
            return "won"
        else:
            return "lost"

    def game_summary(self):
        print("\n[Game Summary] Your points: ", self.human.score, " | Computer points: ", self.computer.score)
        if self.human.score > self.computer.score:
            print("Congratulations! You won the game!")
        elif self.human.score < self.computer.score:
            print("Sorry, you lost the game.")
        else:
            print("The game is a tie!")

def main():
    print("--- Welcome to Rock, Paper, Scissors Game ---")
    rounds = input("How many rounds would you like to play? (default is 3): ")
    if rounds.isdigit():
        print(f"Number of rounds: {rounds}")
        rounds = int(rounds)
    else:
        print("Invalid input. Setting rounds to default (3).")
        rounds = 3
    my_game = Game(rounds)
    my_game.play()
    my_game.game_summary()

if __name__ == "__main__":
    main()
