from pygame import *




       

sprite1 = transform.scale(image.load('ракеткабомбапетарда.jpeg'), (10, 100))





clock = time.Clock()
FPS = 60
clock.tick(FPS)
window = display.set_mode((700, 500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()



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
            
