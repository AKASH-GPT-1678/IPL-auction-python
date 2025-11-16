from enum import Enum



class Player:
    def __init__(self, name, role  , bowling_stats ,batting_stats , fielding_stats ,base_price , sale_price):
        self.name = name
        self.role = role
        self.bowling_stats = bowling_stats
        self.batting_stats = batting_stats
        self.fielding_stats = fielding_stats
        self.base_price = base_price
        self.sale_price = sale_price


    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "bowling_stats": self.bowling_stats,
            "batting_stats": self.batting_stats,
            "fielding_stats": self.fielding_stats,
            "base_price": self.base_price,
            "sale_price": self.sale_price
        }
    
    def display(self):
        print(self.name)
        print(self.role)
        print(self.bowling_stats)
        print(self.batting_stats)
        print(self.fielding_stats)
        print(self.base_price)
        print(self.sale_price)
    
    def get_name(self):
        return self.name


    




    