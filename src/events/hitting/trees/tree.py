from typing import List
from collections import Iterable
from .composite import EventVariableComposite
from .visitors.base import AbstractVisitor
from ....poco import EventCodes


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
