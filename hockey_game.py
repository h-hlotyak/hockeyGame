import turtle
import random
import math
import time



turtle.screensize(325,325)
turtle.hideturtle()
turtle.penup()
turtle.goto(-220,-35)
turtle.pendown()
turtle.goto(-220,35)
turtle.penup()

player = turtle.clone() #creates player
player.shape("square") # sets shape to square
player.goto(0,0) # puts player in the middle of the screen


player.showturtle()

computer = turtle.clone()
computer.shape("square")
computer.right(270)
computer.goto(-200, 0)

computer.showturtle()

writer = turtle.clone()

enemy = turtle.clone()
enemy.shape("square")
enemy.fillcolor("red")
enemy.goto(50,-50)

enemy.showturtle()

score = 0

GOAL_TOP = 35
GOAL_BOTTOM = -35
GOAL_X = -220

COLLISION_DISTANCE = 20 #distance for collision of enemy and player

STEP = 2 # how many pixels an object will move
PUCK_SPEED = 1
PLAYER_SPEED = 1
COMPUTER_SPEED = 2
ENEMY_SPEED = 0.1

puck_direction = [-10,0] # direction vector for puck
puck = turtle.clone() # creates puck
puck.shape("circle") # sets shape of puck to a circle

def shoot_puck(): # shoots puck
    global puck_direction
    puck_direction = [-10, 0]
    puck.hideturtle()
    puck_position = player.xcor() # gets the players x coordinate
    puck_y_cord = player.ycor() # gets players y coord
    puck.goto(puck_position, puck_y_cord) # sends the puck to the player
    puck.showturtle()  # shows the puck

def move_up(): # moves player up by 10
    position = player.ycor() # gets the current y coordnite and puts it into variable position
    x_cord = player.xcor() # gets the current x coordnite and puts it into variable x_cord
    position = position + 10 #increases value of position by 10, moves the player up by 10
    player.goto(x_cord, position) # moves player to the new coordnite

def move_down(): # moves player down by 10
    position = player.ycor()
    x_cord = player.xcor()
    position = position - 10 # decreases value of position by 10, moves player down 10
    player.goto(x_cord, position)

def move_right(): # moves player 10 to the right
    position = player.xcor()
    y_cord = player.ycor()
    position = position + 10 # adds 10 to the x value, moves player right by 10
    player.goto(position, y_cord)


def move_left(): # moves player to the left 10
    position = player.xcor()
    y_cord = player.ycor()
    position = position - 10
    if position <= -100:
        position = position + 15
    player.goto(position, y_cord)
    # make it so player cannot move past a certain point so it cant get close to computer to shoot

def goal_check():
    goal_x = -220
    goal_y_max = 25
    goal_y_min = -25
    puck_x = puck.xcor()
    puck_y = puck.ycor()
    if puck_x < goal_x:
        if puck_y < goal_y_max and puck_y > goal_y_min:
            return True
    else:
        return False

def move_puck():
    global score
    global puck_direction
    puck_x = puck.xcor()
    puck_y = puck.ycor()
    if puck_y >= 100 or puck_y <= -100:
        theta = math.atan(10)
        b = math.sin(theta) * 10
        a = math.cos(theta) * 10
        b = math.floor(b)
        a = math.floor(a)
        puck_direction = [a, b]
    puck_x = puck_x + puck_direction[0]
    puck_y = puck_y + puck_direction[1]
    goal = goal_check()
    if goal == True:
        score = score + 1
        print("yay")
    puck.goto(puck_x, puck_y)
    player_x = player.xcor()
    player_y = player.ycor()
    # make sure it's on the field
    if puck_x<= -325:
        #puck.hideturtle()
        puck_direction = [10,0]
        slope = (player_y - puck_y) / (player_x - puck_x)






