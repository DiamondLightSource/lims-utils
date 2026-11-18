from enum import StrEnum


class Combinator(StrEnum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
