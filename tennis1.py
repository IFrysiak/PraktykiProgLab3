class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        if self.is_tie():
            return self._tie_score()
        elif self.is_advantage_or_win():
            return self._advantage_or_win_score()
        else:
            return self._regular_score()

    def is_tie(self):
        return self.player1_score == self.player2_score

    def _tie_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"

    def is_advantage_or_win(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def _advantage_or_win_score(self):
        score_diff = self.player1_score - self.player2_score

        if abs(score_diff) >= 2:
            winning_player = self.player1_name if score_diff > 0 else self.player2_name
            return f"Win for {winning_player}"
        else:
            leading_player = self.player1_name if score_diff == 1 else self.player2_name
            return f"Advantage {leading_player}"

    def _regular_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"