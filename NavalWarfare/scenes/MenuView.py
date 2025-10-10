import arcade
import arcade.gui
import config

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class MenuView(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 64), cover_imgs=None):
        super().__init__()
        self.background_color = bg_color
        self.cover_imgs = cover_imgs
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=20)

        btn_jugar = arcade.gui.UIFlatButton(text="Comenzar", width=500, height=25)
        btn_jugar.on_click = self.on_click_jugar
        self.v_box.add(btn_jugar)

        btn_volver = arcade.gui.UIFlatButton(text="Volver", width=500, height=25)
        btn_volver.on_click = self.on_click_volver
        self.v_box.add(btn_volver)

        self.sprite_list = arcade.SpriteList()
        self.cover_imgs.center_x = (WINDOW_WIDTH / 2)
        self.cover_imgs.center_y = (WINDOW_HEIGHT / 2)
        self.cover_imgs.scale = 1
        self.sprite_list.append(self.cover_imgs)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y"
        )
        self.uimanager.add(self.anchor_layout)

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
            (WINDOW_WIDTH / 2) - 260, (WINDOW_HEIGHT / 2) + 240,
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

    def on_click_jugar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: jugar_btn")
        from scenes.CoverView import CoverView
        cover_view = CoverView(cover_imgs=self.cover_imgs)
        cover_view.setup()
        self.window.show_view(cover_view)

    def on_click_volver(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: volver_btn")
        from scenes.CoverView import CoverView
        cover_view = CoverView(cover_imgs=self.cover_imgs)
        cover_view.setup()
        self.window.show_view(cover_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            from scenes.CoverView import CoverView
            cover_view = CoverView(cover_imgs=self.cover_imgs)
            cover_view.setup()
            self.window.show_view(cover_view)