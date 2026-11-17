from enum import StrEnum


class CollectionMode(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
