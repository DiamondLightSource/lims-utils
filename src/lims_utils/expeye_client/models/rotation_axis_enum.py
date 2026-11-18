from enum import StrEnum


class RotationAxisEnum(StrEnum):
    KAPPA = "Kappa"
    OMEGA = "Omega"
    PHI = "Phi"

    def __str__(self) -> str:
        return str(self.value)
