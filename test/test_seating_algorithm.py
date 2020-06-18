import unittest
import sys

sys.path.insert(0, '../')
from src import seat_utils


class SeatingAlgoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.seat_structure = [[2, 3], [3, 4], [3, 2], [4, 3]]

    def test_assign_seats(self):
        self.assertEqual(True, seat_utils.Seat.is_valid(self.seat_structure, 36))
