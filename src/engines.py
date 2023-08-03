from .poco import BatterStats
from .events.hitting import AbstractEventGeneratorFactory, \
                            EventGeneratorFactory
from .state import Inning


class InningSimulator():
    def __init__(self, \
                 batter: BatterStats, \
                 event_generator_factory: AbstractEventGeneratorFactory = EventGeneratorFactory()):
        self._batter = batter
        self._event_generator = event_generator_factory.create(self._batter.likelihoods())

    def play(self):
        inning = Inning()
        while not inning.is_over():
            next_event = self._event_generator.next(inning.current_state)
            inning.execute(
                self._batter.key,
                next_event
            )

        return inning
