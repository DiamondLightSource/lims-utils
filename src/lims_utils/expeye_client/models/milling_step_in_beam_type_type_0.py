from enum import StrEnum


class MillingStepInBeamTypeType0(StrEnum):
    ELECTRON = "Electron"
    ION = "Ion"

    def __str__(self) -> str:
        return str(self.value)
