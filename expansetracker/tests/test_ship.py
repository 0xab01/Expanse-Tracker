import unittest
from ship import Ship

class ShipTestCase(unittest.TestCase):
    def setUp(self):
        self.ship = Ship("Rocinante", "Corvette", "James Holden")

    def test_ship_creation(self):
        self.assertEqual(self.ship.name, "Rocinante")
        self.assertEqual(self.ship.ship_type, "Corvette")
        self.assertEqual(self.ship.captain, "James Holden")

    def test_ship_update(self):
        self.ship.update_name("Roci")
        self.ship.update_captain("Naomi Nagata")
        self.assertEqual(self.ship.name, "Roci")
        self.assertEqual(self.ship.captain, "Naomi Nagata")

if __name__ == "__main__":
    unittest.main()
