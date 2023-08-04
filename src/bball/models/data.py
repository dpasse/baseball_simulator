from dataclasses import dataclass


@dataclass
class BatterData:
    E: int
    Outs: int
    K: int
    BB: int
    HBP: int
    Singles: int
    Doubles: int
    Triples: int
    HR: int
    PA: int

class BatterLikelihoodData:
    def __init__(self, data: BatterData):
        self._data = data

    def _compute(self, value: int) -> float:
        return value / float(self._data.PA)

    @property
    def E(self) -> float:
        return self._compute(self._data.E)
    
    @property
    def Outs(self) -> float:
        return self._compute(self._data.Outs)
    
    @property
    def K(self) -> float:
        return self._compute(self._data.K)
    
    @property
    def BB(self) -> float:
        return self._compute(self._data.BB)

    @property
    def HBP(self) -> float:
        return self._compute(self._data.HBP)
    
    @property
    def Singles(self) -> float:
        return self._compute(self._data.Singles)
    
    @property
    def Doubles(self) -> float:
        return self._compute(self._data.Doubles)
    
    @property
    def Triples(self) -> float:
        return self._compute(self._data.Triples)
    
    @property
    def HR(self) -> float:
        return self._compute(self._data.HR)
