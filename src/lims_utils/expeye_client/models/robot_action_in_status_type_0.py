from enum import StrEnum


class RobotActionInStatusType0(StrEnum):
    COMMANDNOTSENT = "COMMANDNOTSENT"
    CRITICAL = "CRITICAL"
    EPICSFAIL = "EPICSFAIL"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
