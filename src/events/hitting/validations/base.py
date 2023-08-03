from abc import ABC, abstractmethod, abstractproperty
from typing import Set, List
from ....poco import EventCodes, InningContext


class AbstractEventValidator:
    @abstractproperty
    def codes(self) -> Set[EventCodes]:
        pass

    @abstractmethod
    def action(self, inning_context: InningContext) -> EventCodes:
        pass
