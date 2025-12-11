import pygame


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
    speed = 300  # pixels per second

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

        screen.fill(bg_color)
        pygame.draw.rect(screen, rect_color, rect)

        fps_surf = font.render(f"FPS: {clock.get_fps():.2f}", True, (200, 200, 200))
        screen.blit(fps_surf, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()