from typing import List, Set
from .base import AbstractBaseEvent

from ....poco import EventCodes


class TakeBase(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.Walk, EventCodes.HBP])

    def action(self, bases: List[int]) -> List[int]:
        if bases == [1, 1, 1]:
            return [1] + bases

        for i, item in enumerate(bases):
            ## find first open base
            if not bool(item):
                bases[i] = 1
                break

        return bases
