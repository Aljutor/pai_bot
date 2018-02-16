from enum import Enum

class StateId(Enum):
    Start   = 0
    Talk    = 1
    XO_3    = 2
    XO_5    = 3
    Matches = 4
    Translate = 5


class UserState:
    state_id = StateId.Start

    matches_game = None
    xo3_game     = None
    xo5_game     = None