class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Игра Alien Invasion запукается в неактивном состоянии.
        self.game_active = False

        # Считывание текущего лучшего счёта из файла.
        hi_score = open('/alien_invasion/hight_score.txt', "r")
        data = hi_score.read()
        hi_score.close()

        # Рекорд не должен сбрасываться.
        self.score = 0
        self.high_score = 0
        # Считывание текущего лучшего счёта из файла.
        hi_score = open('/alien_invasion/hight_score.txt', "r")
        data = hi_score.read()
        hi_score.close()
        self.high_score = int(data)

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1