from enum import StrEnum


class MillingStepOutBeamTypeType0(StrEnum):
    ELECTRON = "Electron"
    ION = "Ion"

    def __str__(self) -> str:
        return str(self.value)
