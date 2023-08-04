from typing import List, Optional

from .bases import Bases
from .calculators.outs import OutsCalculator
from ..poco import EventCodes, InningContext, InningHistory


class Inning():
    def __init__(self, scenario: Optional[InningContext] = None) -> None:
        self._bases = Bases(scenario.bases if scenario else [0, 0, 0])
        self._runs: int = scenario.runs if scenario else 0
        self._outs: int = scenario.outs if scenario else 0

        self._outs_calculator = OutsCalculator()
        self._history: List[InningHistory] = []

    @property
    def history(self) -> List[InningHistory]:
        return self._history

    def is_over(self) -> bool:
        return self._outs >= 3
    
    @property
    def current_state(self) -> InningContext:
        return InningContext(
            self._outs,
            self._bases.current_state,
            self._runs
        )

    def execute(self, key: str, event_code: EventCodes) -> None:
        self._outs += self._outs_calculator.calculate(event_code)
        if not self.is_over():
            self._runs += self._bases.play_event(event_code)
            self._history.append(InningHistory(
                self.current_state,
                key,
                event_code,
                event_code.name
            ))
