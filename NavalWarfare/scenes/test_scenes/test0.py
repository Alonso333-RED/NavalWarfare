import arcade
import arcade.gui
import config
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class Test0(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 64), cover_imgs=None):
        super().__init__()
        self.background_color = bg_color
        self.cover_imgs = cover_imgs
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=20)

        btn_volver = arcade.gui.UIFlatButton(
            text="Volver",
            width=100,
            height=25
            )
        btn_volver.on_click = self.on_click_volver
        self.v_box.add(btn_volver)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x = -320,
            align_y = -230
            )

        self.uimanager.add(self.anchor_layout)

        self.sprite_list = arcade.SpriteList()
        self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
        self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
        self.cover_imgs.scale = 1
        self.sprite_list.append(self.cover_imgs)

        #load yamato sprite
        self.ijnYamato = storage_utils.load_warship("uss_missouri")
        self.kmsBismarck = storage_utils.load_warship("kms_bismarck")
        self.fsRichelieu = storage_utils.load_warship("fs_richelieu")
        self.yamato_sprite_default = arcade.Sprite(storage_utils.load_file(f"{self.ijnYamato.default_sprite}"), scale=0.25)
        self.yamato_sprite_default.center_x = WINDOW_WIDTH // 2
        self.yamato_sprite_default.center_y = (WINDOW_HEIGHT // 2)
        self.sprite_list.append(self.yamato_sprite_default)

        self.yamato_sprite_damaged = arcade.Sprite(storage_utils.load_file(f"{self.kmsBismarck.damaged_sprite}"), scale=0.25)
        self.yamato_sprite_damaged.center_x = WINDOW_WIDTH // 2
        self.yamato_sprite_damaged.center_y = (WINDOW_HEIGHT // 2) + 125
        self.sprite_list.append(self.yamato_sprite_damaged)

        self.yamato_sprite_repaired = arcade.Sprite(storage_utils.load_file(f"{self.fsRichelieu.repaired_sprite}"), scale=0.25)
        self.yamato_sprite_repaired.center_x = WINDOW_WIDTH // 2
        self.yamato_sprite_repaired.center_y = (WINDOW_HEIGHT // 2) - 125
        self.sprite_list.append(self.yamato_sprite_repaired)
    
    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        self.uimanager.draw()

    def on_click_volver(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: volver_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.uimanager.clear()
        from scenes.pre_game.MenuView import MenuView
        menu_view = MenuView(cover_imgs=self.cover_imgs)
        menu_view.setup()
        self.window.show_view(menu_view)