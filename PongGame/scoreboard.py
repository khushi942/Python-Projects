from turtle import Turtle


FONT_NAME="Verdana"



class Scoreboard(Turtle):
    def __init__(self,x_position, name):
        super().__init__()
        self.hideturtle()
        self.xcor=x_position
        self.teleport(self.xcor, 200)
        self.score=0
        self.color("white")
        self.write(self.score,font=(FONT_NAME, 34, "bold"))
        self.name=name

    def increase_score(self):
        self.score+=1
        self.clear()
        # self.teleport(self.xcor,y=200)
        self.write(self.score,font=(FONT_NAME, 34, "bold"))

    def check_winner(self):
        if self.score==10:
            self.teleport(-200,0)
            self.write(f"{self.name} Wins", font=(FONT_NAME,34,"bold"))
            return True
        return False



