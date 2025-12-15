import pygame
import random
from game_objects import *

# Initialize Pygame
pygame.init()

HEIGHT = 800
WIDTH = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tight Lines")
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.Font(None, 24)

def main():
    running = True
    bg_color = (30, 30, 30)
    rect = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50)
    rect_color = (200, 50, 50)
    oceanFloor = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
    oceanFloor_color = pygame.Color('tan')
    oceanWater = pygame.Rect(0, HEIGHT // 2, WIDTH, HEIGHT // 2 - 50)
    oceanWater_color = pygame.Color('deepskyblue')
    speed = 300  # pixels per second
    
    # Fish list and spawn timer
    fish_list = []
    spawn_timer = 0
    spawn_interval = 2.0  # Spawn a fish every 2 seconds

    while running:
        dt = clock.tick(FPS) / 1000.0  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect.x -= int(speed * dt)
        if keys[pygame.K_RIGHT]:
            rect.x += int(speed * dt)
        if keys[pygame.K_UP]:
            rect.y -= int(speed * dt)
        if keys[pygame.K_DOWN]:
            rect.y += int(speed * dt)

        rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
        
        # Spawn fish at intervals
        spawn_timer += dt
        if spawn_timer >= spawn_interval:
            # Randomly choose which type of fish to spawn
            fish_type = random.choice([Salmon, Bass, Trout])
            fish_list.append(fish_type())
            spawn_timer = 0
        
        # Update fish positions
        for fish in fish_list:
            fish.move(dt)
        
        # Remove fish that went off screen (either side)
        fish_list = [fish for fish in fish_list if -20 < fish.x < WIDTH + 20]

        screen.fill(bg_color)
        
        # Draw ocean water (background - drawn first)
        pygame.draw.rect(screen, oceanWater_color, oceanWater)
        
        # Draw ocean floor
        pygame.draw.rect(screen, oceanFloor_color, oceanFloor)
        
        # Draw fish (on top of water)
        for fish in fish_list:
            fish.draw(screen)
        
        # Draw player character (on top)
        pygame.draw.rect(screen, rect_color, rect)

        fps_surf = font.render(f"FPS: {clock.get_fps():.2f}", True, (200, 200, 200))
        screen.blit(fps_surf, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()