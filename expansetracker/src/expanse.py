class Expanse:
    def __init__(self):
        self.ships = {}
        self.crews = {}

    def add_ship(self, name, ship_type, captain):
        ship_id = len(self.ships) + 1
        ship = {"name": name, "type": ship_type, "captain": captain}
        self.ships[ship_id] = ship
        return ship_id

    def get_ship(self, ship_id):
        return self.ships.get(ship_id)

    def remove_ship(self, ship_id):
        if ship_id in self.ships:
            del self.ships[ship_id]

    def update_ship(self, ship_id, **kwargs):
        ship = self.ships.get(ship_id)
        if ship:
            ship.update(kwargs)

    def add_crew(self, name, position, ship_id):
        crew_id = len(self.crews) + 1
        crew = {"name": name, "position": position, "ship_id": ship_id}
        self.crews[crew_id] = crew
        return crew_id

    def get_crew(self, crew_id):
        return self.crews.get(crew_id)

    def remove_crew(self, crew_id):
        if crew_id in self.crews:
            del self.crews[crew_id]

    def update_crew(self, crew_id, **kwargs):
        crew = self.crews.get(crew_id)
        if crew:
            crew.update(kwargs)
