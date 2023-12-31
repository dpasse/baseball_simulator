from typing import List, Set
from .base import AbstractBaseEvent

from ....models import EventCodes


class Empty(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set()

    def action(self, bases: List[int]) -> List[int]:
        return bases
