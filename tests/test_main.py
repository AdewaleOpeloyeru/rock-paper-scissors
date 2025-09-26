import pytest
from src import main


class DummyGame:
    def __init__(self, rounds):
        self.rounds = rounds
        self.play_called = False
        self.summary_called = False

    def play(self):
        self.play_called = True

    def game_summary(self):
        self.summary_called = True


def test_main_valid_rounds(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    monkeypatch.setattr(main, "Game", DummyGame)
    main.main()
    out = capsys.readouterr().out
    assert "Number of rounds: 5" in out


def test_main_invalid_rounds(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    monkeypatch.setattr(main, "Game", DummyGame)
    main.main()
    out = capsys.readouterr().out
    assert "Invalid input. Setting rounds to default (3)." in out


def test_main_default_rounds(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "")
    monkeypatch.setattr(main, "Game", DummyGame)
    main.main()
    out = capsys.readouterr().out
    assert "Invalid input. Setting rounds to default (3)." in out


def test_main_calls_game_methods(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    game_instance = DummyGame(2)

    def game_factory(rounds):
        assert rounds == 2
        return game_instance

    monkeypatch.setattr(main, "Game", game_factory)
    main.main()
    assert game_instance.play_called
    assert game_instance.summary_called
