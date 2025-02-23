import pygame

class Hero():
    def __init__(self, screen):
        self.image = pygame.image.load("image/hero.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.move_right = False
        self.move_left = False

    def output_hero(self):
        self.screen.blit(self.image, self.rect)

    def moving_hero(self, screen):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 4
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 4
    
    def create_hero_again(self):
        self.center = self.screen_rect.centerx