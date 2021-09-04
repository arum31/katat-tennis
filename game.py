current_score_player1 = 0
current_score_player2 = 0


def init_game():
    global current_score_player1
    current_score_player1 = 0


def player_scored(player_name):
    global current_score_player1
    global current_score_player2
    if player_name == "player1":
        current_score_player1 += 15
    else:
        current_score_player2 += 15

    if current_score_player1 == 45:
        current_score_player1 = 40

    return format_score(current_score_player1, current_score_player2)


def format_score(player1_score, player2_score):
    return str(player1_score) + " - " + str(player2_score)
