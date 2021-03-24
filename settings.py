class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана:
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0, 200, 0)
        
        # Настройки корабля:
        self.ship_limit = 3
        
        # Параметры снаряда:
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 255, 25)
        self.bullets_allowed = 25
        
        # Настройки пришельцев:
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует динамические(изменяемые) настройки игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.8
        self.alien_speed = 1

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
