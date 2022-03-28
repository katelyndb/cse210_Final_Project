from color import Color
from point import Point
import pyray
import os
from constants import *


class Sprite:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.
        Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """
    # A static variable to store all of the textures so we only load them once
    textures = {}
    
    def __init__(self):
        """Constructs a new Actor."""
        self._texture = "missing.png"
        self._original_texture = "missing.png"
        self._width = 16
        self._height = 16
        self._texture_x = 0
        self._texture_y = 0
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._rotation = 0
        self._scale = 2
        self._can_move_off_screen = False

    def load_texture(self):
        if self._original_texture not in Sprite.textures.keys():
            self._texture = pyray.load_texture(str(os.path.join(SPRITE_LOC,self._original_texture)))
            Sprite.textures[str(self._original_texture)] = self._texture
        else:
            self._texture = Sprite.textures[self._original_texture]

    def get_size(self):
        """Gets the actor's font size.
        
        Returns:
            Point: The actor's font size.
        """
        return (self._width,self._height)
        
    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_texture(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        if isinstance(self._texture,str):
            self.load_texture()
        return self._texture
    
    def get_texture_rect(self):
        return pyray.Rectangle(self._texture_x,self._texture_y,self._width,self._height)
        
    def get_scaled_rect(self):
        return pyray.Rectangle(self._position.get_x(),self._position.get_y(),self._width*self._scale,self._height*self._scale)
        
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y,wrap=False):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        if wrap:
            x = (self._position.get_x() + self._velocity.get_x()) % max_x
            y = (self._position.get_y() + self._velocity.get_y()) % max_y
        else:
            if not self._can_move_off_screen:
                x = min(max_x-self._width,(self._position.get_x() + self._velocity.get_x()))
                y = min(max_y-self._height,(self._position.get_y() + self._velocity.get_y()))
                x = max(0,x)
                y = max(0,y)
            else:
                x = self._position.get_x() + self._velocity.get_x()
                y = self._position.get_y() + self._velocity.get_y()
        self._position = Point(x, y)
        
    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_texture(self, texture):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._texture = texture
        self._original_texture = self._texture
        # self.load_texture()

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
        
    def set_size(self,vector:pyray.Vector2):
        self._width = vector[0]
        self._height = vector[1]
        
    def set_texture_point(self,vector:pyray.Vector2):
        self._texture_x = vector[0]
        self._texture_y = vector[1]  
        
    def draw(self):
        pyray.draw_texture_pro(self.get_texture(),self.get_texture_rect(),self.get_scaled_rect(),(0,0),self._rotation,pyray.WHITE)
      
    def constrain(self,min_x,min_y,max_x,max_y):
        x = min(max_x,self._position.get_x() )
        y = min(max_y,self._position.get_y() )
        x = max(min_x,x)
        y = max(min_y,y)
        self._position = Point(x, y)        