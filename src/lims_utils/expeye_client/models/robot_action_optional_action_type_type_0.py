from enum import StrEnum


class RobotActionOptionalActionTypeType0(StrEnum):
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
