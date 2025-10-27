class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position

class NFL_team:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players
    def display_team(self):
        print(f"Team Name: {self.team_name}")
        print("Players:")
        for player in self.players:
            print(f"{player.player_name} - {player.player_position}")
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

playerList = [player1, player2, player3, player4]
team = NFL_team("GOATS", playerList)
team.display_team()
