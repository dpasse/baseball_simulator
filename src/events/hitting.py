from typing import List, Tuple, Optional, Set
from abc import ABC, abstractmethod, abstractproperty
from collections import Iterable

import math
import random

from ..poco import EventCodes, InningContext


class AbstractVisitor(ABC):
    @abstractmethod
    def visit_leaf(self, leaf):
        pass
    
    @abstractmethod
    def visit_tree(self, tree):
        pass

class EventVariableComposite():
    def __init__(self, event_code: EventCodes, probability: float = 1):
        self._event_code = event_code
        self._probability = probability

        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    @property
    def event_code(self) -> EventCodes:
        return self._event_code
    
    @property
    def probability(self) -> bool:
        if self.parent:
            return self.parent.probability * self._probability

        return self._probability
    
    def accept(self, visitor: AbstractVisitor):
        visitor.visit_leaf(self)
    
    def __repr__(self) -> str:
        return '{0} - {1}'.format(self.event_code, self.probability)

class EventVariableTree(Iterable, EventVariableComposite):
    _members: List[EventVariableComposite] = []

    def __init__(self, members: List[EventVariableComposite], probability = 1.0):
        self._members = members

        for member in self._members:
            member.parent = self
        
        super().__init__(EventCodes.ParentEvent, probability)

    def __iter__(self):
        return iter(self._members)
    
    def accept(self, visitor: AbstractVisitor):
        visitor.visit_tree(self)

        for node in self:
            node.accept(visitor)


class AbstractEventValidator:
    @abstractproperty
    def codes(self) -> Set[EventCodes]:
        pass

    @abstractmethod
    def action(self, inning_context: InningContext) -> EventCodes:
        pass

class EmptyValidator(AbstractEventValidator):
    def __init__(self, code: EventCodes):
        self._code = code

    @property
    def codes(self) -> Set[EventCodes]:
        return set([self._code])
    
    def action(self, _: InningContext) -> EventCodes:
        return self._code

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

class SimpleEventValidatorFactory:
    supported_validator_types = [
        DoublePlayValidator
    ]

    def __init__(self):
        self._mapping = {}
        for base_event_type in self.supported_validator_types:
            base_event = base_event_type()
            for code in base_event.codes:
                self._mapping[code] = base_event

    def create(self, event_code: EventCodes) -> AbstractEventValidator:
        return self._mapping[event_code] if event_code in self._mapping else EmptyValidator(event_code)

class AbstractEventGenerator(ABC):
    @abstractmethod
    def next(self, inning_state: InningContext):
        pass

class EventGenerator(AbstractEventGenerator):
    def __init__(self, ranges: List[Tuple[float, EventCodes]]):
        self._ranges = ranges
        self._event_validator_Factory = SimpleEventValidatorFactory()

    def next(self, inning_state: InningContext) -> EventCodes:
        next_event_code: Optional[EventCodes] = None

        rand = random.random()
        for probability, event_code in self._ranges:
            if rand <= probability:
                next_event_code = event_code
                break
            
        if next_event_code == None:
            raise ValueError('No Event Code was generated!')

        return self._event_validator_Factory.create(next_event_code).action(inning_state)
    
class GetProbabilityRanges(AbstractVisitor):
    def __init__(self):
        self._total = 0.0
        self._ranges = []

    @property
    def ranges(self):
        if len(self._ranges) == 0:
            return self._ranges
        
        _, last_event_code = self._ranges[-1]
        return self._ranges[:-1] + [(1.0, last_event_code)]

    def visit_leaf(self, leaf):
        self._total += leaf.probability
        self._ranges.append(
            (self._total, leaf.event_code)
        )
    
    def visit_tree(self, tree):
        pass

class AbstractEventTreeFactory(ABC):
    @abstractmethod
    def create(self, likelihoods) -> EventVariableTree:
        pass

class MathelticsEventTreeFactory(AbstractEventTreeFactory):
    def create(self, likelihoods) -> EventVariableTree:
        tree = EventVariableTree(
            members=[
                EventVariableComposite(
                    event_code=EventCodes.Error,
                    probability=likelihoods['E'],
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
                    probability=likelihoods['Outs'],
                ),
                EventVariableComposite(
                    event_code=EventCodes.Strikeout,
                    probability=likelihoods['K'],
                ),
                EventVariableComposite(
                    event_code=EventCodes.Walk,
                    probability=likelihoods['BB'],
                ),
                EventVariableComposite(
                    event_code=EventCodes.HBP,
                    probability=likelihoods['HBP'],
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
                    probability=likelihoods['1B'],
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
                    probability=likelihoods['2B'],
                ),
                EventVariableComposite(
                    event_code=EventCodes.Triple,
                    probability=likelihoods['3B'],
                ),
                EventVariableComposite(
                    event_code=EventCodes.HR,
                    probability=likelihoods['HR'],
                )
            ],
            probability=1.0
        )

        return tree
    
class AbstractEventGeneratorFactory:
    @abstractmethod
    def create(self, likelihoods) -> AbstractEventGenerator:
        pass

class EventGeneratorFactory(AbstractEventGeneratorFactory):
    def __init__(self, event_tree_factory: AbstractEventTreeFactory = MathelticsEventTreeFactory()):
        self._event_tree_factory = event_tree_factory

    def create(self, likelihoods) -> AbstractEventGenerator:
        event_tree = MathelticsEventTreeFactory().create(likelihoods)

        probability_ranges = GetProbabilityRanges()
        event_tree.accept(probability_ranges)

        return EventGenerator(probability_ranges.ranges)
