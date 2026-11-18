from enum import StrEnum


class StateEnum(StrEnum):
    CANCELLED = "Cancelled"
    CLOSED = "Closed"
    OPEN = "Open"

    def __str__(self) -> str:
        return str(self.value)
