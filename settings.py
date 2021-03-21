class Settings():
    """Клас для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует настройки игры."""
        #Параметры экрана
        self.screen_width = 1080
        self.screen_height = 680
        self.bg_color = (0, 200, 0)
        # Салатовый - (85, 225, 20). Небесный - (204, 229, 255)