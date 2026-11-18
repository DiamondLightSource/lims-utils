from enum import StrEnum


class RobotActionInActionTypeType0(StrEnum):
    ANNEAL = "ANNEAL"
    DISPOSE = "DISPOSE"
    LASER = "LASER"
    LOAD = "LOAD"
    MOSAIC = "MOSAIC"
    STORE = "STORE"
    UNLOAD = "UNLOAD"
    WASH = "WASH"

    def __str__(self) -> str:
        return str(self.value)
