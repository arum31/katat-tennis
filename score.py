from dataclasses import dataclass
from score_point import ScorePoint


@dataclass
class Score2:
    player1: ScorePoint = ScorePoint.Love
    player2: ScorePoint = ScorePoint.Love
