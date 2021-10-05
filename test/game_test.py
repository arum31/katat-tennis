import pytest

from game import player_scored, Score, player_scored2
from score import Score2
from pytest import *

from score_point import ScorePoint


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

@pytest.mark.parametrize(
    "expected_score_p1, expected_score_p2, expected_results",
    [
        [1, 0, Score2(ScorePoint.Fifteen, ScorePoint.Love)],
        [2, 0, Score2(ScorePoint.Thirteen, ScorePoint.Love)],
        [3, 0, Score2(ScorePoint.Fourteen, ScorePoint.Love)],
        [0, 1, Score2(ScorePoint.Love, ScorePoint.Fifteen)],
        [0, 2, Score2(ScorePoint.Love, ScorePoint.Thirteen)],
        [0, 3, Score2(ScorePoint.Love, ScorePoint.Fourteen)],
        [1, 1, Score2(ScorePoint.Fifteen, ScorePoint.Fifteen)],
        [1, 2, Score2(ScorePoint.Fifteen, ScorePoint.Thirteen)],
        [1, 3, Score2(ScorePoint.Fifteen, ScorePoint.Fourteen)],
        [2, 1, Score2(ScorePoint.Thirteen, ScorePoint.Fifteen)],
        [2, 2, Score2(ScorePoint.Thirteen, ScorePoint.Thirteen)],
        [2, 3, Score2(ScorePoint.Thirteen, ScorePoint.Fourteen)],
        [3, 1, Score2(ScorePoint.Fourteen, ScorePoint.Fifteen)],
        [3, 2, Score2(ScorePoint.Fourteen, ScorePoint.Thirteen)],
        [3, 3, Score2(ScorePoint.Fourteen, ScorePoint.Fourteen)],
    ]
)
def test_all_basic_scores_2(expected_score_p1, expected_score_p2, expected_results):
    score = Score2()
    for i in range(expected_score_p1):
        score = player_scored2(score, "player1")
    for i in range(expected_score_p2):
        score = player_scored2(score, "player2")

    assert score == expected_results
