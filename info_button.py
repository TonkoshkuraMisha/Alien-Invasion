import pygame.font

class Info_Button():

    def __init__(self, ai_game, info):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопки.
        self.width, self.height = 450, 690
        self.info_button_color = (0, 0, 0)
        self.info_text_color = (0, 255, 0)
        self.font = pygame.font.Font('fonts/unicephalon.ttf', 24)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(10, 70, self.width, self.height)
        #self.rect.center = self.screen_rect.center

        # Сообщение кнопки создаётся только один раз.
        self._prep_info(info)

    def _prep_info(self, info):
        """Преобразует info в прямоугольник и выравнивает текст по центру."""
        self.info_image = self.font.render(info, True, self.info_text_color,
                self.info_button_color)
        self.info_image_rect = self.info_image.get_rect()
        self.info_image_rect.center = self.rect.center

    def draw_button_info(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.info_button_color, self.rect)
        self.screen.blit(self.info_image, self.info_image_rect)