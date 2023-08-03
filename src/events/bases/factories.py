from .states import SUPPORTED_BASE_TYPES, AbstractBaseEvent, Empty
from ...poco import EventCodes


class SimpleBaseEventFactory:
    def __init__(self):
        self._mapping = {}
        for base_event_type in SUPPORTED_BASE_TYPES:
            base_event = base_event_type()
            for code in base_event.codes:
                self._mapping[code] = base_event

    def create(self, event_code: EventCodes) -> AbstractBaseEvent:
        return self._mapping[event_code] if event_code in self._mapping else Empty()
