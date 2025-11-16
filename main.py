from player import Player
import json
import os

def new_player():
    name = input("Enter the name of the player: ")
    role = input("Enter the role of the player: ")
    bowling_stats = input("Enter the bowling stats of the player: ")
    batting_stats = input("Enter the batting stats of the player: ")
    fielding_stats = input("Enter the fielding stats of the player: ")
    base_price = input("Enter the base price of the player: ")
    sale_price = input("Enter the sale price of the player: ")
    player = Player(name, role , bowling_stats ,batting_stats , fielding_stats ,base_price , sale_price)
    return player



filename = "data/players.json"

if os.path.exists(filename):
    print("File exists!")
else:
    with open(filename, "w") as f:
        json.dump([], f)


player = new_player()

try:
    with open("data/players.json", "r") as f:
        players_list = json.load(f)
except FileNotFoundError:
    players_list = []

# Add the new player
players_list.append(player.to_dict())

# Save back to file
with open("data/players.json", "w") as f:
    json.dump(players_list, f, indent=4)

print("Player saved successfully!")