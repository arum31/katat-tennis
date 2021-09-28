import pytest

from game import player_scored, Score
from pytest import *


@pytest.mark.parametrize(
    "expected_score_p1, expected_score_p2, expected_results",
    [
        [1, 0, Score(1, 0)],
        [2, 0, Score(2, 0)],
        [3, 0, Score(3, 0)],
        [4, 0, Score(4, 0)],
        [0, 1, Score(0, 1)],
        [0, 2, Score(0, 2)],
        [0, 3, Score(0, 3)],
        [0, 4, Score(0, 4)],
        [1, 1, Score(1, 1)],
        [1, 2, Score(1, 2)],
        [1, 3, Score(1, 3)],
        [1, 4, Score(1, 4)],
        [2, 1, Score(2, 1)],
        [2, 2, Score(2, 2)],
        [2, 3, Score(2, 3)],
        [2, 4, Score(2, 4)],
        [3, 1, Score(3, 1)],
        [3, 2, Score(3, 2)],
        [3, 3, Score(3, 3)],
        [3, 4, Score(3, 4)],
        [4, 1, Score(4, 1)],
        [4, 2, Score(4, 2)],
        [4, 3, Score(4, 3)],
        [4, 4, Score(4, 4)],
    ]
)
def test_all_basic_scores(expected_score_p1, expected_score_p2, expected_results):
    score = Score()
    for i in range(expected_score_p1):
        score = player_scored(score, "player1")
    for i in range(expected_score_p2):
        score = player_scored(score, "player2")

    assert score == expected_results
