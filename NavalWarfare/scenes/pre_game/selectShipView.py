import random
import arcade
from arcade.gui import UIManager
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
        self.v_box = arcade.gui.UIBoxLayout(vertical=False, space_between=20)

        # botones
        btn_anterior = arcade.gui.UIFlatButton(text="Anterior", width=100, height=25)
        btn_anterior.on_click = self.on_click_anterior
        self.v_box.add(btn_anterior)

        btn_seleccionar = arcade.gui.UIFlatButton(text="Seleccionar", width=100, height=25)
        btn_seleccionar.on_click = self.on_click_seleccionar
        self.v_box.add(btn_seleccionar)

        btn_siguiente = arcade.gui.UIFlatButton(text="Siguiente", width=100, height=25)
        btn_siguiente.on_click = self.on_click_siguiente
        self.v_box.add(btn_siguiente)

        self.anchor_volver_btn = arcade.gui.UIAnchorLayout()
        self.anchor_volver_btn.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=-230
        )

        self.uimanager.add(self.anchor_volver_btn)

        # sprites
        self.sprite_list0 = arcade.SpriteList()
        self.cover_imgs.center_x = WINDOW_WIDTH / 2
        self.cover_imgs.center_y = WINDOW_HEIGHT / 2
        self.cover_imgs.scale = 1
        self.sprite_list0.append(self.cover_imgs)

        self.sprite_list1 = arcade.SpriteList()
        self.all_warships = storage_utils.load_all_warships()
        self.current_index = random.randrange(len(self.all_warships))
        self.selecting_ship = self.all_warships[self.current_index]

        sprite_route = storage_utils.load_file(f"{self.selecting_ship.default_sprite}")
        self.ship_sprite = arcade.Sprite(sprite_route, scale=0.425, angle= -90)
        self.ship_sprite.center_x = (WINDOW_WIDTH // 2)- 250
        self.ship_sprite.center_y = WINDOW_HEIGHT // 2
        self.sprite_list1.append(self.ship_sprite)

        # Textos
        self.label0 = arcade.Text(
            "Seleccionando Barco",
            WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 1.1),
            color=arcade.color.WHITE,
            font_size=25,
            anchor_x="center",
            anchor_y="center"
        )

        self.label1 = arcade.Text(
            f"{self.selecting_ship.get_base_stats()}",
            WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 2)-30,
            color=arcade.color.WHITE,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            multiline=True,
            width=300 
        )

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        #self.sprite_list0.draw()
        self.sprite_list1.draw()
        self.uimanager.draw()
        self.label0.draw()
        self.label1.draw()

    def change_ship(self, direccion: int):
        total = len(self.all_warships)
        self.current_index = (self.current_index + direccion) % total
        self.selecting_ship = self.all_warships[self.current_index]

        new_route = storage_utils.load_file(f"{self.selecting_ship.default_sprite}")
        self.ship_sprite.texture = arcade.load_texture(new_route)
        print(f"Current ship: {self.selecting_ship.name}, {self.current_index}")
        self.label1.text = f"{self.selecting_ship.get_base_stats()}"

    def on_click_seleccionar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: seleccionar_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.uimanager.clear()

        from scenes.pre_game.MenuView import MenuView
        menu_view = MenuView(cover_imgs=self.cover_imgs, selected_warship=self.selecting_ship)
        menu_view.setup()
        self.window.show_view(menu_view)

    def on_click_siguiente(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: siguiente_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.change_ship(+1)

    def on_click_anterior(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: anterior_btn")
        storage_utils.execute_sound("button_sound1.mp3")
        self.change_ship(-1)
