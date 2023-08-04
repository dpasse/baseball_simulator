from typing import List, Set
from .base import AbstractBaseEvent

from ....poco import EventCodes


class Empty(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return { }

    def action(self, bases: List[int]) -> List[int]:
        return bases
