import arcade
import copy
import config
from Warship import Warship
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class Actor:
    def __init__(self, warship: Warship, is_enemy: bool = False):
        self.warship = copy.deepcopy(warship)
        self.points = 0
        self.is_enemy = is_enemy

    def sprite_ubicate(self, sprite: arcade.Sprite):
        
        if self.is_enemy:
            sprite.center_x = (WINDOW_WIDTH // 2) - 80
            sprite.center_y = (WINDOW_HEIGHT // 2) + 200
        else:
            sprite.center_x = (WINDOW_WIDTH // 2) + 75
            sprite.center_y = (WINDOW_HEIGHT // 2) - 200


    def load_sprite(self, sprite_route: str):
        sprite_route = storage_utils.load_file(f"{sprite_route}")
        sprite = arcade.Sprite(sprite_route, scale=0.425)
        self.sprite_ubicate(sprite)
        return sprite

    def load_sprite_list(self):
        default_sprite = self.load_sprite(self.warship.default_sprite)
        damaged_sprite = self.load_sprite(self.warship.damaged_sprite)
        repaired_sprite = self.load_sprite(self.warship.repaired_sprite)

        sprite_list = arcade.SpriteList()
        sprite_list.append(default_sprite)
        sprite_list.append(damaged_sprite)
        sprite_list.append(repaired_sprite)

        sprite_list[1].visible = False
        sprite_list[2].visible = False
        
        return sprite_list