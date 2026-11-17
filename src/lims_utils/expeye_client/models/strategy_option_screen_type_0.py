from enum import StrEnum


class StrategyOptionScreenType0(StrEnum):
    ALL = "all"
    BEST = "best"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
