import random


class Ship:
    def __init__(self, length):
        self.length = length
        self.hits = [False] * length
        self.coords = []

    def is_sunk(self):
        return all(self.hits)


class Mine:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.exploded = False


class Board:
    def __init__(self):
        self.grid_size = 10
        self.ships = []
        self.mines = []
        self.grid_player = [[' '] * self.grid_size for _ in range(self.grid_size)]
        self.grid_opponent = [[' '] * self.grid_size for _ in range(self.grid_size)]
        self.shots_taken = set()

    def place_ship(self, ship, row, col, orientation):
        if orientation == 'h':
            if col + ship.length > self.grid_size:
                return False
            for i in range(ship.length):
                if self.grid_player[row][col + i] != ' ':
                    return False
            for i in range(ship.length):
                self.grid_player[row][col + i] = 'X'
                ship.coords.append((row, col + i))
        elif orientation == 'v':
            if row + ship.length > self.grid_size:
                return False
            for i in range(ship.length):
                if self.grid_player[row + i][col] != ' ':
                    return False
            for i in range(ship.length):
                self.grid_player[row + i][col] = 'X'
                ship.coords.append((row + i, col))
        self.ships.append(ship)
        return True

    def place_mine(self, row, col):
        if self.grid_player[row][col] != ' ':
            return False
        self.mines.append(Mine(row, col))
        self.grid_player[row][col] = 'O'
        return True

    def display_player_board(self):
        print("  A B C D E F G H I J")
        for i in range(self.grid_size):
            print(f"{i + 1:2d}", end=' ')
            for j in range(self.grid_size):
                print(self.grid_player[i][j], end=' ')
            print()

    def display_opponent_board(self):
        print("  A B C D E F G H I J")
        for i in range(self.grid_size):
            print(f"{i + 1:2d}", end=' ')
            for j in range(self.grid_size):
                if (i, j) in self.shots_taken:
                    print(self.grid_opponent[i][j], end=' ')
                else:
                    print(' ', end=' ')
            print()

    def player_shot(self, row, col):
        if (row, col) in self.shots_taken:
            return None
        self.shots_taken.add((row, col))
        if self.grid_opponent[row][col] == 'X':
            self.grid_opponent[row][col] = 'H'
            return "Hit"
        elif self.grid_opponent[row][col] == 'O':
            self.grid_opponent[row][col] = 'X'
            return "Mine"
        else:
            self.grid_opponent[row][col] = 'M'
            return "Miss"

    def opponent_shot(self):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if self.grid_player[row][col] in [' ', 'X', 'O']:
                if self.grid_player[row][col] == 'X':
                    self.grid_player[row][col] = 'H'
                    return row, col, "Hit"
                elif self.grid_player[row][col] == 'O':
                    self.grid_player[row][col] = 'X'
                    self.explode(row, col)
                    return row, col, "Mine"
                else:
                    self.grid_player[row][col] = 'M'
                    return row, col, "Miss"

    def explode(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                r, c = row + i, col + j
                if 0 <= r < self.grid_size and 0 <= c < self.grid_size:
                    if self.grid_player[r][c] == 'X':
                        self.grid_player[r][c] = 'H'
                    elif self.grid_player[r][c] == ' ':
                        self.grid_player[r][c] = 'M'


class Game:
    def __init__(self):
        self.board = Board()
        self.opponent_board = Board()
        self.place_ships_randomly(self.board)
        self.place_ships_randomly(self.opponent_board)
        self.place_mines_randomly(self.board)
        self.place_mines_randomly(self.opponent_board)

    def place_ships_randomly(self, board):
        ships = [
            Ship(4),
            Ship(3),
            Ship(3),
            Ship(2),
            Ship(2),
            Ship(2),
            Ship(1),
            Ship(1),
            Ship(1),
            Ship(1)
        ]
        for ship in ships:
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                orientation = random.choice(['h', 'v'])
                if self.valid_placement(board, row, col, ship.length, orientation):
                    board.place_ship(ship, row, col, orientation)
                    break

    def place_mines_randomly(self, board):
        for _ in range(2):
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if board.place_mine(row, col):
                    break

    def valid_placement(self, board, row, col, length, orientation):
        if orientation == 'h':
            if col + length > board.grid_size:
                return False
            for i in range(-1, length + 1):
                for j in range(-1, 2):
                    if 0 <= row + j < board.grid_size and 0 <= col + i < board.grid_size:
                        if board.grid_player[row + j][col + i] != ' ':
                            return False
        elif orientation == 'v':
            if row + length > board.grid_size:
                return False
            for i in range(-1, 2):
                for j in range(-1, length + 1):
                    if 0 <= row + j < board.grid_size and 0 <= col + i < board.grid_size:
                        if board.grid_player[row + j][col + i] != ' ':
                            return False
        return True

    def play(self):
        while self.board.ships and self.opponent_board.ships:
            print("Your Board:")
            self.board.display_player_board()
            print("\nOpponent's Board:")
            self.opponent_board.display_opponent_board()
            row, col = self.get_player_input()
            result = self.opponent_board.player_shot(row, col)
            if result:
                print(result)
                if result == "Mine":
                    self.explode_mine(self.opponent_board, row, col)
            else:
                print("Already shot there!")
            print("\nYour Board after opponent's shot:")
            opp_row, opp_col, opp_result = self.board.opponent_shot()
            self.board.display_player_board()
            print(f"Opponent shot at {opp_row + 1}, {chr(opp_col + ord('A'))}: {opp_result}")
            if opp_result == "Mine":
                self.explode_mine(self.board, opp_row, opp_col)
            input("Press Enter to continue...")
        if not self.board.ships:
            print("You lost!")
        else:
            print("Congratulations! You sank all the opponent's ships.")

    def explode_mine(self, board, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                r, c = row + i, col + j
                if 0 <= r < board.grid_size and 0 <= c < board.grid_size:
                    if board.grid_player[r][c] == 'X':
                        board.grid_player[r][c] = 'H'
                    elif board.grid_player[r][c] == ' ':
                        board.grid_player[r][c] = 'M'

    def get_player_input(self):
        while True:
            try:
                row = int(input("Enter row (1-10): ")) - 1
                col = ord(input("Enter column (A-J): ").upper()) - ord('A')
                if 0 <= row < 10 and 0 <= col < 10:
                    return row, col
                else:
                    print("Invalid input. Please enter a valid row and column.")
            except ValueError:
                print("Invalid input. Please enter a valid row and column.")


if __name__ == "__main__":
    game = Game()
    game.play()
