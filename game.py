from dataclasses import dataclass


@dataclass
class Score:
    player1: int = 0
    player2: int = 0


def display_score(score: Score):
    return ""


def player_scored(current_score, player_name):
    if player_name == "player1":
        new_score = Score(current_score.player1 + 1, current_score.player2)
    else:
        new_score = Score(current_score.player1, current_score.player2 + 1)

    return new_score


def format_score(player1_score, player2_score):
    score_map = {
        0: "love",
        1: "15",
        2: "30",
        3: "40"
    }
    return score_map[player1_score] + " - " + score_map[player2_score]
