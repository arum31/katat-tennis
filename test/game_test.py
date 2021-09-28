from game import init_game, player_scored, Score


def test_should_return_15_when_player1_scores_one_time():
    init_game()
    current_score = Score()

    score = player_scored(current_score, "player1")

    assert score == Score(1, 0)


def test_should_return_30_0_when_player1_scores_two_times():
    current_score = Score()

    score = player_scored(current_score, "player1")
    score = player_scored(score, "player1")

    assert score == Score(2, 0)


def test_should_return_40_0_when_player1_scores_three_times():
    init_game()
    current_score = Score()

    player_scored("player1")
    player_scored("player1")
    score = player_scored("player1")

    assert score == Score(3, 0)


def test_should_return_0_15_when_player2_scores_one_time():
    init_game()

    score = player_scored("player2")

    assert score == Score(0, 1)
