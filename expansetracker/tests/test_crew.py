import unittest
from crew import Crew

class CrewTestCase(unittest.TestCase):
    def setUp(self):
        self.crew = Crew("James Holden", "Captain", 1)

    def test_crew_creation(self):
        self.assertEqual(self.crew.name, "James Holden")
        self.assertEqual(self.crew.position, "Captain")
        self.assertEqual(self.crew.ship_id, 1)

    def test_crew_update(self):
        self.crew.update_position("Executive Officer")
        self.assertEqual(self.crew.position, "Executive Officer")

    def test_crew_change_ship(self):
        self.crew.change_ship(2)
        self.assertEqual(self.crew.ship_id, 2)

if __name__ == "__main__":
    unittest.main()
