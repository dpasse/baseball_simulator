from typing import List, Set
from abc import ABC, abstractproperty, abstractmethod

from ....poco import EventCodes


class AbstractBaseEvent(ABC):
    @abstractproperty
    def codes(self) -> Set[EventCodes]:
        pass

    @abstractmethod
    def action(self, bases: List[int]) -> List[int]:
        pass