import pytest
from src.player import Player, HumanPlayer, ComputerPlayer

def test_player_initialization():
    p = Player()
    assert p.score == 0
    assert p.choice == ""

def test_humanplayer_inherits_player():
    hp = HumanPlayer()
    assert isinstance(hp, Player)
    assert hp.score == 0
    assert hp.choice == ""

@pytest.mark.parametrize("user_input,expected", [
    (["r"], "r"),
    (["p"], "p"),
    (["s"], "s"),
])
def test_humanplayer_make_choice_valid(monkeypatch, user_input, expected):
    hp = HumanPlayer()
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))
    hp.make_choice()
    assert hp.choice == expected

def test_humanplayer_make_choice_invalid_then_valid(monkeypatch, capsys):
    hp = HumanPlayer()
    inputs = iter(["x", "rock", "p"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    hp.make_choice()
    assert hp.choice == "p"
    out = capsys.readouterr().out
    assert "Invalid choice" in out

def test_computerplayer_make_choice_random(monkeypatch):
    cp = ComputerPlayer()
    monkeypatch.setattr("random.choice", lambda choices: "s")
    cp.make_choice()
    assert cp.choice == "s"

def test_computerplayer_inherits_player():
    cp = ComputerPlayer()
    assert isinstance(cp, Player)
    assert cp.score == 0
    assert cp.choice == ""
