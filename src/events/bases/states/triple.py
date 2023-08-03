from typing import List, Set
from .base import AbstractBaseEvent

from ....poco import EventCodes


class Triple(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.Triple])

    def action(self, bases: List[int]) -> List[int]:
        return [0, 0, 1] + bases
