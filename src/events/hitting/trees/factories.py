from abc import ABC, abstractmethod
from .tree import EventVariableTree, EventVariableComposite
from ....models import EventCodes


class AbstractEventTreeFactory(ABC):
    @abstractmethod
    def create(self, likelihoods) -> EventVariableTree:
        pass
