from utils import *


# Section 1 - Variables
# - add starting values for all the variables
x1 =-90
y1 =-80
x2 =-90
y2 =-40
x3 =-90
y3 =15
x4 =-90
y4 =80


# Section 2 - Setup
# #- use your own background, and set your four turtles to images of your choice
set_background("moon")
t1 = create_sprite("lebron(1)",x1,y1)
t2 = create_sprite("ronaldo.gif",x2,y2)
t3 = create_sprite("america.gif",x3,y3)
t4 = create_sprite("drunkkirmit.gif",x4,y4)


# # Section 3 - Racing
# #  - set how much each variable changes by and increase the number of repeats to at least 30
# # - explain here which sprites are faster or slower
for i in range(30):
    x1 += random.choice([1,0,0,0,50])
    x2 += random.choice([5,0,0,0,50])   
    x3 += random.randint(20,29)
    x4 += random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600])
# technically it x4 would be the fastest if it is lucky but it is a 1 in 31 chance so probably x3
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.5)

    if x1 > 300: 
        break
    if x2 > 300 :
        break
    if x3 > 300 :
        break
    if x4 > 300 :
        break


# Section 4 - Winner
#  - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-250,-250)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
if x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("player 2 wins!")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("player 3 wins!")    
if x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("player 4 wins!")

turtle.exitonclick()