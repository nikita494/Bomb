import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png", (0, 0, 0))
    image_boom = load_image("boom.png", (0, 0, 0))

    def __init__(self, width, height, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.image_boom.get_rect().width,
                                       width - self.image_boom.get_rect().width)
        self.rect.y = random.randrange(self.image_boom.get_rect().height,
                                       height - self.image_boom.get_rect().height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Boom them all')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    bombs = pygame.sprite.Group()
    for i in range(20):
        Bomb(width, height, bombs)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bombs.update(event)
        screen.fill((0, 0, 0))
        bombs.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
