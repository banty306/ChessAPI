from chess.config import SlugName


class FindNextMove:

    def __init__(self, position_data: dict):
        self.position = position_data
        self.knight_position = None
        self.queen_position = None
        self.bishop_position = None
        self.rook_position = None
        self.place_player()

    def convert_to_coordinates(self, notation):
        col_labels = "abcdefgh"
        col = notation[0].lower()
        row = int(notation[1:])
        col_index = col_labels.index(col) + 1
        return col_index, row

    def place_player(self):
        self.knight_position = self.convert_to_coordinates(self.position.get(SlugName.KNIGHT.value))
        self.queen_position = self.convert_to_coordinates(self.position.get(SlugName.QUEEN.value))
        self.rook_position = self.convert_to_coordinates(self.position.get(SlugName.ROOK.value))
        self.bishop_position = self.convert_to_coordinates(self.position.get(SlugName.BISHOP.value))

    def convert_to_chess_notation(self, move):
        col_labels = "ABCDEFGH"
        x, y = move
        return f"{col_labels[x - 1]}{y}"

    def get_valid_moves_knight(self, pos) -> list[str]:
        x, y = pos
        valid_moves = []

        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                valid_moves.append(self.convert_to_chess_notation((new_x, new_y)))

        return valid_moves

    def get_valid_moves_bishop(self, pos) -> list[str]:
        x, y = pos
        valid_moves = []
        bishop_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in bishop_moves:
            new_x, new_y = x, y
            while 1 <= new_x + dx <= 8 and 1 <= new_y + dy <= 8:
                new_x, new_y = new_x + dx, new_y + dy
                valid_moves.append(self.convert_to_chess_notation((new_x, new_y)))

        return valid_moves

    def get_valid_moves_rook(self, pos) -> list[str]:
        x, y = pos
        valid_moves = []

        rook_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in rook_moves:
            new_x, new_y = x, y
            while 1 <= new_x + dx <= 8 and 1 <= new_y + dy <= 8:
                new_x, new_y = new_x + dx, new_y + dy
                valid_moves.append(self.convert_to_chess_notation((new_x, new_y)))

        return valid_moves

    def get_valid_moves_queen(self, pos) -> list[str]:
        valid_moves = self.get_valid_moves_bishop(pos) + \
                      self.get_valid_moves_rook(pos)
        return valid_moves
