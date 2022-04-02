import random
from point import Point
import pyray
from color import Color
from constants import *
from sprite import Sprite

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._count_speed = 0
        self._hit_ceiling = False
        self._collision = False

        self.shark_list = ["shark_image.png","Whale_image.png", "Stingray_image.png" ]
    
        
    def start_game(self, cast, castSprite):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        # I created the score here.
        self.score = 0
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast, castSprite)
            self._do_updates(cast, castSprite)
            self._do_outputs(cast, castSprite)
        self._video_service.close_window()

    def _get_inputs(self, cast, castSprite):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        turtle = castSprite.get_first_actor("turtles")
        velocity, self._count_speed = self._keyboard_service.get_direction(self._count_speed) 
        turtle.set_velocity(velocity)       

    def _do_updates(self, cast, castSprite):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        turtle = castSprite.get_first_actor("turtles")
        sharks = castSprite.get_actors("sharks")

        message = f"Score: {self.score}"
        banner.set_text(message)

        # Allows user to use the space bar to move turtle down.
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        turtle.move_next(max_x, max_y, False)

        # Gives the turtle the floating affect, moving upward.
        turtle.set_velocity(Point(0,-self._count_speed))
        turtle.move_next(max_x, max_y, False)
        self._count_speed += 1

        if turtle.get_position().get_y() <= 1:
            self._hit_ceiling = True

        # Moves each shark in the group across the screen, left.
        for shark in sharks:
            shark.move_next(max_x, max_y, False)

            if shark.get_position().get_x() < -150:
                shark.set_position(Point(MAX_X, random.randint(0, 550)))
                shark.set_velocity(Point(random.randint(-7,-4), 0))
                shark.set_texture(random.choice(SHARK_LIST))

            if shark.get_position() == turtle.get_position():
                self._collision = True
                print("collision")

        


    def _do_outputs(self, cast, castSprite):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        actors2 = castSprite.get_all_actors()

        self._video_service.draw_actors(actors)
        self._video_service.draw_sprites(actors2)
        self._video_service.flush_buffer()

        # # This will help get stop the velocity of all the objects
        # if self._hit_ceiling == True:
        #     for sprite in castSprite.get_all_actors():
        #         sprite._velocity = Point(0, 0)