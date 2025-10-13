import time
import arcade
import arcade.gui
from utils import general_utils
import config


WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class CoverView(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 64), cover_imgs=None):
        super().__init__()
        self.background_color = bg_color
        self.cover_imgs = cover_imgs
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)

        # Botones
        btn_comenzar = arcade.gui.UIFlatButton(text="Comenzar", width=500, height=25)
        btn_comenzar.on_click = self.on_click_comenzar
        self.v_box.add(btn_comenzar)

        btn_tutorial = arcade.gui.UIFlatButton(text="Tutorial", width=500, height=25)
        btn_tutorial.on_click = self.on_click_tutorial
        self.v_box.add(btn_tutorial)

        btn_creditos = arcade.gui.UIFlatButton(text="Creditos", width=500, height=25)
        btn_creditos.on_click = self.on_click_creditos
        self.v_box.add(btn_creditos)

        btn_salir = arcade.gui.UIFlatButton(text="Salir", width=500, height=25,)
        btn_salir.on_click = self.on_click_salir
        self.v_box.add(btn_salir)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
        )

        self.uimanager.add(self.anchor_layout)

        # Inicializando Sistema de Sprites
        self.sprite_list = arcade.SpriteList()
        if self.cover_imgs is None:
            self.cover_imgs = arcade.Sprite(general_utils.get_random_image("NavalWarfare/images/cover"))
            self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
            self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
            self.cover_imgs.scale = 1
            self.sprite_list.append(self.cover_imgs)
        elif self.cover_imgs:
            self.sprite_list.append(self.cover_imgs)
            self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
            self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
            self.cover_imgs.scale = 1

        # Textos
        self.label0 = arcade.Text(
            "Naval Warfare",
            WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 1.25),
            color=arcade.color.WHITE,
            font_size=75,
            anchor_x="center",
            anchor_y="center"
        )

        self.label1 = arcade.Text(
            "alonso",
            (WINDOW_WIDTH / 2) - 250, (WINDOW_HEIGHT / 1.25) + 40,
            color=arcade.color.WHITE,
            font_size=15,
            anchor_x="center",
            anchor_y="center"
        )

        self.label2 = arcade.Text(
            f"{VERSION}",
            (WINDOW_WIDTH / 2) + 250, (WINDOW_HEIGHT / 1.25) - 50,
            color=arcade.color.WHITE,
            font_size=10,
            anchor_x="center",
            anchor_y="center"
        )

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        self.uimanager.draw()
        self.label0.draw()
        self.label1.draw()
        self.label2.draw()

    # Funciones de Botones
    def on_click_comenzar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: comenzar_btn")
        from scenes.pre_game.MenuView import MenuView
        self.uimanager.clear()
        arcade.play_sound(arcade.load_sound("NavalWarfare/sounds/button_sound0.mp3"))
        menu_view = MenuView(cover_imgs=self.cover_imgs)
        menu_view.setup()
        self.window.show_view(menu_view)

    def on_click_tutorial(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: tutorial_btn")
        from scenes.pre_game.TutorialView import TutorialView
        arcade.play_sound(arcade.load_sound("NavalWarfare/sounds/button_sound0.mp3"))
        self.uimanager.clear()
        tutorial_view = TutorialView(cover_imgs=self.cover_imgs)
        tutorial_view.setup()
        self.window.show_view(tutorial_view)

    def on_click_creditos(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: creditos_btn")
        from scenes.pre_game.CreditsView import CreditsView
        arcade.play_sound(arcade.load_sound("NavalWarfare/sounds/button_sound1.mp3"))
        self.uimanager.clear()
        credits_view = CreditsView(cover_imgs=self.cover_imgs)
        credits_view.setup()
        self.window.show_view(credits_view)

    def on_click_salir(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: salir_btn")
        arcade.play_sound(arcade.load_sound("NavalWarfare/sounds/button_sound1.mp3"))
        time.sleep(1)
        arcade.exit()
        exit()