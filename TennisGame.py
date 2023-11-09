class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    @property
    def WinPoint(self):
        self.score += 1

    @property
    def GetScore(self):
        return self.score
    
    @property
    def GetScoreText(self):
        score_map = {0: "love", 1: "15", 2: "30", 3: "40"}
        return score_map[self.score]

    @property
    def GetName(self):
        return self.name
    
class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
    
    def OtherPlayer(self, player):
        return self.player1 if player.GetName == self.player2.GetName else self.player2

    def HasAdvantage(self, player):
        return player.GetScore >= 4 and (player.GetScore - self.OtherPlayer(player).GetScore == 1)
    
    def AreDeuce(self, player):
        p1 = player.GetScore
        p2 = self.OtherPlayer(player).GetScore
        return p1 >= 3 and p2 >= 3 and p1 == p2
    
    def IsWinner(self, player):
        return player.GetScore >= 4 and (player.GetScore - self.OtherPlayer(player).GetScore >= 2)
    
    def GameEnded(self):
        return self.IsWinner(self.player1) or self.IsWinner(self.player2)
    
    def AddPoint(self, player):
        player.WinPoint
        other = self.OtherPlayer(player)

        if self.AreDeuce(player):
            return "Deuce"
        elif self.HasAdvantage(player):
            return f"{player.GetName} has advantage"

        elif self.GameEnded():
            if self.IsWinner(player):
                return f"Game is ended, {player.GetName} wins!"
            else:
                return "Deuce"
        else:
            return f"{player.GetName} - {player.GetScoreText}\t{other.GetName} - {other.GetScoreText}"        
   
