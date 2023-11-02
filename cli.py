class InvalidMoveError(Exception):
    pass


class Board:
    def __init__(self, num_row, num_col):
        print("Board is initializing...")
        self.num_row = num_row
        self.num_col = num_col
        self.board = self.create_board()

    def create_board(self):
        print("Board is creating...")
        return [[" " for _ in range(self.num_col)] for _ in range(self.num_row)]

    def print(self):
        print("Board is printing...")
        for row in self.board:
            print(row)

    def set_move(self, row, col, player):
        print("Board is setting move...")
        if self.board[row][col] != " ":
            raise InvalidMoveError("Invalid move. Please enter valid numbers.")
        self.board[row][col] = player


class Game:
    def __init__(self, players=["X", "O"], num_row=3, num_col=3, starting_player="O"):
        print("Game is initializing...")
        self.players = players
        self.board = Board(num_row, num_col)
        self.current_player_idx = self.players.index(starting_player)

    def switch_player(self):
        print("Game is switching player...")
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def get_row_col(self, input_str):
        try:
            row, col = [int(x) for x in input_str.split(",")]
        except ValueError:
            raise InvalidMoveError(
                "Invalid move. Please enter numbers separated by a comma."
            )
        if row < 0 or row >= self.board.num_row or col < 0 or col >= self.board.num_col:
            raise InvalidMoveError("Invalid move. Please enter valid numbers.")
        return row, col

    def check_winner(self):
        """
        1. Check each row
        2. Check each column
        3. Check left to right diagonal
        4. Check right to left diagonal
        5. Return draw if board is full
        6. Game is not finished
        """
        for row in self.board.board:
            if len(set(row)) == 1:
                return row[0]

        for col_idx in range(self.board.num_col):
            column = [
                self.board.board[row_idx][col_idx]
                for row_idx in range(self.board.num_row)
            ]
            if len(set(column)) == 1:
                return column[0]

        left_to_right_diag = []
        for idx, row in enumerate(self.board.board):
            left_to_right_diag.append(row[idx])
        if len(set(left_to_right_diag)) == 1:
            return left_to_right_diag[0]

        right_to_left_diag = []
        for idx, row in enumerate(self.board.board):
            board_end_idx = self.board.num_row - 1
            right_to_left_diag.append(row[board_end_idx - idx])
        if len(set(right_to_left_diag)) == 1:
            return right_to_left_diag[0]

        all_marks = [mark for row in self.board.board for mark in row]
        if not " " in all_marks:
            return "draw"

        return " "

    def run(self):
        print("Game is running...")
        self.board.create_board()
        while True:
            self.board.print()
            if not self.process_player_move():
                continue
            winner = self.check_winner()
            if winner != " ":
                self.display_winner(winner)
                break
            self.switch_player()

    def process_player_move(self):
        input_str = input("Enter your move: ")
        try:
            row, col = self.get_row_col(input_str)
            self.board.set_move(row, col, self.players[self.current_player_idx])
        except InvalidMoveError as e:
            print(e)
            return False
        return True

    def display_winner(self, winner):
        self.board.print()
        if winner == "draw":
            print("It's a draw!")
        else:
            print(f"{winner} is the winner!")


if __name__ == "__main__":
    game = Game()
    game.run()
