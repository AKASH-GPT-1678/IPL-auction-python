from enum import Enum
from player import Player


import json

class UsePlayer:
    


    def loadfile(self):
        try:
            with open("data/players.json", "r") as f:
                players_list = json.load(f)
        except FileNotFoundError:
            players_list = []
        return players_list

    def new_player(self):
        id  = input("Enter the id of the player: ")
        name = input("Enter the name of the player: ")
        role = input("Enter the role of the player: ")
        bowling_stats = input("Enter the bowling stats of the player: ")
        batting_stats = input("Enter the batting stats of the player: ")
        fielding_stats = input("Enter the fielding stats of the player: ")
        base_price = input("Enter the base price of the player: ")
        sale_price = input("Enter the sale price of the player: ")

        player = Player(name, role, id, bowling_stats, batting_stats, fielding_stats, base_price, sale_price)

       
        players_list = self.loadfile()

    
        players_list.append(player.to_dict())

  
        with open("data/players.json", "w") as f:
            json.dump(players_list, f, indent=4)
            


        return player
    
     
    def getPlayerById(self, id):
        players_list = self.loadfile()
        for player in players_list:
            if player["id"] == id:
                return Player(**player)
        return None

    
    
    
    

    


    




    