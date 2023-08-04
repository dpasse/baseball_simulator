from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass

import math

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

class BatterStats:
    def __init__(self, key: str, data: BatterData) -> None:
        self._key = key
        self._data = data

    @property
    def key(self) -> str:
        return self._key

    @property
    def likelihoods(self) -> BatterLikelihoodData:
        return BatterLikelihoodData(self._data)
    
class AbstractBatterStatsFactory(ABC):
    @abstractmethod
    def create(self, key: str, data: dict) -> BatterStats:
        pass

class BasicBatterStatsFactory(AbstractBatterStatsFactory):
    def create(self, key: str, data: dict) -> BatterStats:
        given_data = data.copy()

        assert 'PA' in given_data or 'AB' in given_data
        for column in ('SH', 'SF', 'K', 'BB', 'HBP', '1B', '2B', '3B', 'HR'):
            assert column in given_data

        if not 'PA' in given_data:
            given_data['PA'] = sum(
                given_data[column] for column in ('BB', 'HBP', 'AB', 'SH', 'SF')
            )

        given_data['HITS'] = sum(
            given_data[column] for column in ('1B', '2B', '3B', 'HR')
        )

        given_data['E'] = math.floor(.018 * given_data['PA'])
        given_data['AtBats'] = sum(
            given_data[column] for column in ('AB', 'SF', 'SH')
        )
        given_data['Outs'] = given_data['AtBats'] - \
            sum(given_data[column] for column in ('HITS', 'E', 'K'))
        
        return BatterStats(key, BatterData(
            given_data['E'],
            given_data['Outs'],
            given_data['K'],
            given_data['BB'],
            given_data['HBP'],
            given_data['1B'],
            given_data['2B'],
            given_data['3B'],
            given_data['HR'],
            given_data['PA']
        ))
