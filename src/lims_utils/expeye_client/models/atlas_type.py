from enum import StrEnum


class AtlasType(StrEnum):
    ROI = "ROI"
    TILESCAN = "Tilescan"

    def __str__(self) -> str:
        return str(self.value)
