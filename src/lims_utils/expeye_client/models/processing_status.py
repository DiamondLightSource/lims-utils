from enum import StrEnum


class ProcessingStatus(StrEnum):
    FAIL = "Fail"
    QUEUED = "Queued"
    RUNNING = "Running"
    SUBMITTED = "Submitted"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
