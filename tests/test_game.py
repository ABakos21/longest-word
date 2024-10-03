from longest_word.game import Game
import string

class TestGame:
    def test_empty_is_invalid(self):

            new_game = Game()
            assert new_game.is_valid('') is False

    def test_is_valid(self):
            new_game = Game()
            test_grid = 'LOPHYBREE'
            test_word = 'HYPERBOLE'
            new_game.grid = list(test_grid)
            assert new_game.is_valid(test_word) is True
            assert new_game.grid == list(test_grid)

    def test_is_invalid(self):
            new_game = Game()
            test_grid = 'LOPHYBREE'
            test_word = 'BUTTERFLY'
            new_game.grid = list(test_grid)
            assert new_game.is_valid(test_word) is False
            assert new_game.grid == list(test_grid)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
