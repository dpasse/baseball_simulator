from abc import ABC, abstractmethod

from ....models import EventCodes, InningContext


class AbstractEventGenerator(ABC):
    @abstractmethod
    def next(self, inning_state: InningContext) -> EventCodes:
        pass
