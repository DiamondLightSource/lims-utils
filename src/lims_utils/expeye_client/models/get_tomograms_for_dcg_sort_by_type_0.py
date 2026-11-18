from enum import StrEnum


class GetTomogramsForDcgSortByType0(StrEnum):
    DATE = "date"
    GLOBALALIGNMENTQUALITY = "globalAlignmentQuality"

    def __str__(self) -> str:
        return str(self.value)
