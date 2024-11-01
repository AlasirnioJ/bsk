import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_something(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f,game.get_frame_at(0))

    def test_something_error(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at,0)

    def test_game_with_11_frames(self):
       game = BowlingGame()
       game.add_frame(Frame(1,5))
       game.add_frame(Frame(3,6))
       game.add_frame(Frame(7,2))
       game.add_frame(Frame(3,6))
       game.add_frame(Frame(4,4))
       game.add_frame(Frame(5,3))
       game.add_frame(Frame(3,3))
       game.add_frame(Frame(4, 5))
       game.add_frame(Frame(8, 1))
       f = Frame(2, 6)
       game.add_frame(f)
       self.assertRaises(BowlingError, game.add_frame, Frame(1, 1))

    def test_calc_score(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(81, game.calculate_score())


    def test_calc_score_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(88, game.calculate_score())
    def test_calc_score_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(94, game.calculate_score())

    def test_calc_score_strike_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(4, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(103, game.calculate_score())

    def test_calc_score_2_strikes(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(112, game.calculate_score())

    def test_calc_score_2_spares(self):
        game = BowlingGame()
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(5, 5))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        f = Frame(2, 6)
        game.add_frame(f)
        self.assertEqual(98, game.calculate_score())
