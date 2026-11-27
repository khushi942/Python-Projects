from turtle import Turtle

ALIGNMENT="left"
FONT=('Courier', 24, 'bold')

# TODO 5: CREATE A SCOREBOARD
class Scoreboard(Turtle):
                # Class Attribute is common for all objects whereas instance attribute value is different for different object
    # high_score=0   # Class Attribute: but here instance attribute bhi shi se behave kre ga because scoreboard ka new object bn hi nhi rha hai
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.teleport(-200, 240)
        self.pencolor("white")

        with open("snakegame_data.txt",mode='r') as f:
            file_highscore=f.read()
            self.high_score=int(file_highscore)   # type casting str to int
        #here self.high_score is instance attribute
        self.update_score_board()

    def show_game_over(self):
        self.teleport(-70,0)
        self.write("Game Over ",align=ALIGNMENT,font=FONT )



    def update_score_board(self):
        self.clear()
        self.write(f"Score={self.score} High Score={self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score>self.high_score:
            self.high_score=self.score
            # Writing new highscore in the snakegame_data.txt file
            with open("snakegame_data.txt",mode='w') as f:
                f.write(str(self.high_score))

        self.score = 0
        self.update_score_board()



    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score_board()