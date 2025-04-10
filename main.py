from turtle import *
from dino import Dinos

game = Dinos()
game.Scree()

game.screen.tracer(0)


game.resist()
line = Turtle()
line.hideturtle()
line.color('white','white')
line.penup()
line.setpos(-250,-70)
line.pendown()
line.goto(250,-70)

is_game_on=True

game.screen.update()
game.screen.tracer(1)


    


while is_game_on:
    game.screen.update()

    if game.resi.xcor()>-250:
        game.resist_move()
        game.screen.onkey(game.jump, 'Up')
        game.screen.listen()
    else:
        game.screen.tracer(0)
        game.resist()
        game.screen.tracer(1) 

    if (game.dino.distance(game.resi)<38 and game.resi.ycor()==-15) or \
        (game.dino.distance(game.resi)<12 and game.resi.ycor()==-45):
        game.game_over()
        is_game_on = False
    else :
        is_game_on = True  
      
    

   
        


    
game.screen.mainloop()