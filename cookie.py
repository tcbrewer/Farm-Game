import pygame, sys


class Game:
    def __init__(self):
        self.cookies = 0
        self.cookie_per_click = 1
        self.cookie = pygame.Rect(400 - 150, 300 - 150, 300, 300)
        self.cookie_color = "#CD853F"
        self.clicked = False

        self.upgradeBtn = pygame.Rect(10, 50, 185, 75)
        self.upgrade1_cost = 5

        self.game_font = pygame.font.Font(None, 28)

    def upgrade(self):
        self.upgrade1_description = self.game_font.render(f"+{self.cookie_per_click} cookie per click", True, "#000000")
        self.display_cost = text_font.render(f"Cost: {str(self.upgrade1_cost)}", True, "#000000")

        pygame.draw.rect(screen, "#488ebd", self.upgradeBtn, border_radius=15)
        screen.blit(self.display_cost, (15, 85))
        screen.blit(self.upgrade1_description, (15,55))

    def draw_score(self):
        self.display_cookies = text_font.render(f"Cookies: {str(self.cookies)}", True, "#000000")
        screen.blit(self.display_cookies, (0,500))

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.cookies += self.cookie_per_click
                    self.clicked = False

        if self.upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.upgrade1_cost:
                    self.cookies -= self.upgrade1_cost
                    self.upgrade1_cost *= 3
                    self.cookie_per_click += 1
        
        pygame.draw.rect(screen, self.cookie_color, self.cookie, border_radius=150)

    def render(self):
        self.click_button()
        self.draw_score()
        self.upgrade()

pygame.init()

width = 800
height = 600

game = Game()

screen = pygame.display.set_mode(size=(width,height))
pygame.display.set_caption("Cookie Clicker")

text_font = pygame.font.Font(None, 50)
title = text_font.render("Cookie Clicker", True, "#000000")
clock = pygame.time.Clock()

while True:
    screen.fill("#98F5FF")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(title, (270,15))

    game.render()

    pygame.display.update()
    clock.tick(60)





