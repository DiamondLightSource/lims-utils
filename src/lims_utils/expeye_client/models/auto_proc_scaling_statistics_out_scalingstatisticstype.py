from enum import StrEnum


class AutoProcScalingStatisticsOutScalingstatisticstype(StrEnum):
    INNERSHELL = "innerShell"
    OUTERSHELL = "outerShell"
    OVERALL = "overall"

    def __str__(self) -> str:
        return str(self.value)
