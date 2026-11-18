from enum import StrEnum


class MXMRRunBlobOptionalMapTypeType0(StrEnum):
    ANOMALOUS = "anomalous"
    DIFFERENCE = "difference"

    def __str__(self) -> str:
        return str(self.value)
