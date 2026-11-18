from enum import StrEnum


class GridInfoInOrientationType0(StrEnum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
