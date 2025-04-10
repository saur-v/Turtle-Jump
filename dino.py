from turtle import *

import random


class Dinos():
    def __init__(self) -> None:
        self.dino = Turtle(shape='turtle')
        self.dino.color('white')
        self.dino.penup()
        self.dino.goto(-200,-50)
        self.dino.setheading(90) 
        self.dino.speed(6)  
    def Scree(self):
        self.screen=Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=500,height=300)

        
    def resist(self) -> None:
        size = [2,5]
        pos = random.choice(size)
        self.resi = Turtle()
        self.resi.color('white')
        self.resi.penup()
        if pos==2:
            self.resi.goto(250,-45)
        else:
            self.resi.goto(250,-15)
        self.resi.setheading(90)
        self.resi.shapesize(stretch_len=pos)

    def resist_move(self):
        current_posy=self.resi.ycor()
        self.resi.goto(self.resi.xcor()-2,current_posy)       
        

    def jump(self): 
        self.screen.onkey(None, 'Up')
        current_posy=self.resi.ycor()
        for i in range(1,31,3):
            self.resi.goto(self.resi.xcor()-3.5,current_posy) 
            self.dino.goto(-200,self.dino.ycor()+8)
        for i in range(1,31,3):  
            self.resi.goto(self.resi.xcor()-3.5,current_posy) 
            self.dino.goto(-200,self.dino.ycor()-8)
        self.screen.onkey(self.jump, 'Up')

    def game_over(self):
        self.text = Turtle()
        self.text.hideturtle()
        self.text.color('white')
        self.text.write('Game over', align='center',font=('arial',20))
        

            
            
        

      

    

