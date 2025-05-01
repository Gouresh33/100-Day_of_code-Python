from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 21, 'normal')


class scoreboared(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.Updatescore()
        self.hideturtle()

    def Updatescore(self):
        self.clear()
        self.write(arg=f"Score:{self.score} Highscore:{self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.Updatescore()

    # def Game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def incre_score(self):
        self.score += 1
        self.Updatescore()