import json
fields = [
    "name",
    "role",
    "bowling_stats",
    "batting_stats",
    "fielding_stats",
    "base_price",
    "sale_price"
]

def update_player_field():
    name = input("Enter player name to update: ")
    field_name = input("Enter fieldname ?")
    if field_name not in fields:
        print("Enter Valid Field")
        return
        
            
    value = input(f"Enter new value for {field_name}: ")

   
    with open('data/players.json', "r") as f:
        player_list = json.load(f)

  
    updated = False
    for player in player_list:
        if player["name"] == name:
            player[field_name] = value
            updated = True
            break

   
    if updated:
        with open('data/players.json', "w") as f:
            json.dump(player_list, f, indent=4)
        print(f"{field_name} updated successfully!")
    else:
        print("Player not found!")



def deletePlayer():
    name = input("Player you want to delete? ")
    

    with open('data/players.json', "r") as f:
        player_list = json.load(f)
    
 
    for player in player_list:
        if player["name"] == name:
            player_list.remove(player)
            print("Player Deleted Successfully")
            break
    else:
        print("Player not found!")
    
    
    with open('data/players.json', "w") as f:
        json.dump(player_list, f, indent=4)

        

update_player_field()