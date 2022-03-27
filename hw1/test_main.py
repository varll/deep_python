import unittest
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):

    def test_check_winner(self):
        game = TicTacGame()
        winner_boards = (
            ('X', '-', 'O',
             'X', 'O', 'O',
             'X', '-', '-'),

            ('O', 'X', 'O',
             'O', 'X', 'O',
             '-', 'X', '-'),

            ('X', 'O', 'X',
             'O', 'O', 'X',
             'O', 'X', 'X'),

            ('O', 'O', 'O',
             '-', '-', 'X',
             '-', 'X', 'X'),

            ('-', 'X', '-',
             'O', 'O', 'O',
             'O', 'X', 'X'),

            ('-', 'O', '-',
             'X', 'X', '-',
             'O', 'O', 'O'),

            ('X', '-', '-',
             'O', 'X', 'O',
             'O', 'X', 'X'),

            ('X', 'O', 'O',
             'O', 'O', 'X',
             'O', 'X', '0')
        )

        boards = (
            ('X', 'O', 'O',
             'O', 'X', 'X',
             'O', 'X', '0'),

            ('-', 'O', '-',
             '-', '-', 'X',
             'O', 'X', '0'),

            ('-', '-', '-',
             '-', '-', '-',
             '-', '-', '-')
        )
        for board in winner_boards:
            game.board = board
            self.assertTrue(game.check_winner())

        for board in boards:
            game.board = board
            self.assertFalse(game.check_winner())

    def test_validate_input(self):
        game = TicTacGame()
        board1 = (
            'O', '-', 'X',
            '-', '-', 'X',
            '-', 'O', '-'
        )
        board2 = (
            '-', '-', '-',
            '-', '-', '-',
            '-', '-', '-'
        )
        invalid_input = ('AdAs', '999', '@^&@*', '4/3', '1.42', '\n', '2', '5', '-1', '9')
        valid_input = ('0', '1', '2', '3', '4', '5', '6', '7', '8')

        for i in invalid_input:
            game.board = board1
            self.assertFalse(game.validate_input(i))

        for i in valid_input:
            game.board = board2
            self.assertTrue(game.validate_input(i))

    def test_check_draw(self):
        game = TicTacGame()
        games = (
            (('O', 'X', 'X',
              'X', 'X', 'O',
              'O', 'O', 'X'), 9),

            (('O', 'X', 'X',
              'X', 'X', 'O',
              'O', 'O', 'O'), 9)
        )
        for test_game in games:
            game.board = test_game[0]
            game.turn = test_game[1]
            if not game.check_winner():
                self.assertTrue(game.check_draw())

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
