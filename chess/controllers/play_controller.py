from chess.controllers.valid_moves import FindNextMove
from chess.config import SlugName
from chess.serializers.play_serializer import PlaySerializer


class PlayController():

    def find_next_move(self, data: dict, slug: str) -> list[str]:
        get_move = FindNextMove(position_data=data)
        knight_move = get_move.get_valid_moves_knight(get_move.knight_position)
        bishop_move = get_move.get_valid_moves_bishop(get_move.bishop_position)
        rook_move = get_move.get_valid_moves_rook(get_move.rook_position)
        queen_move = get_move.get_valid_moves_queen(get_move.queen_position)

        if slug == SlugName.ROOK.value:
            invalid_moves = set(queen_move).union(set(bishop_move)).union(set(knight_move))
            valid_moves = [move for move in rook_move if move not in invalid_moves]
        if slug == SlugName.KNIGHT.value:
            invalid_moves = set(queen_move).union(set(bishop_move)).union(set(rook_move))
            valid_moves = [move for move in knight_move if move not in invalid_moves]
        if slug == SlugName.BISHOP.value:
            invalid_moves = set(queen_move).union(set(knight_move)).union(set(rook_move))
            valid_moves = [move for move in bishop_move if move not in invalid_moves]
        if slug == SlugName.QUEEN.value:
            invalid_moves = set(knight_move).union(set(bishop_move)).union(set(rook_move))
            valid_moves = [move for move in queen_move if move not in invalid_moves]

        formatted_response = PlaySerializer(valid_moves).data

        return formatted_response
