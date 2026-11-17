from enum import StrEnum


class GridInfoOptionalOrientationType0(StrEnum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
