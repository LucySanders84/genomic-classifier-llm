from dataclasses import dataclass
from re import Pattern


@dataclass
class SequenceSourceData:
    filename: str
    id_pattern: Pattern