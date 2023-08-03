from typing import Set

from .base import AbstractEventValidator
from ....poco import EventCodes, InningContext


class EmptyValidator(AbstractEventValidator):
    def __init__(self, code: EventCodes):
        self._code = code

    @property
    def codes(self) -> Set[EventCodes]:
        return set([self._code])
    
    def action(self, _: InningContext) -> EventCodes:
        return self._code
