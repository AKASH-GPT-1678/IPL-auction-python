class Player:
    def __init__(self, name, role, id,bowling_stats, batting_stats, fielding_stats, base_price, sale_price):
        self.name = name
        self.role = role
        self.id = id
        self.bowling_stats = bowling_stats
        self.batting_stats = batting_stats
        self.fielding_stats = fielding_stats
        self.base_price = base_price
        self.sale_price = sale_price
    
    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "id": self.id,
            "bowling_stats": self.bowling_stats,
            "batting_stats": self.batting_stats,
            "fielding_stats": self.fielding_stats,
            "base_price": self.base_price,
            "sale_price": self.sale_price
        }