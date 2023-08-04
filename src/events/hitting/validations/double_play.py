from typing import Set, List

from .empty import EmptyValidator
from ....poco import EventCodes, InningContext


class DoublePlayValidator(EmptyValidator):
    def __init__(self):
        self._double_play_scenarios = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1]
        ]

        super().__init__(EventCodes.GIDP)
    
    def matches_a_scenario(self, bases: List[int]) -> bool:
        for scenario in self._double_play_scenarios:
            if bases == scenario:
                return True

        return False

    def action(self, inning_context: InningContext) -> EventCodes:
        if inning_context.outs == 2 or not self.matches_a_scenario(inning_context.bases):
            return EventCodes.NormalGroundBall
        
        return super().action(inning_context)
