import random
from point import Point
import pyray
from color import Color

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
        
    def start_game(self, cast, castSprite, cast2):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        # I created the score here.
        self.score = 0
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast, castSprite, cast2)
            self._do_updates(cast, castSprite, cast2)
            self._do_outputs(cast, castSprite, cast2)
        self._video_service.close_window()

    def _get_inputs(self, cast, castSprite, cast2):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # turtle = cast.get_first_actor("turtles")
        t = castSprite.get_first_actor("ts")
        velocity = self._keyboard_service.get_direction()
        # turtle.set_velocity(velocity) 
        t.set_velocity(velocity)       

    def _do_updates(self, cast, castSprite, cast2):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        # turtle = cast.get_first_actor("turtles")
        t = castSprite.get_first_actor("ts")
        sharks = cast2.get_all_actors()
        message = f"Score: {self.score}"
        banner.set_text(message)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        # turtle.move_next(max_x, max_y)

        t.move_next(max_x, max_y)
        # turtle.set_velocity(Point(0,-4))
        # turtle.move_next(max_x, max_y)
                 
        t.set_velocity(Point(0,-4))
        t.move_next(max_x, max_y)

        for s in sharks:
            s.move_next(max_x, max_y)


    def _do_outputs(self, cast, castSprite, cast2):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        actors2 = castSprite.get_first_actor("ts")
        actors3 = cast2.get_all_actors()

        self._video_service.draw_actors(actors)
        self._video_service.draw_sprite(actors2)
        self._video_service.draw_sprites(actors3)
        self._video_service.flush_buffer()