import json

def updateBowlstats(name, bowling_stats):
   
    with open('data/players.json', "r") as f:
        player_list = json.load(f)

 
    for data in player_list:
        if data["name"] == name:     
            data["bowling_stats"] = bowling_stats

    
    with open('data/players.json', "w") as f:
        json.dump(player_list, f, indent=4)





updateBowlstats("Ms Dhoni" , "200" )