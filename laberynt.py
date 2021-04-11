import pygame
import sys
import os

...
# Variaber
...
worldx = 960  # bredden på spill rammen
worldy = 720  # lengden på spill rammen

fps = 40  # framerate
ani = 4  # animasjon cyklus

# slipper å skrive hovedkode/ når man skal vise til hvor man henter ting fra
currentPath = "hoved kode/"

# farger, kan brukes til å lage bakrunnen isteden for å importere bilder som bakrunn.
BLACK = (25, 25, 200)
WHITE = (254, 254, 254)

# main = True
vel = 2

...
# objekter
...


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = vel


class Player:  # (pygame.sprite.Sprite):  # spiller klasse
    def __init__(self, pos: Vector2):
        self.heading = 0
        self.char = [pygame.image.load(os.path.join(currentPath + 'sprites', 'hero_idle.png')), pygame.image.load(
            os.path.join(currentPath + 'sprites', 'hero_left.png')), pygame.image.load(os.path.join(currentPath + 'sprites', 'hero_right.png')), pygame.image.load(os.path.join(currentPath + 'sprites', 'hero_up.png')),
            pygame.image.load(os.path.join(currentPath + 'sprites', 'hero_down.png'))]
        self.x = pos.x
        self.y = pos.y
        self.spawn = pos
        screen.blit(self.char[self.heading], (self.spawn.x, self.spawn.y))

    def draw(self):
        screen.blit(self.char[self.heading], (self.x, self.y))
 n
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.y += vel
            self.heading = 4
        if keys[pygame.K_w]:
            self.y -= vel
            self.heading = 3
        if keys[pygame.K_a]:
            self.x -= vel
            self.heading = 1
        if keys[pygame.K_d]:
            self.x += vel
            self.heading = 2

    def rect(self):
        return self.image.get_rect()


def draw_window():
    screen.blit(backdrop, (0, 0))
    player.update()
    player.draw()

    pygame.display.update()


...
# setup
...

# klokke, trengs for å kjøre koden
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((1200, 650))

  
# player_list = pygame.sprite.Group()
# player_list.add(player)

# under er hvordan bakrunnen til spillet skal se ut. Denne delen av koden skal fikse slik at man greier å hente frem informasjon
# fra img filer som er lagret i mappen som heter images

world = pygame.display.set_mode([worldx, worldy])
# pygame.image.load_extended(currentPath + "/images/stage.png")
backdrop = pygame.image.load_extended(
    os.path.join(currentPath + 'sprites', 'background.png'))
# backdropbox = world.get_reackt

...
# main.loop
...


def main():

    run = True

    while run:
        print('running')
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quitting')
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False
            # if event.type == pygame.KEYDOWN:
            #    print('quitting')
            #    if event.key == ord('q'):
            #        pygame.quit()
            #    try:
            #        sys.exit()
            #    finally:
            #        main = False

        draw_window()

    # world.blit(backdrop. backdropbox)  # refresher bakrunen
    # pygame.display.flip()  # refresher alt på skjermen

    # player_list.draw(world)


if __name__ == '__main__':
    pos = Vector2(50, 80)
    player = Player(pos)

    main()
