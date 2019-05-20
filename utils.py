from collections import namedtuple
from enum import Enum

Value = namedtuple("Value", ["name", "type", "is_id"])


class VarType(Enum):
    INT = "int"
    FLOAT = "float"
    STRING = "string"
