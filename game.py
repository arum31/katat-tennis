class Score:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)


current_score = Score()


def init_game():
    global current_score
    current_score = Score()


def display_score(score: Score):
    return ""


def player_scored(player_name):
    global current_score
    if player_name == "player1":
        current_score.player1 += 1
    else:
        current_score.player2 += 1

    return format_score(current_score.player1, current_score.player2)


def format_score(player1_score, player2_score):
    score_map = {
        0: "love",
        1: "15",
        2: "30",
        3: "40"
    }
    return score_map[player1_score] + " - " + score_map[player2_score]
