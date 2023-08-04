from typing import Optional

from .bases import Bases
from .calculators.outs import OutsCalculator
from ..models import EventCodes, InningContext


class Inning():
    def __init__(self) -> None:
        self._bases = Bases([0, 0, 0])
        self._runs: int = 0
        self._outs: int = 0

        self._outs_calculator = OutsCalculator()

    @property
    def current_state(self) -> InningContext:
        return InningContext(
            self._outs,
            self._bases.current_state,
            self._runs
        )

    def is_over(self) -> bool:
        return self._outs >= 3

    def execute(self, event_code: EventCodes) -> None:
        self._outs += self._outs_calculator.calculate(event_code)
        if not self.is_over():
            self._runs += self._bases.play_event(event_code)

    def set_state(self, state: InningContext) -> None:
        self._bases = Bases(state.bases)
        self._runs: int = state.runs
        self._outs: int = state.outs
    