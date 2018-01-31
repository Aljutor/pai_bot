from enum import Enum

class StateId(Enum):
    Start   = 0
    Math    = 1
    XO      = 2
    XO_5    = 3
    Matches = 4


class UserState:
    state_id = StateId.Start

    matches_game = None
    xo_game      = None
    xo5_game     = None