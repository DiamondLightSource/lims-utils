from enum import StrEnum


class FileType(StrEnum):
    DEBUG = "Debug"
    GRAPH = "Graph"
    INPUT = "Input"
    LOG = "Log"
    RESULT = "Result"

    def __str__(self) -> str:
        return str(self.value)
