import unittest
from expanse import Expanse

class ExpanseTestCase(unittest.TestCase):
    def setUp(self):
        self.expanse = Expanse()

    def test_add_ship(self):
        ship_id = self.expanse.add_ship("Rocinante", "Corvette", "James Holden")
        self.assertEqual(ship_id, 1)

    def test_get_ship(self):
        self.expanse.add_ship("Rocinante", "Corvette", "James Holden")
        ship = self.expanse.get_ship(1)
        self.assertEqual(ship["name"], "Rocinante")
        self.assertEqual(ship["type"], "Corvette")
        self.assertEqual(ship["captain"], "James Holden")

    def test_remove_ship(self):
        self.expanse.add_ship("Rocinante", "Corvette", "James Holden")
        self.expanse.remove_ship(1)
        self.assertIsNone(self.expanse.get_ship(1))

    def test_update_ship(self):
        self.expanse.add_ship("Rocinante", "Corvette", "James Holden")
        self.expanse.update_ship(1, name="Roci", captain="Naomi Nagata")
        ship = self.expanse.get_ship(1)
        self.assertEqual(ship["name"], "Roci")
        self.assertEqual(ship["captain"], "Naomi Nagata")

if __name__ == "__main__":
    unittest.main()
