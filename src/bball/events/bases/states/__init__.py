from .base import AbstractBaseEvent
from .empty import Empty
from .take_base import TakeBase
from .singles import SingleBase, MediumSingle, LongSingle
from .doubles import ShortDouble, LongDouble
from .triple import Triple
from .homerun import Homerun
from .grounders import GroundBall, GroundIntoDoublePlay
from .fly_ball import MediumFlyBall, LongFlyBall


SUPPORTED_BASE_TYPES = [
    ## positive
    TakeBase,
    SingleBase,
    MediumSingle,
    LongSingle,
    ShortDouble,
    LongDouble,
    Triple,
    Homerun,

    ## negative
    GroundBall,
    GroundIntoDoublePlay,
    MediumFlyBall,
    LongFlyBall
]
