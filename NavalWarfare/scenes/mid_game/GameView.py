import random
import arcade
from arcade.gui import UIManager
import config
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION


class GameView(arcade.View):
    def __init__(self, selected_warship, enemy_warship, bg_color: tuple = (26, 26, 64)):
        super().__init__()
        self.background_color = bg_color
        self.uimanager = UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(vertical=False, space_between=20)
        self.player_warship = selected_warship
        self.enemy_warship = enemy_warship


        self.bg_sprite_list = arcade.SpriteList()
        self.background = arcade.Sprite(storage_utils.get_random_image("NavalWarfare/images/game_backgrounds"))
        self.background.center_x = (WINDOW_WIDTH / 2)
        self.background.center_y = (WINDOW_HEIGHT / 2)
        self.background.scale = 1.25
        self.bg_sprite_list.append(self.background)

        self.player_ship_sprite_list = arcade.SpriteList()
        player_ship_sprite_route = storage_utils.load_file(f"{self.player_warship.default_sprite}")
        self.player_ship_sprite = arcade.Sprite(player_ship_sprite_route, scale=0.425)
        self.player_ship_sprite.center_x = (WINDOW_WIDTH // 2)
        self.player_ship_sprite.center_y = (WINDOW_HEIGHT // 2) - 200
        self.player_ship_sprite_list.append(self.player_ship_sprite)

        self.enemy_ship_sprite_list = arcade.SpriteList()
        enemy_ship_sprite_route = storage_utils.load_file(f"{self.enemy_warship.default_sprite}")
        self.enemy_ship_sprite = arcade.Sprite(enemy_ship_sprite_route, scale=0.425)
        self.enemy_ship_sprite.center_x = (WINDOW_WIDTH // 2)
        self.enemy_ship_sprite.center_y = (WINDOW_HEIGHT // 2) + 200
        self.enemy_ship_sprite_list.append(self.enemy_ship_sprite)


    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg_sprite_list.draw()
        self.player_ship_sprite_list.draw()
        self.enemy_ship_sprite_list.draw()
        self.uimanager.draw()