def check_collision(): # collision check for puck and computer
    global puck_direction
    # for saying if coords are similar
    touching_x = 0
    touching_y = 0
    puck_x = puck.xcor() # get coordinates for puck and computer
    puck_y = puck.ycor()
    comp_x = computer.xcor()
    comp_y = computer.ycor()
    diff_x = puck_x - comp_x # get the difference of the x coords for computer and puck
    diff_x = abs(diff_x)
    diff_y = puck_y - comp_y # same for y
    diff_y = abs(diff_y)
    if diff_x <= COLLISION_DISTANCE: # if the difference is less than or equal to 20 then they have similar x values
        touching_x = 1

    else:
        touching_x = 0
    if diff_y <= COLLISION_DISTANCE: # if diff is less than or equal to 20 then they have similar y values
        touching_y = 1

    else:
        touching_y = 0
    if touching_x + touching_y == 2: # if the y and the x values are similar they are touching so hide the puck
        writer.goto(0,0)
        writer.write("intercepted!")
        flip = random.randint(1,2)
        if flip == 1:
            puck_direction = [10, 5]
        if flip == 2:
            puck_direction = [10, -5]
        #puck.hideturtle()


def enemy_collision_check():
    player_x = player.xcor()
    player_y = player.ycor()
    enemy_x = enemy.xcor()
    enemy_y = enemy.ycor()
    diff_x = player_x - enemy_x
    diff_y = player_y - enemy_y
    diff_x = abs(diff_x)
    diff_y = abs(diff_y)
    if diff_x <= COLLISION_DISTANCE:
        touching_x = 1
    else:
        touching_x = 0

    if diff_y <= COLLISION_DISTANCE:
        touching_y = 1
    else:
        touching_y = 0

    if touching_y + touching_x == 2:
        turtle.clearscreen()
        writer = turtle.clone()
        writer.goto(0,0)
        writer.write("game over")

def move_computer():
    move_distance = STEP
    y_pos = computer.ycor()  # the y coordinate for the computer
    x_pos = computer.xcor()
    flip = random.randint(1, 2)  # coin flip for computer going up or down randomly
    if flip == 1:  # move up
        step_multiplier = random.uniform(0.0, 3.0) # multiplier on step distance
        move_distance = step_multiplier*move_distance
        computer.goto(x_pos,move_distance)  # moves up
    if flip == 2:  # move down
        step_multiplier = random.uniform(0.0, -3.0) # picks random number for how fast it will move
        move_distance = step_multiplier*move_distance
        computer.goto(x_pos, move_distance)  # moves down

def enemy_control():
    #enemy has to get x coord and y coord of player
    #then gets its own coords and determined if it has to add x values or subtract, or add y values or subtract

    #set how many steps the enemy can take
    enemy_steps = ENEMY_SPEED*STEP

    #get x coord of player
    player_x = player.xcor()
    #get y coord of player
    player_y = player.ycor()

    #get x coord of enemy
    enemy_x = enemy.xcor()
    #get y coord of enemy
    enemy_y = enemy.ycor()

    #if the x coord of player is greater than the enemys
    if player_x > enemy_x:
        #add the amount of steps to the enemys x coord
        enemy_x = enemy_x + enemy_steps

    # if the x coord of player is less than the enemys
    if player_x < enemy_x:
        # subtract the amount of steps to the enemys x coord
        enemy_x = enemy_x - enemy_steps

    # if the y coord of player is greater than the enemys
    if player_y > enemy_y:
        # add the amount of steps to the enemys y coord
        enemy_y = enemy_y + enemy_steps

    # if the y coord of player is less than the enemys
    if player_y < enemy_y:
        # subtract the amount of steps to the enemys y coord
        enemy_y = enemy_y - enemy_steps

    enemy.goto(enemy_x, enemy_y)

def goal_check():
    global score
    global puck_direction
    puck_x = puck.xcor()
    diff = puck_x - GOAL_X
    diff = abs(diff)
    if diff <= 10:
        puck_y = puck.ycor()
        if puck_y <= GOAL_TOP and puck_y >= GOAL_BOTTOM:

            if puck_direction[0] < 0:
                print("its a goal")
                time.sleep(1)
                #puck.hideturtle()
                puck_direction = [10, 0]
                score = score + 1
                print(score)



def play_game():

    move_computer()
    #puck movement()
    move_puck()
    check_collision()
    enemy_control()
    enemy_collision_check()
    turtle.ontimer(play_game, 0)
    # have enemy player target player. player will die

play_game()
# when _ key is pressed it moves a certain direction
turtle.onkey(move_up, "w") #calls move_up
turtle.onkey(move_down, "s")
turtle.onkey(move_right, "d")
turtle.onkey(move_left, "a")


turtle.onkey(shoot_puck, "p")# when p is pressed shoots puck


#turtle.onkey(computer_move, "space")

turtle.listen()
turtle.mainloop()