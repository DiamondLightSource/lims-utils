from enum import StrEnum


class ReductionParameters(StrEnum):
    ALL = "All"
    FASTEST_DIMENSION = "Fastest Dimension"
    VALUE_2 = "1D"

    def __str__(self) -> str:
        return str(self.value)
