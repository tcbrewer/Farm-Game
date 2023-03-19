import pygame #Tech with Tim Youtube Tutorial
import os
pygame.font.init()

pygame.display.set_caption("OwO")

WIDTH, HEIGHT = 1300, 830
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTR = (WIDTH / 2, HEIGHT / 2)
DARKCY = (0, 109, 119)
LITECY = (131, 197, 190)
PEARLY = (237, 246, 249)
LITPNK = (255, 221, 210)
PAPAYA = (226, 149, 120)
MAROON = (153, 66, 66)
SEABLU = (45, 185, 216)
SHADOW = (23, 122, 149)
DRKBLU = (0, 58, 81)
FPS = 60
DOGZILLA_SIZE = (158, 255.64937022)
VEL = 5 #velocity
BULLET_VEL = 7 #bullet velocity
MAX_BULLETS = 3
DOGZILLA_0_IMG = pygame.image.load(os.path.join('Assets', 'Nautilus.png'))
DOGZILLA_0 = pygame.transform.scale(DOGZILLA_0_IMG, DOGZILLA_SIZE)
DOGZILLA_1_IMG = pygame.image.load(os.path.join('Assets', 'AntiNautilus.png'))
DOGZILLA_1 = pygame.transform.scale(DOGZILLA_1_IMG, DOGZILLA_SIZE)
BULLET = pygame.image.load(os.path.join('Assets', 'Bubbullet.png'))
BORDER = pygame.Rect(CENTR[0] - 5, 0, 10, HEIGHT) #x, y, w, h
NAUT_HIT = pygame.USEREVENT + 1 #Nautilus is hit
ANTI_HIT = pygame.USEREVENT + 2 #Edgy Nautilus is hit
HEALTH_FONT = pygame.font.SysFont(None, 40)
WINNER_FONT = pygame.font.SysFont(None, 100)



def draw_window(rect0, rect1, bullets_0, bullets_1, naut_health, anti_health):
    WIN.fill(SEABLU)
    pygame.draw.rect(WIN, SHADOW, BORDER)

    naut_health_text = HEALTH_FONT.render("Dogzilla Health: " + str(naut_health), 1, PEARLY)
    anti_health_text = HEALTH_FONT.render("Edgy Dogzilla Health: " + str(anti_health), 1, DRKBLU)
    WIN.blit(naut_health_text, (10, 10))
    WIN.blit(anti_health_text, (WIDTH - anti_health_text.get_width() - 10, 10))

    WIN.blit(DOGZILLA_0, (rect0.x, rect0.y))
    WIN.blit(DOGZILLA_1, (rect1.x, rect1.y))

    for bullet in bullets_0:
        WIN.blit(BULLET, (bullet.x, bullet.y))
    for bullet in bullets_1:
        WIN.blit(BULLET, (bullet.x, bullet.y))

    pygame.display.update()


def dogzilla_0_movement(keys_pressed, rect):
        #normal Nautilus motion
        if keys_pressed[pygame.K_a] and rect.x - VEL > 0: #A key
            rect.x -= VEL
        if keys_pressed[pygame.K_d] and rect.x + DOGZILLA_SIZE[0] + VEL < CENTR[0]: #D key
            rect.x += VEL
        if keys_pressed[pygame.K_w] and rect.y + 35 - VEL > 0: #W key
            rect.y -= VEL
        if keys_pressed[pygame.K_s] and rect.y + 225 + VEL < HEIGHT: #S key
            rect.y += VEL

def dogzilla_1_movement(keys_pressed, rect):
        #anti-Nautilus motion
        if keys_pressed[pygame.K_LEFT] and rect.x - VEL > CENTR[0]: #< key
            rect.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and rect.x + DOGZILLA_SIZE[0] + VEL < WIDTH: #> key
            rect.x += VEL
        if keys_pressed[pygame.K_UP] and rect.y + 35 - VEL > 0: #^ key
            rect.y -= VEL
        if keys_pressed[pygame.K_DOWN] and rect.y + 225 + VEL < HEIGHT: #v key
            rect.y += VEL

def handle_bullets(bullets0, bullets1, rect0, rect1):
    for bullet in bullets0:
        bullet.x += BULLET_VEL
        if rect1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ANTI_HIT))
            bullets0.remove(bullet)

    for bullet in bullets1:
        bullet.x -= BULLET_VEL
        if rect0.colliderect(bullet):
            pygame.event.post(pygame.event.Event(NAUT_HIT))
            bullets1.remove(bullet)

def draw_winner(text):
    if text == "Dogzilla Wins!":
        color = PEARLY
    else:
        color = DRKBLU
    draw_text = WINNER_FONT.render(text, 1, color)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2500)

def main():
    rect0 = pygame.Rect(CENTR[0] * 0.5 - DOGZILLA_SIZE[0] / 2, CENTR[1] - DOGZILLA_SIZE[1] / 2, DOGZILLA_SIZE[0], DOGZILLA_SIZE[1])
    rect1 = pygame.Rect(CENTR[0] * 1.5 - DOGZILLA_SIZE[0] / 2, CENTR[1] - DOGZILLA_SIZE[1] / 2, DOGZILLA_SIZE[0], DOGZILLA_SIZE[1])
    
    bullets_0 = []
    bullets_1 = []

    naut_health = 10
    anti_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LSHIFT and len(bullets_0) < MAX_BULLETS: #left shift
                      bullet = pygame.Rect(rect0.x + DOGZILLA_SIZE[0] - 15, rect0.y + 70, 15, 15)
                      bullets_0.append(bullet)
                
                 if event.key == pygame.K_RSHIFT and len(bullets_1) < MAX_BULLETS: #right shift
                    bullet = pygame.Rect(rect1.x, rect1.y + 70, 15, 15)
                    bullets_1.append(bullet)
            
            winner_text = ""
            if event.type == NAUT_HIT:
                naut_health -= 1

            if event.type == ANTI_HIT:
                anti_health -= 1

        if anti_health <= 0:
            winner_text = "Dogzilla Wins!"

        if naut_health <= 0:
            winner_text = "Edgy Dogzilla Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        dogzilla_0_movement(keys_pressed, rect0)
        dogzilla_1_movement(keys_pressed, rect1)

        handle_bullets(bullets_0, bullets_1, rect0, rect1)

        draw_window(rect0, rect1, bullets_0, bullets_1, naut_health, anti_health)

    main()

if __name__ == "__main__":
    main()