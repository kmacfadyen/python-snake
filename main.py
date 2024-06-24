from flask import Flask
from tkinter import *
import random

TK_SILENCE_DEPRECATION=1

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text='Score:{}'.format(score), font=('consales', 40))
label.pack()


window.mainloop()