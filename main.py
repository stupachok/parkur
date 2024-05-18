from pygame import *
import sys

window = display.set_mode((700, 500))
display.set_caption("shos_cikave)))")
back_ground2 = image.load("background.png")
a1 = image.load("sprite.jpg")
a22 = image.load("sprite2.png")
background = transform.scale(back_ground2, (700, 500))
a1 = transform.scale(a1, (60, 50))
a22 = transform.scale(a22, (60, 50))
window.blit(background, (0, 0))

BLUE = (0, 0, 255)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(player_image, (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect.midbottom = (player_x, player_y)
        self.isJump = False
        self.jumpCount = 8

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_d]:
            self.image = a22

        for wall in walls:
            if self.rect.colliderect(wall.rect) and self.jumpCount < 0:
                self.isJump = False
                self.jumpCount = 8
                self.rect.bottom = wall.rect.top
        on_platform = False
        for wall in walls:
            if self.rect.colliderect(wall.rect) and self.rect.bottom == wall.rect.top:
                on_platform = True
                break
        if not on_platform and not self.isJump:
            self.rect.y += 5
            for wall in walls:
                if self.rect.colliderect(wall.rect) and self.rect.bottom > wall.rect.top:
                    self.rect.bottom = wall.rect.top
                    break

        if keys_pressed[K_SPACE]:
            self.isJump = True

        if self.isJump:

            if self.jumpCount >= -8:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) / 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 1



            else:
                self.isJump = False
                self.jumpCount = 8



class Wall:
    def __init__(self, color, player_x, player_y, width, height):
        self.surface = Surface((width, height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.surface, (self.rect.x, self.rect.y))


run = True
finish = False

walls = [
    Wall(BLUE, 1, 450, 700, 10),
    Wall(BLUE, 200, 370, 10, 10),
    Wall(BLUE, 300, 300, 10, 10),
    Wall(BLUE, 400, 240, 10, 10),
    Wall(BLUE, 500, 170, 10, 10),
    Wall(BLUE, 600, 100, 110, 10)
]

sprite1 = GameSprite(a1, 50, 449, 5, 60, 50)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))

    for wall in walls:
        wall.draw()

    sprite1.draw()
    sprite1.move()

    display.update()
    time.delay(17)
