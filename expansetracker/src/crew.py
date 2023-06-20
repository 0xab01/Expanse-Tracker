class Crew:
    def __init__(self, name, position, ship_id):
        self.name = name
        self.position = position
        self.ship_id = ship_id

    def update_position(self, new_position):
        self.position = new_position

    def change_ship(self, new_ship_id):
        self.ship_id = new_ship_id
