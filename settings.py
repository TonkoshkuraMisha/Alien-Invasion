class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана:
        self.screen_width = 1366
        self.screen_height = 768
        #self.bg_color = (0, 200, 0)
        
        # Настройки корабля:
        self.ship_limit = 3
        
        # Параметры снаряда корабля:
        self.bullet_width = 5
        self.bullet_height = 24
        self.bullet_color = (255, 255, 0)
        # (255, 255, 0) - цвет надписи Play.
        self.bullets_allowed = 10

        # Параметры снарядов пришельцев.
        #self.alien_bullet_width = 3
        #self.alien_bullet_height = 12
        #self.alien_bullet_color = (60, 240, 255)
        #self.alien_bullets_allowed = 4

        # Настройки пришельцев:
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.05
        # Темп роста стоимости пришельцев.
        self.speedup_scale_2 = 1.03

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует динамические(изменяемые) настройки игры."""
        self.ship_speed = 2.5
        self.bullet_speed = 2.2
        self.alien_speed = 1.5
        #self.alien_bullet_speed = 2.2

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчёт очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale_2
        self.alien_speed *= self.speedup_scale
        #self.alien_bullet_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale_2

        self.alien_points = int(self.alien_points * self.speedup_scale_2)
