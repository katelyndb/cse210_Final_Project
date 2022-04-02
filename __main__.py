import os
import random
import pyray
import raylib

from actor import Actor
from cast import Cast
from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point
from sprite import Sprite
from constants import *



def main():
    
    # Create the cast.
    cast = Cast()
    castSprite = Cast()
    castWelcome = Cast()

    #Creates the Welcome Screen

    welcome_background = Sprite()
    welcome_background.set_texture('underwater.png')
    welcome_background.set_position(Point(0, 0))
    welcome_background.set_size((150,150))
    castWelcome.add_actor("welcome_background", welcome_background)



    welcome_turtle = Sprite()
    welcome_turtle.set_texture(random.choice(WELCOME_TURTLES))
    welcome_turtle.set_position(Point(550, 250))
    welcome_turtle.set_size((150,150))
    castWelcome.add_actor("welcome_turtle", welcome_turtle)


    welcome_banner = Actor()
    welcome_banner.set_text("Welcome to the Aquarium!")
    welcome_banner.set_font_size(FONT_SIZE)
    welcome_banner.set_color(Color(169, 169, 169))
    welcome_banner.set_position(Point(CELL_SIZE, 300))
    cast.add_actor("banner_welcome", welcome_banner)

    start_banner = Actor()
    start_banner.set_text("Press space to start...")
    start_banner.set_font_size(FONT_SIZE)
    start_banner.set_color(Color(169, 169, 169))
    start_banner.set_position(Point(CELL_SIZE, 500))
    cast.add_actor("banner_start", start_banner)

    # Create the banner for the points.
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(Color(169, 169, 169))
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    background = Sprite()
    background.set_texture('underwater.png')
    background.set_position(Point(0, 0))
    background.set_size((150,150))
    castSprite.add_actor("background", background)

    # create the turtle sprite
    position = Point(80, 400)
    turtle = Sprite()
    turtle.set_texture("turtle3.png")
    turtle.set_size((16,16))
    turtle.set_position(position)
    turtle._can_move_off_screen = False
    # turtle.set_texture_point((14*16,21*16))        # Not sure if we need these two lines of code.
    # turtle.set_velocity(Point(1,2))
    castSprite.add_actor("turtles", turtle)

    # Create a group of shark sprites.
    for n in range(4):
        p = Point(800, random.randint(0, 550))
        shark = Sprite()
        shark.set_texture(random.choice(SHARK_LIST))
        shark.set_position(p)
        # shark.set_size((0,0))
        # shark.set_velocity(Point(random.randint(-7,-4),0))
        shark.set_velocity(Point(random.randint(-7,-4), 0))
        castSprite.add_actor("sharks", shark)

    


    # Start the game.
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast, castSprite, castWelcome)


if __name__ == "__main__":
    main()