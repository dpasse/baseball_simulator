from .base import AbstractEventValidator
from .empty import EmptyValidator
from .double_play import DoublePlayValidator

from ....poco import EventCodes

SUPPORTED_BASE_VALIDATOR_TYPES = [
    DoublePlayValidator,
]

class SimpleEventValidatorFactory:
    def __init__(self):
        self._mapping = {}
        for base_event_type in SUPPORTED_BASE_VALIDATOR_TYPES:
            base_event = base_event_type()
            for code in base_event.codes:
                self._mapping[code] = base_event

    def create(self, event_code: EventCodes) -> AbstractEventValidator:
        return self._mapping[event_code] if event_code in self._mapping else EmptyValidator(event_code)
