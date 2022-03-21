import random
from game.shared.point import Point

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
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        # I created the score here.
        self.score = 0

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for artifact in artifacts:
            artifact.move_next(max_x, max_y)

            # Find the difference between artifact and robot.
            delta = artifact.get_position().subtract(robot.get_position())

            # If the difference between and artifact and robot is less than 25,
            # restart it at a random place at the top of the game screen.

            # Displays score on top of the screen
            message = f"Score: {self.score}"
            banner.set_text(message)

            # Detect collisions
            if abs(delta.get_x()) < 25 and abs(delta.get_y()) < 25:
                artifact.set_position(Point(random.randint(1, self._video_service.get_width()), 0))
                # Update score based upon being a gem or rock
                if artifact._text == "*":
                    self.score += 1
                if artifact._text == "o":
                    self.score -= 1

            # If the artifact makes it to the bottom of the screen, assign it to a new random 
            # position at the top of the screen.
            if robot.get_position().equals(artifact.get_position()):
                artifact.set_position(Point(random.randint(1, self._video_service.get_width()), 0))
                
                   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()