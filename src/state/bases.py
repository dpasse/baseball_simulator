from typing import List, Optional

from ..poco import EventCodes
from ..events import SimpleBaseEventFactory


class Bases():
    def __init__(self, scenario: Optional[List[int]] = None) -> None:
        self._bases = (scenario if scenario else [0, 0, 0]).copy()
        
        self._base_event_factory = SimpleBaseEventFactory()

    @property
    def current_state(self) -> List[int]:
        return self._bases.copy()

    def play_event(self, event_code: EventCodes) -> int:
        bases = self._base_event_factory \
            .create(event_code) \
            .action(self._bases.copy())

        self._bases, runs = bases[:3], bases[3:]
        return sum(runs)
