from game import Game

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
