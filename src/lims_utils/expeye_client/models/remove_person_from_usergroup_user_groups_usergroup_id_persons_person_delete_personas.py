from enum import StrEnum


class RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas(StrEnum):
    FEDID = "fedId"
    NUMERICID = "numericId"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
