from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

import random

from .base import AbstractEventGenerator
from ..validations.factories import SimpleEventValidatorFactory
from ....models import EventCodes, InningContext


class SimpleEventGenerator(AbstractEventGenerator):
    def __init__(self, ranges: List[Tuple[float, EventCodes]]):
        self._ranges = ranges
        self._event_validator_Factory = SimpleEventValidatorFactory()

    def next(self, inning_state: InningContext) -> EventCodes:
        next_event_code: Optional[EventCodes] = None

        rand = random.random()
        for probability, event_code in self._ranges:
            if rand <= probability:
                next_event_code = event_code
                break
            
        if next_event_code == None:
            raise ValueError('No Event Code was generated!')

        return self._event_validator_Factory.create(next_event_code).action(inning_state)
