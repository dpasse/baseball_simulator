from typing import List
from abc import ABC
from dataclasses import dataclass
from enum import Enum

import math


class EventCodes(Enum):
    Strikeout = 1
    Walk = 2
    HBP = 3
    Error = 4
    LongSingle = 5
    MediumSingle = 6
    ShortSingle = 7
    ShortDouble = 8
    LongDouble = 9
    Triple = 10
    HR = 11
    GIDP = 12
    NormalGroundBall = 13
    NoAdvanceGroundBall = 14
    LineDriveInfieldFly = 15
    LongFly = 16
    MediumFly = 17
    ShortFly = 18
    ParentEvent = 100

@dataclass
class InningContext:
    outs: int
    bases: List[int]
    runs: int

@dataclass
class InningHistory():
    scenario: InningContext
    batter: str
    event: EventCodes
    desc: str

class PlayerStats(ABC):
    def __init__(self, key: str, data: dict, likelihood_keys: List[str]) -> None:
        self.__key = key
        self.__data = data.copy()
        self.__likelihood_keys = likelihood_keys.copy()

    @property
    def key(self) -> str:
        return self.__key

    def likelihoods(self) -> dict:
        likelihood = {}
        for key in self.__likelihood_keys:
            likelihood[key] = self.__data[key] / self.__data['PA']

        return likelihood

class BatterStats(PlayerStats):
    def __init__(self, key: str, data: dict):
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

        super().__init__(key, given_data, [
            'E',
            'Outs',
            'K',
            'BB',
            'HBP',
            '1B',
            '2B',
            '3B',
            'HR'
        ])

    @staticmethod
    def create(key: str, data: dict):
        return BatterStats(key, data)
