from typing import List, Optional

from .bases import Bases
from .calculators.outs import OutsCalculator
from ..models import EventCodes, InningContext, InningHistory


class Inning():
    def __init__(self, state: Optional[InningContext] = None) -> None:
        self._bases = Bases(state.bases if state else [0, 0, 0])
        self._runs: int = state.runs if state else 0
        self._outs: int = state.outs if state else 0
        self._outs_calculator = OutsCalculator()

    def is_over(self) -> bool:
        return self._outs >= 3
    
    @property
    def current_state(self) -> InningContext:
        return InningContext(
            self._outs,
            self._bases.current_state,
            self._runs
        )

    def execute(self, event_code: EventCodes) -> None:
        self._outs += self._outs_calculator.calculate(event_code)
        if not self.is_over():
            self._runs += self._bases.play_event(event_code)
