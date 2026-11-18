from enum import StrEnum


class Operator(StrEnum):
    BEGINSWITH = "beginsWith"
    BETWEEN = "between"
    CONTAINS = "contains"
    DOESNOTBEGINWITH = "doesNotBeginWith"
    DOESNOTCONTAIN = "doesNotContain"
    DOESNOTENDWITH = "doesNotEndWith"
    ENDSWITH = "endsWith"
    IN = "in"
    NOTBETWEEN = "notBetween"
    NOTIN = "notIn"
    NOTNULL = "notNull"
    NULL = "null"
    VALUE_0 = "="
    VALUE_1 = "!="
    VALUE_2 = "<"
    VALUE_3 = ">"
    VALUE_4 = "<="
    VALUE_5 = ">="

    def __str__(self) -> str:
        return str(self.value)
