class Score:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0


current_score = Score()
current_score_player1 = 0
current_score_player2 = 0


def init_game():
    global current_score
    current_score = Score()


def player_scored(player_name):
    global current_score_player1
    global current_score_player2
    if player_name == "player1":
        current_score_player1 += 1
    else:
        current_score_player2 += 1

    return format_score(current_score_player1, current_score_player2)


def format_score(player1_score, player2_score):
    score_map = {
        0: "love",
        1: "15",
        2: "30",
        3: "40"
    }
    return score_map[player1_score] + " - " + score_map[player2_score]
