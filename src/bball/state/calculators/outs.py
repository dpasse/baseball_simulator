from ...models import EventCodes


class OutsCalculator:
    def __init__(self):
        self._mapping = {
            EventCodes.GIDP: 2,
            EventCodes.Strikeout: 1,
            EventCodes.ShortFly: 1,
            EventCodes.MediumFly: 1,
            EventCodes.LongFly: 1,
            EventCodes.LineDriveInfieldFly: 1,
            EventCodes.NormalGroundBall: 1,
            EventCodes.NoAdvanceGroundBall: 1,
        }

    def calculate(self, event_code: EventCodes):
        if event_code in self._mapping:
            return self._mapping[event_code]
        
        return 0
