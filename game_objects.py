import pygame
import random
import main

# Module exports
__all__ = ['Fish', 'spawn_fish']
class Fish:
    def __init__(self, x, y, fish_type, direction='right'):
        self.x = x
        self.y = y
        self.fish_type = fish_type
        self.direction = direction
        self.speed = random.randint(2, 5)
        
        # Load fish image based on type
        # self.image = pygame.image.load(f'assets/{fish_type}.png')
        # For now, use a colored rectangle
        self.width = 40
        self.height = 20
        self.color = self.get_fish_color()
        
    def get_fish_color(self):
        """Return different colors for different fish types"""
        colors = {
            'bass': (34, 139, 34),
            'trout': (255, 140, 0),
            'salmon': (255, 99, 71),
            'pike': (60, 179, 113)
        }
        return colors.get(self.fish_type, (100, 100, 100))
    
    def update(self):
        """Move the fish across the screen"""
        if self.direction == 'right':
            self.x += self.speed
        else:
            self.x -= self.speed
    
    def draw(self, screen):
        """Draw the fish on the screen"""
        pygame.draw.rect(screen, self.color, 
                        (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self, screen_width):
        """Check if fish has moved off screen"""
        if self.direction == 'right':
            return self.x > screen_width
        else:
            return self.x < -self.width


# Helper function to spawn fish at random heights
def spawn_fish(screen_height, fish_types=['bass', 'trout', 'salmon', 'pike']):
    fish_type = random.choice(fish_types)
    y = random.randint(50, screen_height - 100)
    direction = random.choice(['left', 'right'])
    x = -40 if direction == 'right' else 800  # Adjust based on your screen width
    return Fish(x, y, fish_type, direction)