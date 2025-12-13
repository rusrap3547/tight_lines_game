import pygame
import random
import main

FISH_TYPES = [
    {
        "name": "bass",
        "speed": 100,
        "size": (40, 20),
        "color": (34, 139, 34),
        "spawn_rate": 0.5,
        "points": 1
    },
    {
        "name": "trout",
        "speed": 150,
        "size": (30, 15),
        "color": (70, 130, 180),
        "spawn_rate": 0.7,
        "points": 2
    },
    {
        "name": "salmon",
        "speed": 200,
        "size": (50, 25),
        "color": (250, 128, 114),
        "spawn_rate": 0.3,
        "points": 5
    }
]

class Fish:
    def __init__(self, fish_config):
        self.name = fish_config["name"]
        self.speed = fish_config["speed"]
        self.size = fish_config["size"]
        self.color = fish_config["color"]
        self.points = fish_config["points"]
        self.start = fish_config["spawn_rate"]

# Usage:
import random
fish = Fish(random.choice(FISH_TYPES))