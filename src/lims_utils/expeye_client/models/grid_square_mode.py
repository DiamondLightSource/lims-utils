from enum import StrEnum


class GridSquareMode(StrEnum):
    BRIGHT_FIELD = "Bright Field"
    BRIGHT_FIELD_AND_FLUORESCENT = "Bright Field and Fluorescent"
    FLUORESCENT = "Fluorescent"
    SINGLE_PARTICLE = "Single Particle"
    TOMOGRAPHY = "Tomography"

    def __str__(self) -> str:
        return str(self.value)
