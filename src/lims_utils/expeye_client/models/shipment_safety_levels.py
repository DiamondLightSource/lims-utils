from enum import StrEnum


class ShipmentSafetyLevels(StrEnum):
    GREEN = "Green"
    RED = "Red"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
