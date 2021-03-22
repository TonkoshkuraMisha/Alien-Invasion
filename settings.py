class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры."""
        #Параметры экрана
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 200, 0)
        # Настройки корабля.
        self.ship_speed = 1.2
        # Параметры снаряда.
        self.bullet_speed = 2.2
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 255, 25)
        self.bullets_allowed = 5