from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
                self.rect.y -= self.speed
    
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s]:
                self.rect.y += self.speed

        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
                self.rect.x -= self.speed

        keys_pressed = key.get_pressed()
        if keys_pressed[K_d]:
                self.rect.x += self.speed



sprite1 = transform.scale(image.load('raketa.jpeg'), (10, 100))





clock = time.Clock()
FPS = 60
clock.tick(FPS)
window = display.set_mode((700, 500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('galaxy.png'), (700, 500))
mixer.init()




finish = False
game = True
while game:
    if finish != True:
        window.blit(background,(0, 0))
        window.blit(sprite1, (100, 100))










    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
