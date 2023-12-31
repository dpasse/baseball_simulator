from ..models import BatterStats, InningHistory
from ..events.hitting.generators import AbstractEventGenerator
from ..state import Inning


class InningSimulator():
    def __init__(self, event_generator: AbstractEventGenerator):
        self._event_generator = event_generator

    def play(self):
        inning = Inning()
        while not inning.is_over():
            next_event = self._event_generator.next(inning.current_state)
            inning.execute(next_event)

        return inning
