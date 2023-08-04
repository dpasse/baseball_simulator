from typing import List, Set
from .base import AbstractBaseEvent

from ....models import EventCodes


class ShortDouble(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return { EventCodes.ShortDouble }

    def action(self, bases: List[int]) -> List[int]:
        return [0, 1] + bases

class LongDouble(ShortDouble):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.LongDouble])

    def action(self, bases: List[int]) -> List[int]:
        return super().action([0] + bases)
