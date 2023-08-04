from typing import List, Set
from .base import AbstractBaseEvent

from ....poco import EventCodes


class MediumFlyBall(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return { EventCodes.MediumFly }

    def action(self, bases: List[int]) -> List[int]:
        return bases[:2] + [0] + bases[2:]

class LongFlyBall(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return { EventCodes.MediumFly }

    def action(self, bases: List[int]) -> List[int]:
        return  bases[:1] + [0] + bases[1:]
