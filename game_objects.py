import pygame
import random
import main

class swimmingFish:
    def __init__(self, x, y, race, color, speed):
        self.x = x
        self.y = y
        self.race = race
        self.color = color
        self.speed = speed
    
    def move(self, dt):
        self.x += self.speed * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)
        
class Salmon(swimmingFish):
    def __init__(self):
        # Randomly choose left or right side
        from_left = random.choice([True, False])
        
        if from_left:
            x = 0
            speed = random.randint(2, 6) * 60  # Positive speed (move right)
        else:
            x = main.WIDTH
            speed = -random.randint(2, 6) * 60  # Negative speed (move left)
        
        y = random.randint(50, main.HEIGHT - 50)
        color = (255, 0, 0)  # Red color for Salmon
        super().__init__(x, y, "Salmon", color, speed)

class Bass(swimmingFish):
    def __init__(self):
        # Randomly choose left or right side
        from_left = random.choice([True, False])
        
        if from_left:
            x = 0
            speed = random.randint(1, 5) * 60  # Positive speed (move right)
        else:
            x = main.WIDTH
            speed = -random.randint(1, 5) * 60  # Negative speed (move left)
        
        y = random.randint(50, main.HEIGHT - 50)
        color = (0, 0, 255)  # Blue color for Bass
        super().__init__(x, y, "Bass", color, speed)

class Trout(swimmingFish):
    def __init__(self):
        # Randomly choose left or right side
        from_left = random.choice([True, False])
        
        if from_left:
            x = 0
            speed = random.randint(3, 7) * 60  # Positive speed (move right)
        else:
            x = main.WIDTH
            speed = -random.randint(3, 7) * 60  # Negative speed (move left)
        
        y = random.randint(50, main.HEIGHT - 50)
        color = (0, 255, 0)  # Green color for Trout
        super().__init__(x, y, "Trout", color, speed)

FISHRACE = {
    "Salmon": {
        "name": "Salmon",
        "color": (255, 0, 0),
        "speed_range": (2, 6),
        "x": 85,
        "y": random.randint(50, main.HEIGHT - 50),
    },
    "Bass": {
        "name": "Bass",
        "color": (0, 0, 255),
        "speed_range": (1, 5),
        "x": 75,
        "y": random.randint(50, main.HEIGHT - 50),
    },
    "Trout": {
        "name": "Trout",
        "color": (0, 255, 0),
        "speed_range": (3, 7),
        "x": 55,
        "y": random.randint(50, main.HEIGHT - 50),
    },
}