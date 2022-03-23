import unittest
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):

    def test_check_winner(self):
        game = TicTacGame()
        winner_boards = (
            (('X', '-', 'O',
              'X', 'O', 'O',
              'X', '-', '-'), True),

            (('X', '-', 'O',
              'X', 'O', 'O',
              'X', '-', '-'), True),

            (('X', '0', 'O',
              '0', 'X', 'X',
              'O', 'X', '0'), False),

            (('X', '0', 'O',
              '0', 'X', 'X',
              'O', 'X', '0'), False)
        )
        for board in winner_boards:
            game.board = board[0]
            self.assertEqual(game.check_winner(), board[1])

    def test_validate_input(self):
        game = TicTacGame()
        board = (
            '-', '-', 'O',
            'X', 'O', '-',
            '-', '-', '-'
        )
        game.board = board
        invalid_input = ('AdAs', '999', '@^&@*', '2')
        valid_input = ('0', '5', '8')

        for i in invalid_input:
            game.board = board
            self.assertFalse(game.validate_input(i))

        for i in valid_input:
            game.board = board
            self.assertTrue(game.validate_input(i))

    def test_play_turn(self):
        game = TicTacGame()
        board = [
            '-', '-', 'O',
            'X', 'O', '-',
            '-', '-', '-'
        ]
        game.board = board
        expected_board = [
            '-', '-', 'O',
            'X', 'O', '-',
            '-', '-', 'X'
        ]

        game.play_turn('8')
        self.assertEqual(game.board, expected_board)


if __name__ == "__main__":
    unittest.main()
