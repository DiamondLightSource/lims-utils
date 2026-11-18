from enum import StrEnum


class SafetyLevels(StrEnum):
    GREEN = "GREEN"
    RED = "RED"
    YELLOW = "YELLOW"

    def __str__(self) -> str:
        return str(self.value)
