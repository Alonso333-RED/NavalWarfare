import random
import time
import arcade
from arcade.gui import UIManager
import config
from Warship import Warship
from Actor import Actor
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION


class GamePreparation(arcade.View):
    def __init__(self, selected_warship: Warship, enemy_warship: Warship, bg_color: tuple = (26, 26, 64)):
        super().__init__()
        self.background_color = bg_color
        self.uimanager = UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(vertical=False, space_between=20)
        self.player = Actor(selected_warship)
        self.enemy = Actor(enemy_warship, True)

        self.bg_sprite_list = arcade.SpriteList()
        self.background = arcade.Sprite(storage_utils.get_random_image("NavalWarfare/images/game_backgrounds"))
        self.background.center_x = (WINDOW_WIDTH / 2)
        self.background.center_y = (WINDOW_HEIGHT / 2)
        self.background.scale = 1.25
        self.bg_sprite_list.append(self.background)

        self.player_sprite_list = self.player.load_sprite_list()
        self.enemy_sprite_list = self.enemy.load_sprite_list()

        self.label0 = arcade.Text(
            f"{self.player.warship.name} V/S {self.enemy.warship.name}",
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2),
            color=arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center"
        )

        btn_empezar = arcade.gui.UIFlatButton(text="Empezar", width=500, height=25)
        btn_empezar.on_click = self.on_click_empezar
        self.v_box.add(btn_empezar)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=-75
        )
        self.uimanager.add(self.anchor_layout)

        self.enemy.warship.current_speed = self.enemy.warship.max_speed

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg_sprite_list.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        self.label0.draw()
        self.uimanager.draw()

    def on_click_empezar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: empezar_btn")
        storage_utils.execute_sound("button_sound0.mp3")
        self.clear()
        self.uimanager.clear()
        from scenes.mid_game.PlayerTurnView import PlayerTurnView
        player_turn = PlayerTurnView(self.player, self.enemy, self.background)
        player_turn.setup()
        self.window.show_view(player_turn)
