from typing import List, Set
from abc import ABC, abstractproperty, abstractmethod

from ..poco import EventCodes


class AbstractBaseEvent(ABC):
    @abstractproperty
    def codes(self) -> Set[EventCodes]:
        pass

    @abstractmethod
    def action(self, bases: List[int]) -> List[int]:
        pass

class Empty(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([])

    def action(self, bases: List[int]) -> List[int]:
        return bases
    
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

class TakeBase(SingleBase):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.Walk, EventCodes.HBP])

    def action(self, bases: List[int]) -> List[int]:
        if bases == [1, 1, 1]:
            return super().action(bases)

        for i, item in enumerate(bases):
            ## find first open base
            if not bool(item):
                bases[i] = 1
                break

        return bases
    
class Double(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.ShortDouble])

    def action(self, bases: List[int]) -> List[int]:
        return [0, 1] + bases
    
class LongDouble(Double):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.LongDouble])

    def action(self, bases: List[int]) -> List[int]:
        return super().action([0] + bases)

class Triple(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.Triple])

    def action(self, bases: List[int]) -> List[int]:
        return [0, 0, 1] + bases

class Homerun(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.HR])

    def action(self, bases: List[int]) -> List[int]:
        return [0, 0, 0] + bases
    
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

class MediumFlyBall(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.MediumFly])

    def action(self, bases: List[int]) -> List[int]:
        return bases[:2] + [0] + bases[2:]

class LongFlyBall(AbstractBaseEvent):
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.MediumFly])

    def action(self, bases: List[int]) -> List[int]:
        return  bases[:1] + [0] + bases[1:]

class SimpleBaseEventFactory:
    supported_event_types = [
        TakeBase,
        SingleBase,
        MediumSingle,
        LongSingle,
        Double,
        Triple,
        Homerun,
        GroundBall,
        GroundIntoDoublePlay,
        MediumFlyBall,
        LongFlyBall
    ]

    def __init__(self):
        self._mapping = {}
        for base_event_type in self.supported_event_types:
            base_event = base_event_type()
            for code in base_event.codes:
                self._mapping[code] = base_event

    def create(self, event_code: EventCodes) -> AbstractBaseEvent:
        return self._mapping[event_code] if event_code in self._mapping else Empty()
