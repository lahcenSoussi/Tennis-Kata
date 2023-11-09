import pytest

from TennisGame import TennisGame

@pytest.fixture
def game():
    return TennisGame("Player1", "Player2")

def test_game_first_case(game):
    assert game.AddPoint(game.player1) == "Player1 - 15\tPlayer2 - love"
    assert game.AddPoint(game.player1) == "Player1 - 30\tPlayer2 - love"
    assert game.AddPoint(game.player2) == "Player2 - 15\tPlayer1 - 30"
    assert game.AddPoint(game.player2) == "Player2 - 30\tPlayer1 - 30"
    assert game.AddPoint(game.player1) == "Player1 - 40\tPlayer2 - 30"
    assert game.AddPoint(game.player2) == "Deuce"
    assert game.AddPoint(game.player1) == "Player1 has advantage"
    assert game.AddPoint(game.player2) == "Deuce"
    assert game.AddPoint(game.player2) == "Player2 has advantage"
    assert game.AddPoint(game.player1) == "Deuce"
    assert game.AddPoint(game.player1) == "Player1 has advantage"
    assert game.AddPoint(game.player1) == "Game is ended, Player1 wins!"
    
def test_game_second_case(game):
    assert game.AddPoint(game.player1) == "Player1 - 15\tPlayer2 - love"
    assert game.AddPoint(game.player1) == "Player1 - 30\tPlayer2 - love"
    assert game.AddPoint(game.player2) == "Player2 - 15\tPlayer1 - 30"
    assert game.AddPoint(game.player1) == "Player1 - 40\tPlayer2 - 15"
    assert game.AddPoint(game.player1) == "Game is ended, Player1 wins!"