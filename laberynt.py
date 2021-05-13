import pygame
import sys
import os

...
# Variaber
...
worldx = 400  # bredden på spill rammen
worldy = 400  # lengden på spill rammen

fps = 40  # framerate
ani = 4  # animasjon cyklus

# slipper å skrive hovedkode/ når man skal vise til hvor man henter ting fra
currentPath = "labyrintoppgave/hovedkode/"

# farger, kan brukes til å lage bakrunnen isteden for å importere bilder som bakrunn.
BLACK = (25, 25, 200)
WHITE = (254, 254, 254)

vel1 = 2
vel2 = 3
...
# objekter
...


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = vel1


class Vector3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = vel2


class Player:  # (pygame.sprite.Sprite):  # spiller klasse
    def __init__(self, pos1: Vector2):
        self.heading = 0
        self.char = [
            pygame.image.load(os.path.join(
                currentPath + 'sprites', 'hero_idle.png')),
            pygame.image.load(os.path.join(
                currentPath + 'sprites', 'hero_left.png')),
            pygame.image.load(os.path.join(
                currentPath + 'sprites', 'hero_right.png')),
            pygame.image.load(os.path.join(
                currentPath + 'sprites', 'hero_up.png')),
            pygame.image.load(os.path.join(currentPath + 'sprites', 'hero_down.png'))]
        self.x = pos1.x
        self.y = pos1.y
        self.spawn = pos1
        screen.blit(self.char[self.heading], (self.spawn.x, self.spawn.y))

    def draw(self):
        screen.blit(self.char[self.heading], (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.y += vel1
            self.heading = 4
        if keys[pygame.K_w]:
            self.y -= vel1
            self.heading = 3
        if keys[pygame.K_a]:
            self.x -= vel1
            self.heading = 1
        if keys[pygame.K_d]:
            self.x += vel1
            self.heading = 2

    def rect(self):
        return self.image.get_rect()


class Wall:
    def __init__(self, pos2: Vector3):
        self.heading = 0
        self.char[
            pygame.rect.load(os.path.join(
                currentPath + 'sprites', 'vegg.png'))]
        self.x = pos2.x
        self.y = pos2.y
        self.spawn = pos2
        screen.blit(self.char[self.heading], (self.spawn.x, self.spawn.y))

    def draw(self):
        screen.blit(self.char[self.heading], (self.x, self.y))


def draw_window():
    screen.blit(backdrop, (0, 0))
    player.update()
    wall.uppdate()
    player.draw()
    wall.draw()

    pygame.display.update()


def drawGrid():
    blockSize = 20
    for x in range(0, worldx, blockSize):
        for y in range(0, worldy, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

    pygame.display.update()


...
# setup
...

# klokke, trengs for å kjøre koden
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((1200, 650))


# under er hvordan bakrunnen til spillet skal se ut. Denne delen av koden skal fikse slik at man greier å hente frem informasjon
# fra img filer som er lagret i mappen som heter images

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join(
    currentPath + 'sprites', 'stage.png'))


...
# main.loop
...


def main():

    run = True

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((worldx, worldy))
    CLOCK = pygame.time.Clock()

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quitting')
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False

        draw_window()
        drawGrid()


if __name__ == '__main__':
    pos1 = Vector2(50, 80)
    player = Player(pos1)
    pos2 = Vector3(10, 10)
    wall = Wall(pos2)
    main()
