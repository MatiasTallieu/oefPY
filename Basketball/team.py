from player import *
class Team():
    def __init__(self,name,abbreviation):
        self.name= name
        self.abbreviation = abbreviation
        self.players = []

    def add_player(self,name,number):
        p1 = Player(name,number)
        self.players.append(p1)
        
        
    def get_player(self,number):
        for player in self.players:
            if player.number == number:
                return player

t = Team("Las Vegas",'LV')
t.add_player("Matias",10)
mat = t.get_player(10)
print(mat.name)
print(mat.number)