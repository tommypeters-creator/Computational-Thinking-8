from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("saas")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
money = 0
warehouse = 0

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -250,200)
m1.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_money():
    global money
    money += 1
    x= random.randint(-200,200)
    y= random.randint(-200,200)
def Get_warehouse():
    global money, warehouse
    if money >= 50:
        warehouse += 1
        x= random.randint(-200,200)
        y= random.randint(-200,200)  
#get warehouse give money passivley, you need 30 money to get warehouse
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_money, "space")
# TODO - make a second control

window.onkeypress(Get_warehouse, "w")
#get_money gives you 1 money every space press


# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    if i % 10 == 0:
        money += warehouse

    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write (f"you have {warehouse} warehouses,you have {money} money")

    time.sleep(0.01)
    window.update()
    #the goal of the game is to get to 50,000 money