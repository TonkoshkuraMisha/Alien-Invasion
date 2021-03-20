class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры."""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (114, 160, 193)
        # Салатовый - (85, 225, 20). Небесный - (204, 229, 255)