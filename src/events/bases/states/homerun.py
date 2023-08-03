from typing import List, Set
from .base import AbstractBaseEvent

from ....poco import EventCodes


class Homerun(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.HR])

    def action(self, bases: List[int]) -> List[int]:
        return [0, 0, 0] + bases
