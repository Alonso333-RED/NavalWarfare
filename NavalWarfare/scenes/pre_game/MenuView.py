import random
import arcade
import arcade.gui
import config
from utils import storage_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class MenuView(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 64), cover_imgs=None, selected_warship=None):
        super().__init__()
        self.background_color = bg_color
        self.cover_imgs = cover_imgs
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)
        self.selected_warship = selected_warship

        # Botones
        btn_jugar = arcade.gui.UIFlatButton(text="Jugar", width=500, height=25)
        btn_jugar.on_click = self.on_click_jugar
        self.v_box.add(btn_jugar)

        btn_select_ship = arcade.gui.UIFlatButton(text="Seleccionar Buque", width=500, height=25)
        btn_select_ship.on_click = self.on_click_select_ship
        self.v_box.add(btn_select_ship)

        btn_volver = arcade.gui.UIFlatButton(text="Volver", width=500, height=25)
        btn_volver.on_click = self.on_click_volver
        self.v_box.add(btn_volver)

        btn_test0 = arcade.gui.UIFlatButton(text="Test0", width=500, height=25)
        btn_test0.on_click = self.on_click_test0
        self.v_box.add(btn_test0)
        
        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y"
        )
        self.uimanager.add(self.anchor_layout)

        # Inicializando Sistema de Sprites
        self.sprite_list0 = arcade.SpriteList()
        self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
        self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
        self.cover_imgs.scale = 1
        self.sprite_list0.append(self.cover_imgs)

        # Textos
        self.label0 = arcade.Text(
            "Menu Principal",
            WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 1.25),
            color=arcade.color.WHITE,
            font_size=75,
            anchor_x="center",
            anchor_y="center"
        )

        self.label1 = arcade.Text(
            f"Naval Warfare, ({VERSION}) por Alonso",
            (WINDOW_WIDTH / 2) - 240, (WINDOW_HEIGHT / 2) + 240,
            color=arcade.color.WHITE,
            font_size=10,
            anchor_x="center",
            anchor_y="center"
        )

        # random ship
        self.all_warships = storage_utils.load_all_warships()
        if self.selected_warship == None:
            self.current_index = random.randrange(len(self.all_warships))
            self.selected_warship = self.all_warships[self.current_index]

        self.sprite_list1 = arcade.SpriteList()
        sprite_route = storage_utils.load_file(f"{self.selected_warship.default_sprite}")
        self.ship_sprite = arcade.Sprite(sprite_route, scale=0.425)
        self.ship_sprite.center_x = (WINDOW_WIDTH // 2)
        self.ship_sprite.center_y = (WINDOW_HEIGHT // 2) - 200
        self.sprite_list1.append(self.ship_sprite)

        self.label0 = arcade.Text(
            self.selected_warship.name,
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 125,
            color=arcade.color.WHITE,
            font_size=20,
            anchor_x="center",
            anchor_y="center"
        )

        self.enemy_warship = random.choice(self.all_warships)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.sprite_list0.draw()
        self.sprite_list1.draw()
        self.uimanager.draw()
        self.label0.draw()
        self.label1.draw()

    # Funciones de Botones
    def on_click_jugar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: jugar_btn")
        storage_utils.execute_sound("button_sound0.mp3")
        self.uimanager.clear()
        from scenes.mid_game.GameView import GameView
        game_view = GameView(selected_warship=self.selected_warship, enemy_warship=self.enemy_warship)
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_select_ship(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: select_ship_btn")
        storage_utils.execute_sound("button_sound0.mp3")
        self.uimanager.clear()
        from scenes.pre_game.selectShipView import selecShipView
        select_ship_view = selecShipView(cover_imgs=self.cover_imgs)
        select_ship_view.setup()
        self.window.show_view(select_ship_view)

    def on_click_volver(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: volver_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.uimanager.clear()
        from scenes.pre_game.CoverView import CoverView
        cover_view = CoverView(cover_imgs=self.cover_imgs)
        cover_view.setup()
        self.window.show_view(cover_view)

    def on_click_test0(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: test0_btn")
        storage_utils.execute_sound("button_sound0.mp3")
        self.uimanager.clear()
        from scenes.test_scenes.test0 import Test0
        test0_view = Test0(cover_imgs=self.cover_imgs)
        test0_view.setup()
        self.window.show_view(test0_view)