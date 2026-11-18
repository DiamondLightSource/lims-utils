from enum import StrEnum


class RemovePersonFromUsergroupPersonas(StrEnum):
    FEDID = "fedId"
    NUMERICID = "numericId"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
