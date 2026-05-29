import turtle
import random
import time

# ---------------- GAME VARIABLES ----------------
delay = 0.2
score = 0
high_score = 0

bodies = []

# ---------------- SCREEN ----------------
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light blue")
s1.setup(width=600, height=600)
s1.tracer(0)

# ---------------- SNAKE HEAD ----------------
h1 = turtle.Turtle()
h1.speed(0)
h1.shape("circle")
h1.color("red")
h1.fillcolor("green")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# ---------------- FOOD ----------------
f1 = turtle.Turtle()
f1.speed(0)
f1.shape("square")
f1.color("red")
f1.fillcolor("blue")
f1.penup()
f1.goto(100, 100)

# ---------------- SCOREBOARD ----------------
s2 = turtle.Turtle()
s2.speed(0)
s2.penup()
s2.hideturtle()
s2.goto(-250, 260)

s2.write(
    "Score: 0   |   High Score: 0",
    font=("Arial", 14, "bold")
)

# ---------------- FUNCTIONS ----------------
def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def stop():
    h1.direction = "stop"

def move():

    if h1.direction == "up":
        y = h1.ycor()
        h1.sety(y + 20)

    if h1.direction == "down":
        y = h1.ycor()
        h1.sety(y - 20)

    if h1.direction == "left":
        x = h1.xcor()
        h1.setx(x - 20)

    if h1.direction == "right":
        x = h1.xcor()
        h1.setx(x + 20)

# ---------------- KEYBOARD ----------------
s1.listen()

s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveleft, "Left")
s1.onkey(moveright, "Right")
s1.onkey(stop, "space")

# ---------------- MAIN LOOP ----------------
while True:

    s1.update()

    # BORDER COLLISION
    if h1.xcor() > 290:
        h1.setx(-290)

    if h1.xcor() < -290:
        h1.setx(290)

    if h1.ycor() > 290:
        h1.sety(-290)

    if h1.ycor() < -290:
        h1.sety(290)

    # FOOD COLLISION
    if h1.distance(f1) < 20:

        # MOVE FOOD
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        f1.goto(x, y)

        # NEW BODY
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.shape("square")
        b1.color("yellow")
        b1.penup()

        bodies.append(b1)

        # SCORE UPDATE
        score += 10

        if score > high_score:
            high_score = score

        s2.clear()

        s2.write(
            "Score: {}   |   High Score: {}".format(score, high_score),
            font=("Arial", 14, "bold")
        )

        # SLOW SPEED INCREASE
        if delay > 0.05:
            delay -= 0.002

    # MOVE BODY
    for i in range(len(bodies)-1, 0, -1):

        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()

        bodies[i].goto(x, y)

    # FIRST BODY FOLLOW HEAD
    if len(bodies) > 0:

        x = h1.xcor()
        y = h1.ycor()

        bodies[0].goto(x, y)

    # MOVE HEAD
    move()

    # SELF COLLISION
    for b in bodies:

        if b.distance(h1) < 20:

            time.sleep(1)

            # RESET HEAD
            h1.goto(0, 0)
            h1.direction = "stop"

            # HIDE BODY
            for body in bodies:
                body.goto(1000, 1000)

            bodies.clear()

            # RESET SCORE
            score = 0
            delay = 0.2

            s2.clear()

            s2.write(
                "Score: {}   |   High Score: {}".format(score, high_score),
                font=("Arial", 14, "bold")
            )

    time.sleep(delay)

s1.mainloop()