from enum import StrEnum


class MillingStepInStatusType0(StrEnum):
    ABORTED = "Aborted"
    FAILED = "Failed"
    FINISHED = "Finished"

    def __str__(self) -> str:
        return str(self.value)
