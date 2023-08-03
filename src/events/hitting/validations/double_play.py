from typing import Set, List

from .base import AbstractEventValidator
from ....poco import EventCodes, InningContext


class DoublePlayValidator(AbstractEventValidator):
    def __init__(self):
        self._double_play_scenarios = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1]
        ]
    
    @property
    def codes(self) -> Set[EventCodes]:
        return set([EventCodes.GIDP])
    
    def matches_a_scenario(self, bases: List[int]) -> bool:
        for scenario in self._double_play_scenarios:
            if bases == scenario:
                return True

        return False

    def action(self, inning_context: InningContext) -> EventCodes:
        if inning_context.outs == 2 or not self.matches_a_scenario(inning_context.bases):
            return EventCodes.NormalGroundBall
        
        return EventCodes.GIDP
