from enum import StrEnum


class RobotActionOutActionTypeType0(StrEnum):
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
