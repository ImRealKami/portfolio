# Turtle racing   

import turtle
import random
import time

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'yellow', 'black', 'pink', 'cyan']

def user_input():
    while True:
        racers = input("Enter the number of turtles (2-5): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Entered input should be numeric!")
            continue
        if 2 <= racers <= 5:
            return racers
        else: 
            print("Number not in range. Try again")

def choose_turtle():
    betting = input("Which turtle would you like to bet on [Red, Yellow, Black, Pink, Cyan] depends on the number of turtles choosen: ")
    value = random.randint(10, 50)

    winner = race(colors)
    print(f"The winner turtle is {winner}")

    if winner == betting :
        print(f"You won {value} dollars")
    else:
        print("You dint win anything... Try again later")


def race(colors):
    racer_turtles = create_turtles(colors)

    while True:
        for racer in racer_turtles:
            move = random.randrange(1,20)
            racer.forward(move)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[racer_turtles.index(racer)]

def create_turtles(colors):
    racer_turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setposition(-WIDTH//2 +(i+1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        racer_turtles.append(racer)
    
    return racer_turtles

def turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = user_input()
turtles()

colors = COLORS[:racers]
choose_turtle()
time.sleep(2)
