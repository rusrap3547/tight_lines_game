from asyncio import FrameCallGraphEntry

import pygame
import random
import main

class swimmingFish (self, race, color):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.race = race
        self.color = color
        self.speed = random.randint(1, 5)


Bass = {
    'Name': 'Bass',
    'Color': "Gray",
    
}

print(swimmingFish(Bass))