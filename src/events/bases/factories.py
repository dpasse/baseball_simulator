from .base import AbstractBaseEvent
from .empty import Empty
from .take_base import TakeBase
from .singles import SingleBase, MediumSingle, LongSingle
from .doubles import Double, LongDouble
from .triple import Triple
from .homerun import Homerun
from .grounders import GroundBall, GroundIntoDoublePlay
from .fly_ball import MediumFlyBall, LongFlyBall

from ...poco import EventCodes


SUPPORTED_BASE_TYPES = [
    ## positive
    TakeBase,
    SingleBase,
    MediumSingle,
    LongSingle,
    Double,
    LongDouble,
    Triple,
    Homerun,

    ## negative
    GroundBall,
    GroundIntoDoublePlay,
    MediumFlyBall,
    LongFlyBall
]

class SimpleBaseEventFactory:
    def __init__(self):
        self._mapping = {}
        for base_event_type in SUPPORTED_BASE_TYPES:
            base_event = base_event_type()
            for code in base_event.codes:
                self._mapping[code] = base_event

    def create(self, event_code: EventCodes) -> AbstractBaseEvent:
        return self._mapping[event_code] if event_code in self._mapping else Empty()
