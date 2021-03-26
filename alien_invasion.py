import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведения игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()

        pygame.mixer.music.load('sound/intro_normal.wav')
        pygame.mixer.music.play(loops = -1)
        self.shot = pygame.mixer.Sound('sound/shots/laser_blast.wav')
        self.button_play = pygame.mixer.Sound('sound/sound_play.wav')
        #self.flight_ship = pygame.mixer.Sound('sound/stinger-rocket.wav')
        # звук для движения вправо-влево.

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            #(self.settings.screen_width, 
            #self.settings.screen_height))
        # для полноэкранного режима нужно применить:
        # (0, 0), pygame.FULLSCREEN) - вставить в set_mode
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.bg_img = pygame.image.load('images/backgraunds/start_game_1366.jpg')
        pygame.display.set_caption("Alien Invasion")

        # Создание экземпляра для хранения игровой статистики и результатов игры.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


    def _check_events(self):
        """Обрабатываются нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('alien_invasion/hight_score.txt', 'w') as file_object:
                    file_object.write("Ну и в чём дело?")
                    file_object.close()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self.button_play.play()

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровой статистики.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            # Указатель мыши скрывается.
            pygame.mouse.set_visible(False)

            # Обновляются значения уровня и количества жизней перед началом
            # новой игры.
            self.sb.prep_level()
            self.sb.prep_ships()
            self.sb.prep_ships_left()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            #self.flight_ship.play()
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # При включении клавиш вверх-вниз и столкновении на некоторой высоте 
        # с пришельцами происходит множественная коллизия, которая приводит к тому,
        # что игра зависает. Нужно доработать.
            #self.flight_ship.play()
        #elif event.key == pygame.K_UP:
            #self.ship.moving_up = True
        #elif event.key == pygame.K_DOWN:
            #self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.shot.play()
        #Пасхалочка для тестировщиков - суперснаряды в два потока!(доделать!)
        elif event.key == pygame.K_a:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиции снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и пришельцев, учавствующих в коллизиях.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Увеличение уровня.
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            # Уменьшение ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            # Уменьшает количество жизней.
            self.sb.prep_ships_left()

            # Пауза.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же, что при столкновении с кораблём.
                self._ship_hit()
                break

    def _update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана,
            с последующим обновлением позиций всех пришельцев во флоте.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец - корабль."
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()


    def _create_fleet(self):
        """Создаёт флот пришельцев."""
        # Создание пришельца и вычисление количества пришельцев в ряду.
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        (alien_width, alien_height) = alien.rect.size
        available_space_x = self.settings.screen_width  - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
            (4 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(row_number, alien_number)
                # alien_number на первом месте, row_number - на втором!

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран."""
        #self.screen.fill(self.settings.bg_color) - однотонный цвет фона!
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Вывод информации о счёте.
        self.sb.show_score()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()