from typing import List, Set
from .base import AbstractBaseEvent

from ...poco import EventCodes


class GroundBall(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.NormalGroundBall])

    def action(self, bases: List[int]) -> List[int]:
        if bases == [0, 1, 1]:
            return bases

        return bases[:1] + [0] + bases[1:]

class GroundIntoDoublePlay(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.GIDP])

    def action(self, bases: List[int]) -> List[int]:
        if bases == [1, 0, 0]:
            return [0, 0, 0]

        if bases == [1, 1, 0]:
            return [1, 0, 0]

        if bases == [1, 0, 1]:
            return [0, 0, 0] + [1]

        if bases == [1, 1, 1]:
            return [0, 1, 1]

        return bases
