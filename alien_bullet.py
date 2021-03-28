import pygame
from pygame.sprite import Sprite

class Alien_Bullet(Sprite):
    """Класс для управления снарядами, выпущеными пришельцами."""

    def __init__(self, ai_game):
        """Создаёт объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width, 
            self.settings.alien_bullet_height)
        self.rect.midtop = ai_game.alien.rect.midbottom

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд пришельцев вниз по экрану."""#_alien_bullet
        # Обновление позиции снаряда пришельцев в вещественном формате.
        self.y += self.settings.alien_bullet_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """Вывод снаряда пришельцев на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
