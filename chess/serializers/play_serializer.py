from rest_framework import serializers
from chess.config import SlugName


class PlaySerializer(serializers.BaseSerializer):

    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise serializers.ValidationError("Invalid data. Expected a dictionary.")

        positions = data.get("positions")

        if not positions or not isinstance(positions, dict):
            raise serializers.ValidationError("Invalid  or missing 'positions' data. Expected a dictionary.")

        valid_pieces = [SlugName.BISHOP.value, SlugName.QUEEN.value, SlugName.KNIGHT.value, SlugName.ROOK.value]
        internal_value = {}
        for piece in positions:
            piece_lower = piece.lower()
            if piece_lower in valid_pieces:
                position = positions[piece]
                if not isinstance(position, str) or len(position) != 2:
                    raise serializers.ValidationError(f"Invalid position for {piece}. Expected a 2-character string.")
                internal_value[piece_lower] = position

        return internal_value

    def to_representation(self, instance):
        return {
            "valid moves": instance
        }

