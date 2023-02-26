from enum import Enum


class State(Enum):
    STATE_INITIAL = 0,
    STATE_INT_SIGN = 1,
    STATE_INTEGER = 2,
    STATE_POINT = 3, # 左无整数
    STATE_POINT_WITHOUT_INT = 4,  # 左有整数
    STATE_FRACTION = 5,
    STATE_EXP = 6,
    STATE_EXP_SIGN = 7,
    STATE_EXP_NUMBER = 8,
    STATE_END = 9,


class Chartype(Enum):
    CHAR_NUMBER = 0,
    CHAR_EXP = 1,
    CHAR_POINT = 2,
    CHAR_SIGN = 3,
    CHAR_SPACE = 4,
    CHAR_ILLEGAL = 5


def isNumber(s: str) -> bool:
    def _toChartype(ch: str) -> Chartype:
        if ch.isdigit():
            return Chartype.CHAR_NUMBER
        elif ch.lower() == "e":
            return Chartype.CHAR_EXP
        elif ch == ".":
            return Chartype.CHAR_POINT
        elif ch == "+" or ch == "-":
            return Chartype.CHAR_SIGN
        elif ch == " ":
            return Chartype.CHAR_SPACE
        else:
            return Chartype.CHAR_ILLEGAL
    
    st_machine = {
        State.STATE_INITIAL: {
            Chartype.CHAR_SPACE: State.STATE_INITIAL,
            Chartype.CHAR_NUMBER: State.STATE_INTEGER,
            Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            Chartype.CHAR_SIGN: State.STATE_INT_SIGN
        },
        State.STATE_INT_SIGN: {
            Chartype.CHAR_NUMBER: State.STATE_INTEGER,
            Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
        },
        State.STATE_INTEGER: {
            Chartype.CHAR_NUMBER: State.STATE_INTEGER,
            Chartype.CHAR_EXP: State.STATE_EXP,
            Chartype.CHAR_POINT: State.STATE_POINT,
            Chartype.CHAR_SPACE: State.STATE_END
        },
        State.STATE_POINT: {
            Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            Chartype.CHAR_EXP: State.STATE_EXP,
            Chartype.CHAR_SPACE: State.STATE_END
        },
        State.STATE_POINT_WITHOUT_INT: {
            Chartype.CHAR_NUMBER: State.STATE_FRACTION
        },
        State.STATE_FRACTION: {
            Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            Chartype.CHAR_EXP: State.STATE_EXP,
            Chartype.CHAR_SPACE: State.STATE_END
        },
        State.STATE_EXP: {
            Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
        },
        State.STATE_EXP_SIGN: {
            Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
        },
        State.STATE_EXP_NUMBER: {
            Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            Chartype.CHAR_SPACE: State.STATE_END
        },
        State.STATE_END: {
            Chartype.CHAR_SPACE: State.STATE_END
        },
    }

    st=State.ST_INIT
    for c in s:
        ct=_toChartype(c)
        trans=st_machine[st]
        st=trans.get(ct)

        if(st == None):
            return False
        
    return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER, State.STATE_END]

