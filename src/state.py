from typing import List, Optional

from .events.bases import SimpleBaseEventFactory
from .poco import EventCodes, InningContext, InningHistory


class RunsCalculator:
    def calculate(self, bases: List[int]) -> int:
        return sum(bases[3:]) if len(bases) > 2 else 0

class Bases():
    def __init__(self, scenario: Optional[List[int]] = None) -> None:
        self._bases = (scenario if scenario else [0, 0, 0]).copy()
        
        self._base_event_factory = SimpleBaseEventFactory()
        self._calculator = RunsCalculator()

    @property
    def current_state(self) -> List[int]:
        return self._bases.copy()

    def play_event(self, event_code: EventCodes) -> int:
        bases = self._base_event_factory \
            .create(event_code) \
            .action(self._bases.copy())

        self._bases = bases[:3]
        return self._calculator.calculate(bases)

class OutsCalculator:
    def __init__(self):
        self._mapping = {
            EventCodes.GIDP: 2,
            EventCodes.Strikeout: 1,
            EventCodes.ShortFly: 1,
            EventCodes.MediumFly: 1,
            EventCodes.LongFly: 1,
            EventCodes.LineDriveInfieldFly: 1,
            EventCodes.NormalGroundBall: 1,
            EventCodes.NoAdvanceGroundBall: 1,
        }

    def calculate(self, event_code: EventCodes):
        if event_code in self._mapping:
            return self._mapping[event_code]
        
        return 0

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
