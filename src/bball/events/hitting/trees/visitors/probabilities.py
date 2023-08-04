from .base import AbstractVisitor


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
