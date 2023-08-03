from abc import ABC, abstractmethod
from .tree import EventVariableTree, EventVariableComposite
from ....poco import EventCodes


class AbstractEventTreeFactory(ABC):
    @abstractmethod
    def create(self, likelihoods) -> EventVariableTree:
        pass
