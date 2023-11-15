import random


class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 Tic Tac Toe board

    def print_board(self):
        for i in range(3):
            print("|".join(self.board[i * 3 : (i + 1) * 3]))
            if i < 2:
                print("-----")

    def make_move(self, position, symbol):
        if self.is_valid_move(position):
            self.board[position] = symbol
            return True
        return False

    def is_valid_move(self, position):
        if 0 <= position <= 8:
            return self.board[position] == " "
        return False

    def check_winner(self, symbol):
        # Check all winning conditions
        for i in range(3):
            # Check rows and columns
            if (
                self.board[i * 3]
                == self.board[i * 3 + 1]
                == self.board[i * 3 + 2]
                == symbol
            ) or (self.board[i] == self.board[i + 3] == self.board[i + 6] == symbol):
                return True
        # Check diagonals
        if (self.board[0] == self.board[4] == self.board[8] == symbol) or (
            self.board[2] == self.board[4] == self.board[6] == symbol
        ):
            return True
        return False

    def is_full(self):
        return " " not in self.board


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        try:
            position = int(input(f"Player {self.symbol}, enter your move (0-8): "))
        except ValueError:
            return False
        return board.make_move(position, self.symbol)


class BotPlayer(Player):
    def make_move(self, board):
        valid_moves = [i for i in range(9) if board.is_valid_move(i)]
        print(f"Valid moves: {valid_moves}")
        position = random.choice(valid_moves)
        print(f"BotPlayer {self.symbol} chooses position {position}")
        return board.make_move(position, self.symbol)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        while True:
            self.board.print_board()
            if not self.current_player.make_move(self.board):
                print("Invalid move, try again.")
                continue

            if self.board.check_winner(self.current_player.symbol):
                self.board.print_board()
                print(f"Player {self.current_player.symbol} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break

            self.switch_player()


# To play the game
num_human_players = input("How many human players? (1/2): ")
player1 = HumanPlayer("X")
player2 = BotPlayer("O")
if num_human_players == "1":
    player2 = BotPlayer("O")
elif num_human_players == "2":
    player2 = HumanPlayer("O")
else:
    print("Invalid input, defaulting to 1 human player.")
game = Game(player1, player2)
game.play()
