import json

class Team:
    
    def to_dict(self , name, purse):
        return {
            "name": name,
            "purse": purse
        }
    def createTeam(self, name, purse):
        with open('data/teams.json', "r") as f:
            team_list = json.load(f)
        team = {"name": name, "purse": purse}
        team_list.append(team)
        with open('data/teams.json', "w") as f:
            json.dump(team_list, f, indent=4)
        print("Team created successfully!") 
    
      
    
    