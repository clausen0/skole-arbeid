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

main = True

...
# objekter
...


class Player(pygame.sprite.Sprite):  # spiller klasse
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        #img = pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        img = pygame.image.load(os.path.join(
            currentPath + 'images', 'hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


...
# setup
...

# klokke, trengs for å kjøre koden
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((1200, 650))

player = Player
# player.rect = 0
#player.rect = 0
player_list = pygame.sprite.Group()
player_list.add(player)

# under er hvordan bakrunnen til spillet skal se ut. Denne delen av koden skal fikse slik at man greier å hente frem informasjon
# fra img filer som er lagret i mappen som heter images

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load_extended(currentPath + "/images/stage.png")
# backdropbox = world.get_reackt

...
# main.loop
...

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    # world.blit(backdrop. backdropbox)  # refresher bakrunen
    # pygame.display.flip()  # refresher alt på skjermen
    player_list.draw(world)
    clock.tick(fps)
