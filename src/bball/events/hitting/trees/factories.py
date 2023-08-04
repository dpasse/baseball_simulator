from abc import ABC, abstractmethod
from .tree import EventVariableTree


class AbstractEventTreeFactory(ABC):
    @abstractmethod
    def create(self, likelihoods) -> EventVariableTree:
        pass
