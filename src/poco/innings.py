from typing import List
from dataclasses import dataclass

from .event_codes import EventCodes


@dataclass
class InningContext:
    outs: int
    bases: List[int]
    runs: int

@dataclass
class InningHistory():
    scenario: InningContext
    batter: str
    event: EventCodes
    desc: str
