
## Tennis Game Kata

This project implements a simple Tennis Game using Python. It is inspired by the Tennis Game Kata, a coding exercise aimed at practicing problem-solving and coding skills.

- Overview

The Tennis Game consists of two main classes:

    Player: Represents a player with a name, score, and methods for winning points and retrieving information.
    TennisGame: Manages the game's state, scoring logic, and checks for game end conditions.

- Usage

    + Player Class:
        WinPoint(): Increases the player's score.
        GetScore(): Retrieves the player's current score.
        GetScoreText(): Retrieves the player's score in text format.
        GetName(): Retrieves the player's name.

    + TennisGame Class:
        OtherPlayer(player): Returns the opponent of the provided player.
        HasAdvantage(player): Checks if a player has the advantage.
        AreDeuce(player): Checks if the game is in a deuce state.
        IsWinner(player): Checks if a player has won the game.
        GameEnded(): Checks if the game has ended.
        AddPoint(player): Adds a point to the specified player and returns the current state of the game.

- Test
    The project includes tests using the pytest framework to ensure the correctness of the Tennis Game implementation. Run the tests using: pytest test_tennisGame.py