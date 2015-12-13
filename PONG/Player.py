class Player():
    "Game player metadata"
    def __init__(self, score, paddle):
        self.score = score
        self.paddle = paddle

    def scored(self):
        self.score += 1
        print "Player ", self.paddle, " scored!"
