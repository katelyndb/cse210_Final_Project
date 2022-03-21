import os
import random

from actor import Actor

from cast import Cast

from director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.color import Color
from shared.point import Point



def main():
    
    # create the cast
    cast = Cast()