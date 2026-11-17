from enum import StrEnum


class MXMRRunBlobOutMapTypeType0(StrEnum):
    ANOMALOUS = "anomalous"
    DIFFERENCE = "difference"

    def __str__(self) -> str:
        return str(self.value)
