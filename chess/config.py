from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls, name=False):
        if name:
            return list(map(lambda c: c.name, cls))
        return list(map(lambda c: c.value, cls))

    @classmethod
    def dict(cls, reverse=False):
        if reverse is False:
            d = cls._member_map_
        else:
            d = cls._value2member_map_
        return d


class SlugName(ExtendedEnum):
    KNIGHT = "knight"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
