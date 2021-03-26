import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчёта очков."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счёта.
        self.text_color = (0, 0, 255)
        self.text_color_higt_score = (255, 0, 0)
        self.text_color_level = (0, 255, 0)
        self.text_color_ships_left = (255, 255, 0)
        self.font = pygame.font.Font('fonts/unicephalon.ttf', 28)
        # Подготовка изображений данных.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships_left()

    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(f"score:{score_str}", True, 
                self.text_color)
        # Можно задать цвет фона для счёта: ', self.settings.bg_color'.

        # Вывод счёта в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 40

    def prep_high_score(self):
        """Преобразует рекордный счёт в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(f"h-score:{high_score_str}", 
                True, self.text_color_higt_score)

        # Рекорд выравнивается сверху над текущим счётом.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 10

        ## Рекорд выравнивается по центру верхней стороны.
        #self.high_score_rect = self.high_score_image.get_rect()
        #self.high_score_rect.centerx = self.screen_rect.centerx
        #self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(f"level:{level_str}", True, 
                self.text_color_level)

        # Уровень выводиться над рекордным счётом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -20
        self.level_rect.top = 70

    def prep_ships_left(self):
        """Преобразует количество оставшихся жизней в графическое изображение"""
        ships_left_str = str(self.stats.ships_left)
        self.ships_left_image = self.font.render(f"ships:{ships_left_str}", 
                True, self.text_color_ships_left)

        # Количество оставшихся жизней выводиться под счётом.
        self.ships_left_rect = self.ships_left_image.get_rect()
        self.ships_left_rect.right = self.screen_rect.right - 20
        self.ships_left_rect.top = 100

    def show_score(self):
        """Выводит данные игры на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_left_image, self.ships_left_rect)

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()