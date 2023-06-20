class Ship:
    def __init__(self, name, ship_type, captain):
        self.name = name
        self.ship_type = ship_type
        self.captain = captain

    def update_name(self, new_name):
        self.name = new_name

    def update_captain(self, new_captain):
        self.captain = new_captain
