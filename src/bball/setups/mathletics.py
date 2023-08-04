from ..events.hitting.generators import AbstractEventGenerator, SimpleEventGenerator
from ..events.hitting import EventVariableComposite, EventVariableTree
from ..events.hitting.trees.visitors.probabilities import GetProbabilityRanges
from ..events.hitting.trees.factories import AbstractEventTreeFactory
from ..models.data import BatterLikelihoodData
from ..models import EventCodes, BatterStats


class MathleticsEventTreeFactory(AbstractEventTreeFactory):
    def create(self, likelihoods: BatterLikelihoodData) -> EventVariableTree:
        tree = EventVariableTree(
            members=[
                EventVariableComposite(
                    event_code=EventCodes.Error,
                    probability=likelihoods.E,
                ),
                EventVariableTree(
                    members=[
                        EventVariableTree(
                            members=[
                                EventVariableComposite(
                                    event_code=EventCodes.GIDP,
                                    probability=.5,
                                ),
                                EventVariableComposite(
                                    event_code=EventCodes.NormalGroundBall,
                                    probability=.5,
                                )
                            ],
                            probability=.538,
                        ),
                        EventVariableComposite(
                            event_code=EventCodes.LineDriveInfieldFly,
                            probability=.153,
                        ),
                        EventVariableTree(
                            members=[
                                EventVariableComposite(
                                    event_code=EventCodes.LongFly,
                                    probability=.2,
                                ),
                                EventVariableComposite(
                                    event_code=EventCodes.MediumFly,
                                    probability=.5,
                                ),
                                EventVariableComposite(
                                    event_code=EventCodes.ShortFly,
                                    probability=.3,
                                )
                            ],
                            probability=.309,
                        ),
                    ],
                    probability=likelihoods.Outs,
                ),
                EventVariableComposite(
                    event_code=EventCodes.Strikeout,
                    probability=likelihoods.K,
                ),
                EventVariableComposite(
                    event_code=EventCodes.Walk,
                    probability=likelihoods.BB,
                ),
                EventVariableComposite(
                    event_code=EventCodes.HBP,
                    probability=likelihoods.HBP,
                ),
                EventVariableTree(
                    members=[
                        EventVariableComposite(
                            event_code=EventCodes.LongSingle,
                            probability=.3,
                        ),
                        EventVariableComposite(
                            event_code=EventCodes.MediumSingle,
                            probability=.5,
                        ),
                        EventVariableComposite(
                            event_code=EventCodes.ShortSingle,
                            probability=.2,
                        )
                    ],
                    probability=likelihoods.Singles,
                ),
                EventVariableTree(
                    members=[
                        EventVariableComposite(
                            event_code=EventCodes.ShortDouble,
                            probability=.8,
                        ),
                        EventVariableComposite(
                            event_code=EventCodes.LongDouble,
                            probability=.2,
                        ),
                    ],
                    probability=likelihoods.Doubles,
                ),
                EventVariableComposite(
                    event_code=EventCodes.Triple,
                    probability=likelihoods.Triples,
                ),
                EventVariableComposite(
                    event_code=EventCodes.HR,
                    probability=likelihoods.HR,
                )
            ],
            probability=1.0
        )

        return tree

class MathleticsSimpleEventGenerator():
    def __init__(self):
        self._event_tree_factory = MathleticsEventTreeFactory()

    def create(self, batter: BatterStats) -> AbstractEventGenerator:
        probability_ranges = GetProbabilityRanges()
        MathleticsEventTreeFactory() \
            .create(batter.likelihoods) \
            .accept(probability_ranges)

        return SimpleEventGenerator(probability_ranges.ranges)
