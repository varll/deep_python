class TicTacGame:

    def __init__(self):
        self.board = ['-'] * 9
        self.turn = 0
        self.player = 'X'

    def show_board(self):
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('----------')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('----------')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')
        print('----------')

    def check_winner(self):
        if self.board[0] == self.board[4] == self.board[8] != '-' or \
                self.board[2] == self.board[4] == self.board[6] != '-':
            return True

        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != '-' or \
                    self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] != '-':
                return True

        return False

    def check_draw(self):
        return self.turn == 9

    def validate_input(self, input_line):
        if not input_line.isnumeric():
            print('Введите число.')
            return False

        if int(input_line) > 8 or int(input_line) < 0:
            print('Введите число в диапазоне от 0 до 8.')
            return False

        if self.board[int(input_line)] != '-':
            print('Эта клетка занята, введите другое число.')
            return False

        return True

    def play_turn(self, input_line):
        self.board[int(input_line)] = self.player
        self.turn += 1

    def change_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def start_game(self):
        while True:
            self.show_board()
            input_line = input('Введите ход: ')
            if not self.validate_input(input_line):
                continue
            self.play_turn(input_line)

            if self.check_winner():
                self.show_board()
                print(f'Игра окончена. Игрок {self.player} победил!')
                break
            if self.check_draw():
                self.show_board()
                print('Ничья!')
                break

            self.change_player()


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
