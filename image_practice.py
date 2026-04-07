# Section 1 - Your code
from utils import *
set_background("capybara_sunset")

s1 = create_sprite("ronaldo.gif", 50, 100)
s2 = create_sprite("lebron(1).gif", -112, 100)
s2 = create_sprite("ronaldo.gif", -79, -100)
s2 = create_sprite("lebron(1).gif", 56, -100)

message1 = create_sprite("alien",-2,200)
message1.color("green")
message1.write("sup G",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()