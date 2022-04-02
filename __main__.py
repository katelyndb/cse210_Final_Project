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
from sprite import Sprite
from constants import *



def main():
    
    # Create the cast.
    cast = Cast()
    castSprite = Cast()

    # Create the banner for the points.
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(Color(169, 169, 169))
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

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
    shark_list = ["shark_image.png","Whale_image.png", "Stingray_image.png" ]
    for n in range(4):
        p = Point(800, random.randint(100,900))
        shark = Sprite()
        shark.set_texture(random.choice(shark_list))
        shark.set_position(p)
        # shark.set_size((0,0))
        # shark.set_velocity(Point(random.randint(-7,-4),0))
        shark.set_velocity(Point(random.randint(-7,-4), 0))
        castSprite.add_actor("sharks", shark)


    # Start the game.
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast, castSprite)


if __name__ == "__main__":
    main()