import os
import random

from game.actor import Actor

from game.cast import Cast

from game.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 25
FONT_SIZE = 25
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(10, 20)


def main():
    
    # create the cast
    cast = Cast()



    # create the turtle, place at the left side of screen
    x = int(MAX_X / 2)
    y = 200
    position = Point(x, y)


    turtle = Actor()
    turtle.set_text("#")
    turtle.set_font_size(15)
    turtle.set_position(position)
    cast.add_actor("turtle", turtle)




    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)




if __name__ == "__main__":
    main()