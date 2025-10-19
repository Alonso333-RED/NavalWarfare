import random
import arcade
from arcade.gui import UIManager, UIDropdown, UIAnchorLayout, UIOnChangeEvent
import config
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class selecShipView(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 64), cover_imgs=None):
        super().__init__()
        self.background_color = bg_color
        self.cover_imgs = cover_imgs
        self.uimanager = UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)

        btn_volver = arcade.gui.UIFlatButton(
            text="Volver",
            width=100,
            height=25
        )
        btn_volver.on_click = self.on_click_volver
        self.v_box.add(btn_volver)

        self.anchor_volver_btn = arcade.gui.UIAnchorLayout()
        self.anchor_volver_btn.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=-320,
            align_y=-230
        )

        self.uimanager.add(self.anchor_volver_btn)

        self.sprite_list0 = arcade.SpriteList()
        self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
        self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
        self.cover_imgs.scale = 1
        self.sprite_list0.append(self.cover_imgs)

        self.sprite_list1 = arcade.SpriteList()
        all_warships = storage_utils.load_all_warships()
        self.selecting_ship = random.choice(all_warships)
        self.some_sprite = arcade.Sprite(storage_utils.load_file(f"{self.selecting_ship.default_sprite}"), scale=1)
        self.some_sprite.center_x = WINDOW_WIDTH // 2
        self.some_sprite.center_y = (WINDOW_HEIGHT // 2)
        self.sprite_list1.append(self.some_sprite)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.sprite_list0.draw()
        self.sprite_list1.draw()
        self.uimanager.draw()

    def on_click_volver(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: volver_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.uimanager.clear()
        from scenes.pre_game.MenuView import MenuView
        menu_view = MenuView(cover_imgs=self.cover_imgs)
        menu_view.setup()
        self.window.show_view(menu_view)
