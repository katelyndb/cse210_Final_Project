import os
import random
import pyray

from actor import Actor

from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 25
FONT_SIZE = 40
COLS = 60
ROWS = 40
CAPTION = "Turtle"
WHITE = Color(255, 255, 255)


def main():
    
    # Create the cast.
    cast = Cast()

    # Create the banner for the points.
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(Color(169, 169, 169))
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

     # Create the turtle at the bottom middle of screen.
    x = int(MAX_X / 2)
    y = 575
    position = Point(x, y)

    turtle = Actor()
    turtle.set_text("@@")
    turtle.set_font_size(FONT_SIZE)
    turtle.set_color(Color(0,255,0))
    # turtle.set_image(pyray.load_texture("turtle.png"))
    turtle.set_position(position)
    turtle.set_velocity(Point(0,3))
    cast.add_actor("turtles", turtle)


    # Start the game.
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()