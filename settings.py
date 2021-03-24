class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры."""
        
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0, 200, 0)
        
        # Настройки корабля.
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Параметры снаряда.
        self.bullet_speed = 2.8
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (255, 255, 25)
        self.bullets_allowed = 25
        
        # Настройки пришельцев.
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1