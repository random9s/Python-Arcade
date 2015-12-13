class Player:
    "Metadata for player"
    def __init__(self, lives, score):
        self.lives = 3
        self.score = 0

    def inc_score(self, score):
        self.score += score
