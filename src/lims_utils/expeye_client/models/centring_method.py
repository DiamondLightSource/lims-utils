from enum import StrEnum


class CentringMethod(StrEnum):
    DIFFRACTION = "diffraction"
    LOOP = "loop"
    OPTICAL = "optical"
    XRAY = "xray"

    def __str__(self) -> str:
        return str(self.value)
