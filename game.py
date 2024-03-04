import pygame as p
from random import randint

# pygame setup
p.init()
screen = p.display.set_mode((1280, 720))
clock = p.time.Clock()
running = True

player = p.Vector2(screen.get_width() / 2, screen.get_height() / 2)

p.mixer.music.load('speedOfLight.mp3')
p.mixer.music.set_volume(0.05)
p.mixer.music.play()

xv = 0
yv = 0
f = 0 

while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    dt = clock.tick(60) / 1000

 # Reset 'f' to 0 when it reaches 255

    screen.fill(p.Color(round(f), round(f), round(f)))
    
    p.draw.circle(screen, (p.Color(round(255 - f), round(255 - f), round(255 - f))), player, 20)
    
    keys = p.key.get_pressed()
    
    xv *= 0.95 + (keys[p.K_SPACE] * 0.045)
    yv *= 0.95 + (keys[p.K_SPACE] * 0.045)
    
    yv += (keys[p.K_w] - keys[p.K_s]) * 15 * dt
    xv += (keys[p.K_a] - keys[p.K_d]) * 15 * dt
    
    if keys[p.K_SPACE]:
        f += (255 - f)/25
    else:
        f += (0 - f)/25

    player.y -= yv
    player.x -= xv
    
    if player.y > 760:
        player.y = -40
    if player.y < -40:
        player.y = 760
    if player.x > 1320:
        player.x = -40
    if player.x < -40:
        player.x = 1320
                    
    p.display.flip()

p.quit()
