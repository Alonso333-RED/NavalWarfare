import arcade
from arcade.gui import UIManager
import config
from Actor import Actor
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION


class GameOverView(arcade.View):
    def __init__(self, player_wins: bool, player: Actor, enemy: Actor, background: arcade.Sprite, bg_color: tuple = (26, 26, 64)):
        super().__init__()
        self.background_color = bg_color
        self.uimanager = UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=0)
        self.player = player
        self.enemy = enemy
        self.background = background
        self.player_wins = player_wins

        self.bg_sprite_list = arcade.SpriteList()
        self.background.center_x = (WINDOW_WIDTH / 2)
        self.background.center_y = (WINDOW_HEIGHT / 2)
        self.background.scale = 1.25
        self.bg_sprite_list.append(self.background)

        self.player_sprite_list = self.player.load_sprite_list()
        self.enemy_sprite_list = self.enemy.load_sprite_list()

        if self.player_wins:
            result_text = "¡Victoria!"
            storage_utils.execute_sound("victory.mp3")
        else:
            result_text = "¡Derrota!"
            storage_utils.execute_sound("game_over.mp3")

        self.label0 = arcade.Text(
            f"{result_text}",
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2),
            color=arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center"
        )

        btn_menu = arcade.gui.UIFlatButton(text="Menu", width=500, height=25)
        btn_menu.on_click = self.on_click_menu
        self.v_box.add(btn_menu)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=-75
        )
        self.uimanager.add(self.anchor_layout)

        # DO
        storage_utils.execute_sound("warship_destroyed.mp3")

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg_sprite_list.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        self.label0.draw()
        self.uimanager.draw()

    def on_click_menu(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: menu_btn")
        storage_utils.execute_sound("button_sound0.mp3")
        self.clear()
        self.uimanager.clear()
        from scenes.pre_game.CoverView import CoverView
        cover_view = CoverView()
        self.window.show_view(cover_view)
