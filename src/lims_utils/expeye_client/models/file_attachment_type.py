from enum import StrEnum


class FileAttachmentType(StrEnum):
    LOG = "log"
    PARAMS = "params"
    PIA = "pia"
    RECIP = "recip"
    SNAPSHOT = "snapshot"
    WARNING = "warning"
    XY = "xy"

    def __str__(self) -> str:
        return str(self.value)
