from player import HumanPlayer, ComputerPlayer

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
