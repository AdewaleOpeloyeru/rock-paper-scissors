import pytest
from src.game import Game

class DummyPlayer:
    def __init__(self, choice=None, score=0):
        self.choice = choice
        self.score = score
    def make_choice(self):
        pass

@pytest.fixture
def game():
    g = Game(rounds=3)
    g.human = DummyPlayer()
    g.computer = DummyPlayer()
    return g

@pytest.mark.parametrize(
    "human_choice, computer_choice, expected",
    [
        ("r", "s", "won"),
        ("p", "r", "won"),
        ("s", "p", "won"),
        ("r", "p", "lost"),
        ("p", "s", "lost"),
        ("s", "r", "lost"),
        ("r", "r", "tie"),
        ("p", "p", "tie"),
        ("s", "s", "tie"),
    ]
)
def test_get_result(game, human_choice, computer_choice, expected):
    game.human.choice = human_choice
    game.computer.choice = computer_choice
    assert game.get_result() == expected

def test_play_increments_scores(monkeypatch):
    g = Game(rounds=3)
    g.human = DummyPlayer(score=0)
    g.computer = DummyPlayer(score=0)
    # Simulate: win, lose, tie
    choices = [("r", "s"), ("r", "p"), ("r", "r")]
    def make_choice_human():
        g.human.choice = choices[g.human.score + g.computer.score][0]
    def make_choice_computer():
        g.computer.choice = choices[g.human.score + g.computer.score][1]
    g.human.make_choice = make_choice_human
    g.computer.make_choice = make_choice_computer
    g.play()
    assert g.human.score == 1
    assert g.computer.score == 1

def test_game_summary_win(capsys):
    g = Game()
    g.human = DummyPlayer(score=2)
    g.computer = DummyPlayer(score=1)
    g.game_summary()
    out = capsys.readouterr().out
    assert "Congratulations! You won the game!" in out

def test_game_summary_lose(capsys):
    g = Game()
    g.human = DummyPlayer(score=1)
    g.computer = DummyPlayer(score=2)
    g.game_summary()
    out = capsys.readouterr().out
    assert "Sorry, you lost the game." in out

def test_game_summary_tie(capsys):
    g = Game()
    g.human = DummyPlayer(score=1)
    g.computer = DummyPlayer(score=1)
    g.game_summary()
    out = capsys.readouterr().out
    assert "The game is a tie!" in out

def test_play_prints_rounds(monkeypatch, capsys):
    g = Game(rounds=1)
    g.human = DummyPlayer()
    g.computer = DummyPlayer()
    g.human.choice = "r"
    g.computer.choice = "s"
    g.human.make_choice = lambda: None
    g.computer.make_choice = lambda: None
    g.play()
    out = capsys.readouterr().out
    assert "Round 1" in out
    assert "You: r | Computer: s" in out
    assert "You won this round!" in out

def test_init_default_rounds():
    g = Game()
    assert g.rounds == 3

def test_init_custom_rounds():
    g = Game(rounds=5)
    assert g.rounds == 5
