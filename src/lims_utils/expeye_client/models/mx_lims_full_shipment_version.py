from enum import StrEnum


class MxLimsFullShipmentVersion(StrEnum):
    VALUE_0 = "0.6.12"
    VALUE_1 = "0.6.13"

    def __str__(self) -> str:
        return str(self.value)
