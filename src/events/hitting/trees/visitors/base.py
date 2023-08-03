from abc import ABC, abstractmethod


class AbstractVisitor(ABC):
    @abstractmethod
    def visit_leaf(self, leaf):
        pass

    @abstractmethod
    def visit_tree(self, tree):
        pass
