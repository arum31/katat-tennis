from game import init_game, player_scored


def test_should_return_15_when_player1_scores_one_time():
    init_game()

    score = player_scored("player1")

    assert score == "15 - love"


def test_should_return_30_0_when_player1_scores_two_times():
    init_game()

    player_scored("player1")
    score = player_scored("player1")

    assert score == "30 - love"


def test_should_return_40_0_when_player1_scores_three_times():
    init_game()

    player_scored("player1")
    player_scored("player1")
    score = player_scored("player1")

    assert score == "40 - love"


def test_should_return_0_15_when_player2_scores_one_time():
    init_game()

    score = player_scored("player2")

    assert score == "love - 15"
