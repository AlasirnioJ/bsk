from idlelib.debugger_r import frametable

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) >= 10:
            raise BowlingError()
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        is_spare = False
        is_strike = False
        for index, frame in enumerate(self._frames):
            if frame.is_spare():
                score += self._frames[index +1].get_first_throw()
            if frame.is_strike():
                if self._frames[index +1].is_strike():
                    score += self._frames[index +2].get_first_throw()
                score += self._frames[index + 1].score()
            score += frame.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
