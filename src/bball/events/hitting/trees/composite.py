from ....models import EventCodes
from .visitors.base import AbstractVisitor


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
    def probability(self) -> float:
        if self.parent:
            return self.parent.probability * self._probability

        return self._probability
    
    def accept(self, visitor: AbstractVisitor):
        visitor.visit_leaf(self)
    
    def __repr__(self) -> str:
        return '{0} - {1}'.format(self.event_code, self.probability)
