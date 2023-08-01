from turtle import Turtle

data_location = "Snake_game/data.txt"

new_data = 0

with open(data_location) as data:
        new_data = data.read()
        print(new_data)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.highscore = new_data
        self.goto(0,280)
        self.color("white")
        self.current_Score = 0
        self.write(f"score : {self.current_Score}",align="center",font = ("Arial",16,"normal"))


    def update(self):
        self.clear()
        self.write(f"score : {self.current_Score} high score : {self.highscore}",align="center",font = ("Arial",16,"normal"))

    
    def reset_score(self):
        if self.current_Score > int(self.highscore):
            self.highscore = str(self.current_Score)
        
        with open(data_location,mode="w") as data:
             data.write(self.highscore)

        self.current_Score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game_Over",align="center",font=("Arial", 16, "normal"))

    def increase_Score(self):
        self.current_Score+=1
        self.update()


