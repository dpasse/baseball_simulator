from typing import List, Set
from .base import AbstractBaseEvent

from ...poco import EventCodes


class SingleBase(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.Error, EventCodes.ShortSingle])

    def action(self, bases: List[int]) -> List[int]:
        return [1] + bases

class MediumSingle(SingleBase):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.MediumSingle])

    def action(self, bases: List[int]) -> List[int]:
        return super().action(bases[:1] + [0] + bases[1:])

class LongSingle(SingleBase):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.LongSingle])

    def action(self, bases: List[int]) -> List[int]:
        return super().action([0] + bases)
